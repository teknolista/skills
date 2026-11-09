"""Check collection links, catalog versions and complete manual-install coverage. Run from the repository root."""
from collections import Counter
import os
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import subprocess

root = Path.cwd()
inventory = subprocess.check_output(
    ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"]
)
files = {root / os.fsdecode(path) for path in inventory.split(b"\0") if path}
directories = {root}
for file in files:
    directories.update(parent for parent in file.parents if root in parent.parents)
markdown = sorted(file for file in files if file.suffix == ".md")
headings = re.compile(r"^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$", re.M)
links = re.compile(r"(?<!!)\[[^\]\n]*\]\((<[^>]+>|[^)\s]+)\)")
def anchors(path):
    counts = Counter()
    result = set()
    for title in headings.findall(path.read_text()):
        slug = re.sub(r"[^\w -]", "", title.lower()).replace(" ", "-")
        seq = counts[slug]
        counts[slug] += 1
        result.add(f"{slug}-{seq}" if seq else slug)
    return result

checked = 0
problems = []
for file in markdown:
    if not file.is_file() or file.resolve() not in files:
        problems.append(f"{file.relative_to(root)} is missing or resolves outside the collection")
        continue
    fenced = None
    for number, row in enumerate(file.read_text().splitlines(), 1):
        fence = re.match(r"^\s*(`{3,}|~{3,})", row)
        if fence:
            marker = fence[1]
            if not fenced:
                fenced = marker
            elif marker[0] == fenced[0] and len(marker) >= len(fenced):
                fenced = None
            continue
        if fenced:
            continue
        for raw in links.findall(row):
            parsed = urlsplit(raw.strip("<>"))
            if parsed.scheme or parsed.netloc:
                continue
            path = file if not parsed.path else Path(os.path.abspath(file.parent / unquote(parsed.path)))
            checked += 1
            if not path.exists() or any(
                target not in files and target not in directories for target in (path, path.resolve())
            ):
                problems.append(f"{file.relative_to(root)}:{number} missing or outside collection: {raw}")
            elif parsed.fragment and path.suffix == ".md" and unquote(parsed.fragment) not in anchors(path):
                problems.append(f"{file.relative_to(root)}:{number} missing anchor {raw}")

entries = sorted(file for file in markdown if file.name == "SKILL.md" and file.parent.parent == root)
readme = (root / "README.md").read_text()
labels = {
    "penta-pro":"PentaPRO", "peer-review":"Peer Review", "cybersec":"Cybersecurity",
    "ui-design":"UI Design", "diagnose-defect":"Diagnose Defect",
    "software-delivery":"Software Delivery", "technical-research":"Technical Research", "git-delivery":"Git Delivery", "agent-instructions":"Agent Instructions", "behavior-testing":"Behavior Testing", "http-api":"HTTP API", "mcp-server":"MCP Server",
}
versions = {}
for entry in entries:
    package = entry.parent.name
    if not entry.is_file() or entry.resolve() not in files:
        continue
    match = re.search(r'^  version: "(.*?)"$', entry.read_text(), re.M)
    if not match:
        problems.append(f"Missing version metadata for {package}")
        continue
    version = match[1]
    versions[package] = version
    if package in labels:
        label = labels[package]
        slug = label.lower().replace(" ", "-")
        if f"| [{label}](#{slug}) | {version} |" not in readme:
            problems.append(f"README version mismatch for {package}")
    elif f"]({package}/SKILL.md) | {version} |" not in readme:
        problems.append(f"README version mismatch for {package}")

process_template = root / "penta-pro/assets/process.md"
if (
    "penta-pro" not in versions
    or process_template not in files
    or process_template.resolve() not in files
    or not process_template.is_file()
    or f"| Template version | {versions['penta-pro']} |" not in process_template.read_text()
):
    problems.append("PentaPRO template version mismatch")
for entry in entries:
    if not entry.is_file() or entry.resolve() not in files:
        continue
    name = entry.parent.name
    if f"your-project/.agents/skills/{name}/SKILL.md" not in readme:
        problems.append(f"Missing manual installation entry for {name}")
    if not re.search(r"^name: " + re.escape(name) + r"$", entry.read_text(), re.M):
        problems.append(f"Directory/name mismatch for {name}")
print(f"{len(markdown)} Markdown files, {checked} local links/anchors, {len(entries)} version checks, {len(problems)} issues")
for problem in problems:
    print(problem)
raise SystemExit(bool(problems))
