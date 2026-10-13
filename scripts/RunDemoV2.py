#!/usr/bin/env python3
"""Check an intentionally defective fixture and its reference correction.

No AI provider is contacted. No comparison of ZAD effectiveness is performed.
Exit zero only when the starter is detected as defective and the reference passes.
"""
from __future__ import annotations

import argparse
import importlib.util
import io
from pathlib import Path
import sys
from types import ModuleType
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load_module(path: Path, name: str) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--verbose", action="store_true", help="Show all test output.")
    parser.add_argument(
        "--implementation", type=Path,
        help="Run the contract tests only against a chosen module exposing paginate.")
    args = parser.parse_args()
    tests = load_module(ROOT / "demo/test_PaginationV2.py", "zad_demo_tests")
    if args.implementation is not None:
        path = args.implementation.expanduser().resolve()
        if not path.is_file():
            raise FileNotFoundError(f"Implementation file not found: {path}")
        implementation = load_module(path, "zad_candidate")
        result = unittest.TextTestRunner(verbosity=2 if args.verbose else 1).run(
            tests.build_suite(implementation.paginate))
        passed = result.testsRun > 0 and result.wasSuccessful() and not result.skipped
        print(f"Candidate: {result.testsRun} tests; {len(result.failures)} failures; "
              f"{len(result.errors)} errors; {len(result.skipped)} skipped")
        print("This grades the tested code contract, not ZAD effectiveness.")
        return 0 if passed else 1

    results: dict[str, unittest.TestResult] = {}
    details: dict[str, str] = {}
    for label, file_name in (
        ("starter", "PaginationStarterV2.py"),
        ("reference", "PaginationReferenceV2.py"),
    ):
        implementation = load_module(ROOT / "demo" / file_name, f"zad_{label}")
        stream = io.StringIO()
        suite = tests.build_suite(implementation.paginate)
        result = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
        results[label] = result
        details[label] = stream.getvalue()
        print(f"{label}: {result.testsRun} tests; {len(result.failures)} failures; "
              f"{len(result.errors)} errors; {len(result.skipped)} skipped")
        if args.verbose:
            print(details[label])

    starter, reference = results["starter"], results["reference"]
    valid = (
        starter.testsRun == reference.testsRun and starter.testsRun > 0
        and len(starter.failures) > 0 and not starter.errors and not starter.skipped
        and reference.wasSuccessful() and not reference.skipped
    )
    if not valid:
        if not args.verbose:
            print("\n".join(details.values()), file=sys.stderr)
        print("FAIL: fixture expectations were not met.", file=sys.stderr)
        return 1
    print("PASS: the defect is detected and the reference satisfies the tested contract.")
    print("This is a fixture check, not evidence that ZAD improves AI performance.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ImportError, RuntimeError, AttributeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc
