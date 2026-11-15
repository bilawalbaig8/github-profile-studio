"""Check this portable skill package; no dependencies or network operations."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


def validate(root: Path) -> list[str]:
    errors = []
    skill = root / "skills/github-profile-studio/SKILL.md"
    if not skill.is_file():
        return ["Missing skill entry point"]
    content = skill.read_text(encoding="utf-8")
    match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", content, re.S)
    fields = dict(re.findall(r"^([a-z-]+):\s*(.+)$", match[1], re.M)) if match else {}
    if fields.get("name") != "github-profile-studio" or not fields.get("description"):
        errors.append("Skill needs valid name and description frontmatter")
    for name in ("intake", "design-brief", "project-state"):
        path = skill.parent / "templates" / (name + ".md")
        if not path.is_file() or len(path.read_text(encoding="utf-8").strip()) < 150:
            errors.append(f"Missing or empty template: {name}")
    for path in sorted(root.rglob("*.md")):
        if ".git" in path.relative_to(root).parts:
            continue
        body = path.read_text(encoding="utf-8")
        # Inline links used by this package; not a general Markdown parser.
        for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", body):
            target = target.strip().strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            resolved = (path.parent / unquote(parsed.path)).resolve()
            if not resolved.is_relative_to(root.resolve()):
                errors.append(f"Link leaves package: {path.relative_to(root)} -> {target}")
            elif not resolved.exists():
                errors.append(f"Broken local link: {path.relative_to(root)} -> {target}")
        if re.search(r"\b(?:TODO|TBD|FIXME)\b|\[INSERT[^\]]*\]", body):
            errors.append(f"Unfinished scaffold: {path.relative_to(root)}")
    return errors


if __name__ == "__main__":
    base = Path(__file__).resolve().parents[1]
    findings = validate(base)
    if findings:
        print("\n".join(findings))
        sys.exit(1)
    files = [p for p in base.rglob("*") if p.is_file() and ".git" not in p.relative_to(base).parts]
    print(f"PASS: frontmatter, 3 templates and local Markdown paths; {len(files)} package files")
