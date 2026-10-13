#!/usr/bin/env python3
"""Validate local ZAD package structure, Markdown targets, and Python syntax.

Uses the Python standard library only. Does not execute publishing scripts,
contact services, or verify live URLs. This is not a semantic ZAD compliance test.
"""
from __future__ import annotations

import argparse
import ast
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
PENDING_READMES = {"README.md", "demo/README.md"}
REQUIRED = (
    "README.md", "MANIFESTO.md", "ZAD.md", "AGENTS.md", "CLAUDE.md", "LICENSE",
    "VERSION", "CONTRIBUTING.md", "CHANGELOG.md", "ROADMAP.md",
    "docs/GETTING_STARTED.md", "docs/TOOL_INTEGRATIONS.md", "docs/SOURCES.md",
    "docs/VALIDATION.md", "examples/PROMPT_LIBRARY.md", "examples/WORKED_EXAMPLES.md",
    "evaluation/PROTOCOL.md", "templates/TASK.md", "templates/CASE_STUDY.md",
    "demo/README.md", "demo/PaginationStarterV2.py", "demo/PaginationReferenceV2.py",
    "demo/test_PaginationV2.py", "scripts/RunDemoV2.py",
    ".github/ISSUE_TEMPLATE/experience_report.md",
    ".github/ISSUE_TEMPLATE/methodology_proposal.md", ".github/PULL_REQUEST_TEMPLATE.md",
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--allow-pending-readmes", action="store_true",
        help="Validate the toolkit without requiring the withheld README files. "
             "This does not certify README publication readiness.")
    args = parser.parse_args()
    errors: list[str] = []
    required = tuple(p for p in REQUIRED
                     if not (args.allow_pending_readmes and p in PENDING_READMES))
    for relative in required:
        path = ROOT / relative
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"Required file missing or empty: {relative}")
    if not args.allow_pending_readmes:
        readme = ROOT / "README.md"
        if readme.is_file() and "Zero-Assumption Development" not in readme.read_text(encoding="utf-8"):
            errors.append("README.md is still a placeholder; a reviewed ZAD README is required.")
    version_file = ROOT / "VERSION"
    if version_file.exists() and version_file.read_text(encoding="utf-8").strip() != "1.0.0":
        errors.append("VERSION does not match this initial 1.0.0 package.")

    markdown_files = sorted(ROOT.rglob("*.md"))
    local_targets = 0
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        # Match standard inline Markdown links, not bare URLs or reference links.
        for target in re.findall(r"\[[^\]\n]+\]\(([^)]+)\)", text):
            target = target.strip().split(' "', 1)[0]
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            relative = unquote(parsed.path)
            resolved = (path.parent / relative).resolve()
            local_targets += 1
            if not resolved.is_relative_to(ROOT):
                errors.append(f"Link escapes repository: {path.relative_to(ROOT)} -> {target}")
            elif not resolved.exists():
                errors.append(f"Broken local link: {path.relative_to(ROOT)} -> {target}")
        if re.search(r"turn\d+(?:search|view|file)\d+", text):
            errors.append(f"Unportable internal citation marker: {path.relative_to(ROOT)}")

    python_files = sorted(ROOT.rglob("*.py"))
    for path in python_files:
        if not re.search(r"V\d+\.py$", path.name):
            errors.append(f"Code filename is missing its version suffix: {path.name}")
        try:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except SyntaxError as exc:
            errors.append(f"Python syntax error: {path.relative_to(ROOT)}: {exc}")

    question_examples = 0
    for relative in ("docs/GETTING_STARTED.md", "examples/PROMPT_LIBRARY.md", "examples/WORKED_EXAMPLES.md"):
        path = ROOT / relative
        if not path.is_file():
            continue
        for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if line.startswith("> "):
                question_examples += 1
                if not line.rstrip().endswith("?"):
                    errors.append(f"Prompt example does not end with ?: {relative}:{line_no}")

    for path in sorted((ROOT / ".github/ISSUE_TEMPLATE").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n") or "\n---\n" not in text[4:]:
            errors.append(f"Issue-template front matter is incomplete: {path.name}")
        elif not re.search(r"^name: .+", text, re.MULTILINE) or not re.search(r"^about: .+", text, re.MULTILINE):
            errors.append(f"Issue-template metadata missing: {path.name}")

    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print(f"PASS: {len(required)} required files; {len(markdown_files)} Markdown files; "
          f"{local_targets} local link targets; {len(python_files)} Python files; "
          f"{question_examples} question examples.")
    if args.allow_pending_readmes:
        print("NOTICE: README publication readiness was not checked; README files remain pending review.")
    print("Checks cover local structure and syntax, not AI effectiveness or live integrations.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, UnicodeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
