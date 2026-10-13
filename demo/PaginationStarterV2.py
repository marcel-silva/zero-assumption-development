"""Intentionally defective pagination fixture for the ZAD demonstration.

Contract: one-based pages; positive integer page and page_size; return a new
list without mutating the input. Out-of-range pages return an empty list.
"""

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def paginate(items: Sequence[T], page: int, page_size: int) -> list[T]:
    """Return the requested page according to the documented contract."""
    if isinstance(page, bool) or not isinstance(page, int):
        raise TypeError("page must be an integer, not a boolean")
    if isinstance(page_size, bool) or not isinstance(page_size, int):
        raise TypeError("page_size must be an integer, not a boolean")
    if page < 1:
        raise ValueError("page must be at least 1")
    if page_size < 1:
        raise ValueError("page_size must be at least 1")

    start = page * page_size  # Intentional off-by-one-page defect.
    return list(items[start:start + page_size])
