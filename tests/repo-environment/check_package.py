"""Check basic package structure and local references in an isolated copy.

Uses only the Python standard library. This is not a host/schema validator
and does not evaluate skill behavior or install anything into Codex.
"""

import json
import re
import shutil
import tempfile
from pathlib import Path
from urllib.parse import unquote, urlsplit


def check_package(package: Path) -> tuple[int, int]:
    manifest = json.loads((package / "plugin.json").read_text(encoding="utf-8"))
    for field in ("name", "version", "description"):
        if not isinstance(manifest.get(field), str) or not manifest[field].strip():
            raise ValueError(f"Missing plugin metadata: {field}")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", manifest["name"]):
        raise ValueError("Invalid plugin name")

    skills = list((package / "skills").glob("*/SKILL.md"))
    if not skills:
        raise ValueError("No packaged skills found")
    for skill in skills:
        content = skill.read_text(encoding="utf-8")
        header = re.match(r"\A---\n(.*?)\n---\n", content, re.DOTALL)
        if not header:
            raise ValueError(f"Missing skill frontmatter: {skill}")
        for field in ("name", "description"):
            match = re.search(rf"^{field}: (.+)$", header[1], re.MULTILINE)
            if not match or not match[1].strip():
                raise ValueError(f"Missing skill {field}: {skill}")
            if field == "name" and match[1] != skill.parent.name:
                raise ValueError(f"Skill name/folder mismatch: {skill}")

    links = 0
    for document in package.rglob("*.md"):
        content = document.read_text(encoding="utf-8")
        for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", content):
            url = urlsplit(target)
            if url.scheme in ("https", "http"):
                continue
            if url.scheme or url.netloc:
                raise ValueError(f"Unsupported link: {document}: {target}")
            resolved = (document.parent / unquote(url.path)).resolve()
            if not resolved.is_relative_to(package):
                raise ValueError(f"Reference leaves the package: {document}: {target}")
            if not resolved.is_file():
                raise ValueError(f"Missing packaged reference: {document}: {target}")
            links += 1
    return len(skills), links


def main() -> None:
    source = Path(__file__).resolve().parents[2] / "plugins" / "repo-environment"
    for path in source.rglob("*"):
        if path.is_symlink():
            raise ValueError(f"Symlink requires explicit packaging review: {path}")
    with tempfile.TemporaryDirectory(prefix="repo-environment-package-") as temporary:
        package = Path(temporary) / "target" / ".agents" / "plugins" / source.name
        shutil.copytree(source, package)
        skills, links = check_package(package.resolve())
        print(f"PASS: isolated package, {skills} skills, {links} local references")


if __name__ == "__main__":
    main()
