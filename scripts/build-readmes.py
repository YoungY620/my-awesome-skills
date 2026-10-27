#!/usr/bin/env python3
"""Regenerate README.md and README.zh-CN.md from skills/index.json.

The two READMEs are generated artifacts: edit skills/index.json, run this
script, and commit the results. CI fails if they drift apart.
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def render(repo, skills, lang):
    if lang == "en":
        title, heading = repo["name"], "Skills"
        tagline = repo["tagline_en"]
        key = "summary_en"
    else:
        title, heading = repo["name"], "技能列表"
        tagline = repo["tagline_zh"]
        key = "summary_zh"
    lines = [f"# {title}", "", tagline, "", f"## {heading}", ""]
    for skill in skills:
        lines.append(f"- **[{skill['dir']}](skills/{skill['dir']}/)** — {skill[key]}")
    return "\n".join(lines) + "\n"


def main():
    index = json.loads((ROOT / "skills" / "index.json").read_text())
    repo, skills = index["repo"], index["skills"]
    for lang, filename in (("en", "README.md"), ("zh", "README.zh-CN.md")):
        (ROOT / filename).write_text(render(repo, skills, lang))
    if "--check" in sys.argv:
        result = subprocess.run(["git", "-C", str(ROOT), "diff", "--exit-code", "--", "README.md", "README.zh-CN.md"])
        if result.returncode != 0:
            print("READMEs are out of sync with skills/index.json; run scripts/build-readmes.py and commit.", file=sys.stderr)
            sys.exit(result.returncode)
        print("READMEs are in sync with skills/index.json.")


if __name__ == "__main__":
    main()
