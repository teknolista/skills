"""Check skill metadata, collection links, catalog versions, and installation coverage."""
from collections import Counter
import os
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
import subprocess

import yaml


class FrontmatterLoader(yaml.SafeLoader):
    def construct_mapping(self, node, deep=False):
        mapping = super().construct_mapping(node, deep=deep)
        if len(mapping) != len(node.value):
            raise yaml.YAMLError("duplicate mapping key")
        return mapping


def frontmatter(entry):
    lines = entry.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        raise ValueError("missing YAML frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError("unterminated YAML frontmatter") from exc
    data = yaml.load("\n".join(lines[1:end]), Loader=FrontmatterLoader)
    if not isinstance(data, dict):
        raise ValueError("frontmatter must be a YAML mapping")
    return data


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
descriptions = {}
mit_notice = (root / "LICENSE").read_bytes()
for entry in entries:
    package = entry.parent.name
    if not entry.is_file() or entry.resolve() not in files:
        continue
    if f"your-project/.agents/skills/{package}/SKILL.md" not in readme:
        problems.append(f"Missing manual installation entry for {package}")
    try:
        data = frontmatter(entry)
    except (ValueError, yaml.YAMLError) as exc:
        problems.append(f"{package}: {exc}")
        continue
    if data.get("name") != package or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", package) or len(package) > 64:
        problems.append(f"Invalid or mismatched skill name for {package}")
    description = data.get("description")
    if not isinstance(description, str) or not description.strip() or len(description) > 1024:
        problems.append(f"Invalid description for {package}")
    else:
        normalized = " ".join(description.casefold().split())
        if normalized in descriptions:
            problems.append(f"Duplicate description for {package} and {descriptions[normalized]}")
        descriptions[normalized] = package
    if data.get("license") != "MIT":
        problems.append(f"{package}: expected MIT license metadata")
    notice = entry.parent / "LICENSE"
    if notice not in files or notice.is_symlink() or not notice.is_file() or notice.read_bytes() != mit_notice:
        problems.append(f"{package}: standalone LICENSE must match the repository MIT notice")
    metadata = data.get("metadata")
    version = metadata.get("version") if isinstance(metadata, dict) else None
    if not isinstance(version, str) or not re.fullmatch(r"(?:0|[1-9][0-9]*)(?:\.(?:0|[1-9][0-9]*)){2}", version):
        problems.append(f"Invalid release version metadata for {package}")
        continue
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
print(f"{len(markdown)} Markdown files, {checked} local links/anchors, {len(entries)} version checks, {len(problems)} issues")
for problem in problems:
    print(problem)
raise SystemExit(bool(problems))
