from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
READMES = [
    "README.md",
    "README.zh-CN.md",
    "README.ja.md",
    "README.ko.md",
    "README.es.md",
]


class RepositoryConsistencyTests(unittest.TestCase):
    def test_single_canonical_skill_entrypoint(self) -> None:
        entries = [
            path.relative_to(ROOT)
            for path in ROOT.rglob("SKILL.md")
            if ".git" not in path.parts
        ]
        self.assertEqual(entries, [Path("SKILL.md")])

    def test_version_is_consistent(self) -> None:
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["version"], "0.2.0")
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn('version: "0.2.0"', skill)
        for name in READMES:
            self.assertIn("0.2.0", (ROOT / name).read_text(encoding="utf-8"), name)

    def test_language_switchers_link_every_readme(self) -> None:
        for name in READMES:
            text = (ROOT / name).read_text(encoding="utf-8")
            for target in READMES:
                if target == name:
                    continue
                self.assertIn(target, text, f"{name} does not link to {target}")

    def test_local_markdown_links_resolve(self) -> None:
        failures: list[str] = []
        for path in ROOT.rglob("*.md"):
            if ".git" in path.parts:
                continue
            text = path.read_text(encoding="utf-8")
            for target in re.findall(r"(?<!!)\[[^\]]*\]\(([^)]+)\)", text):
                target = target.split("#", 1)[0]
                if not target or re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
                    continue
                if not (path.parent / target).resolve().exists():
                    failures.append(f"{path.relative_to(ROOT)} -> {target}")
        self.assertEqual(failures, [])

    def test_public_files_have_no_machine_specific_home_path(self) -> None:
        pattern = re.compile(r"(?:/Users/[A-Za-z0-9._-]+/|/home/[A-Za-z0-9._-]+/|[A-Za-z]:\\\\Users\\\\)")
        failures: list[str] = []
        for path in ROOT.rglob("*"):
            if not path.is_file() or ".git" in path.parts:
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if pattern.search(text):
                failures.append(str(path.relative_to(ROOT)))
        self.assertEqual(failures, [])


if __name__ == "__main__":
    unittest.main()
