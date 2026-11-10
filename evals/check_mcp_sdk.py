"""In-process Streamable HTTP smoke test with the official MCP Python SDK 2.2.0."""

import asyncio
from importlib.metadata import version
from typing import TypedDict

from httpx2 import ASGITransport, AsyncClient, ReadError
from mcp import Client
from mcp.client.streamable_http import streamable_http_client
from mcp.server.mcpserver import Context, MCPServer
from mcp.server.mcpserver.exceptions import ToolError

LEGACY = "2025-11-25"
MODERN = "2026-07-28"
ENDPOINT = "http://127.0.0.1:8000/mcp"
META = "io.modelcontextprotocol/"
server = MCPServer("synthetic-receipts")
receipts = {}
effects = []


def fixture_principal(ctx: Context) -> str:
    # Use real authentication in a deployed server. This header selects a fixture principal.
    value = ctx.request_context.request.headers.get("X-Fixture-Principal")
    if value not in {"tenant-a", "tenant-b"}:
        raise ToolError("fixture principal required")
    return value


class ReceiptResult(TypedDict):
    handle: str


@server.tool()
async def create_receipt(request_id: str, ctx: Context) -> ReceiptResult:
    principal = fixture_principal(ctx)
    key = (principal, request_id)
    if key not in receipts:
        handle = f"receipt-{len(effects) + 1}"
        effects.append((principal, request_id))
        receipts[key] = handle
    return {"handle": receipts[key]}


@server.tool()
async def read_receipt(handle: str, ctx: Context) -> ReceiptResult:
    principal = fixture_principal(ctx)
    if not any(owner == principal and owned_handle == handle for (owner, _), owned_handle in receipts.items()):
        raise ToolError("handle not accessible")
    return {"handle": handle}


def rpc(method, request_id, params=None):
    body = {"jsonrpc": "2.0", "method": method, "params": params or {}}
    if request_id is not None:
        body["id"] = request_id
    return body


async def legacy_start(client):
    response = await client.post(ENDPOINT, json=rpc("initialize", 1, {
        "protocolVersion": LEGACY,
        "clientInfo": {"name": "legacy-fixture", "version": "1"},
        "capabilities": {},
    }))
    assert response.status_code == 200 and response.json()["result"]["protocolVersion"] == LEGACY, response.text
    headers = {"Mcp-Session-Id": response.headers["Mcp-Session-Id"], "MCP-Protocol-Version": LEGACY}
    ready = await client.post(ENDPOINT, headers=headers, json=rpc("notifications/initialized", None))
    assert ready.status_code == 202, ready.text
    return headers


async def modern(client, method, request_id, *, revision=MODERN, name=None, arguments=None, header_name=None):
    headers = {"MCP-Protocol-Version": revision, "Mcp-Method": method}
    params = {"_meta": {META + "protocolVersion": revision, META + "clientCapabilities": {}}}
    if name:
        headers["Mcp-Name"] = header_name or name
        params.update(name=name, arguments=arguments or {})
    return await client.post(ENDPOINT, headers=headers, json=rpc(method, request_id, params))


class FixtureTransport(ASGITransport):
    discard_next_response = False

    async def handle_async_request(self, request):
        response = await super().handle_async_request(request)
        if self.discard_next_response:
            self.discard_next_response = False
            assert response.status_code == 200 and "Mcp-Session-Id" not in response.headers
            await response.aclose()
            raise ReadError("synthetic loss after the server handled the request", request=request)
        return response


async def main():
    app = server.streamable_http_app(json_response=True)
    transport = FixtureTransport(app)
    defaults = {"Accept": "application/json, text/event-stream"}
    async with (
        app.router.lifespan_context(app),
        AsyncClient(transport=transport, headers=defaults | {"X-Fixture-Principal": "tenant-a"}) as first,
        AsyncClient(transport=transport, headers=defaults | {"X-Fixture-Principal": "tenant-b"}) as second,
    ):
        legacy = await legacy_start(first)
        legacy_list = await first.post(ENDPOINT, headers=legacy, json=rpc("tools/list", 2))
        assert [tool["name"] for tool in legacy_list.json()["result"]["tools"]] == ["create_receipt", "read_receipt"]

        # The first modern request goes straight to the tool, with no discover or session.
        request = {"request_id": "abc"}
        transport.discard_next_response = True
        try:
            await modern(first, "tools/call", 7, name="create_receipt", arguments=request)
        except ReadError:
            pass
        else:
            raise AssertionError("the first response must be discarded")
        assert effects == [("tenant-a", "abc")], effects

        retry = await modern(first, "tools/call", 8, name="create_receipt", arguments=request)
        body = retry.json()
        assert body["id"] == 8 and body["result"]["structuredContent"] == {"handle": "receipt-1"}, body
        assert effects == [("tenant-a", "abc")], effects
        legacy_retry = await first.post(ENDPOINT, headers=legacy, json=rpc("tools/call", 3, {
            "name": "create_receipt", "arguments": request,
        }))
        assert legacy_retry.json()["result"]["structuredContent"] == {"handle": "receipt-1"}, legacy_retry.text
        assert effects == [("tenant-a", "abc")], effects

        owned_handle = {"handle": "receipt-1"}
        allowed = await modern(first, "tools/call", 9, name="read_receipt", arguments=owned_handle)
        assert allowed.json()["result"]["structuredContent"] == owned_handle, allowed.text
        denied = await modern(second, "tools/call", 9, name="read_receipt", arguments=owned_handle)
        denied_result = denied.json()["result"]
        assert denied_result["isError"] is True and "structuredContent" not in denied_result, denied.text
        independent = await modern(second, "tools/call", 10, name="create_receipt", arguments=request)
        assert independent.json()["result"]["structuredContent"] == {"handle": "receipt-2"}, independent.text

        mismatch = await modern(first, "tools/call", 11, name="create_receipt", header_name="read_receipt",
                                arguments={"request_id": "must-not-run"})
        assert mismatch.json()["error"]["code"] == -32020, mismatch.text
        unsupported = await modern(first, "tools/list", 12, revision="2099-01-01")
        assert unsupported.json()["error"]["code"] == -32022, unsupported.text
        assert effects == [("tenant-a", "abc"), ("tenant-b", "abc")], effects

        async with Client(streamable_http_client(ENDPOINT, http_client=first)) as sdk_client:
            assert sdk_client.protocol_version == MODERN, sdk_client.protocol_version
            tools = await sdk_client.list_tools()
            assert [tool.name for tool in tools.tools] == ["create_receipt", "read_receipt"], tools
            assert tools.ttl_ms is not None and tools.cache_scope is not None, tools

        closed = await first.delete(ENDPOINT, headers=legacy)
        assert closed.status_code == 200, closed.text

    print(f"MCP Python SDK {version('mcp')}: legacy session, modern direct call, SDK discovery, "
          "retry after simulated response loss, principal-scoped handles, and version/header errors passed.")


if __name__ == "__main__":
    asyncio.run(main())
