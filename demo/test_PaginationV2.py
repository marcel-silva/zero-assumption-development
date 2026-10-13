"""Shared deterministic contract tests; not an AI-methodology benchmark."""
from collections.abc import Callable
import unittest
from typing import Any


def build_suite(paginate: Callable[..., list[Any]]) -> unittest.TestSuite:
    """Use the same tests for the intentionally broken and reference versions."""

    class PaginationTests(unittest.TestCase):
        def test_first_page(self) -> None:
            self.assertEqual(paginate(list(range(10)), 1, 3), [0, 1, 2])

        def test_middle_page(self) -> None:
            self.assertEqual(paginate(list(range(10)), 2, 3), [3, 4, 5])

        def test_final_partial_page(self) -> None:
            self.assertEqual(paginate(list(range(10)), 4, 3), [9])

        def test_beyond_end(self) -> None:
            self.assertEqual(paginate([1, 2], 99, 3), [])

        def test_empty_items(self) -> None:
            self.assertEqual(paginate([], 1, 3), [])

        def test_page_size_one(self) -> None:
            self.assertEqual(paginate([10, 20, 30], 1, 1), [10])

        def test_tuple_input(self) -> None:
            self.assertEqual(paginate(("a", "b", "c"), 1, 2), ["a", "b"])

        def test_page_zero_raises(self) -> None:
            with self.assertRaises(ValueError):
                paginate([1, 2], 0, 2)

        def test_negative_page_raises(self) -> None:
            with self.assertRaises(ValueError):
                paginate([1, 2], -1, 2)

        def test_zero_size_raises(self) -> None:
            with self.assertRaises(ValueError):
                paginate([1, 2], 1, 0)

        def test_noninteger_page_raises(self) -> None:
            with self.assertRaises(TypeError):
                paginate([1, 2], 1.5, 2)

        def test_boolean_page_raises(self) -> None:
            with self.assertRaises(TypeError):
                paginate([1, 2], True, 2)

        def test_noninteger_size_raises(self) -> None:
            with self.assertRaises(TypeError):
                paginate([1, 2], 1, "2")

        def test_boolean_size_raises(self) -> None:
            with self.assertRaises(TypeError):
                paginate([1, 2], 1, True)

        def test_does_not_mutate_input(self) -> None:
            items = [1, 2, 3, 4]
            original = items.copy()
            result = paginate(items, 1, 2)
            result.append(999)
            self.assertEqual(items, original)
            self.assertIsNot(result, items)

        def test_large_page_size(self) -> None:
            self.assertEqual(paginate([1, 2, 3], 1, 100), [1, 2, 3])

    return unittest.defaultTestLoader.loadTestsFromTestCase(PaginationTests)
