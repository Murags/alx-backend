#!/usr/bin/env python3
"""pagination"""


def index_range(page: int, page_size: int) -> tuple:
    """returns a tuple of page start and end

    Args:
        page (int): page number
        page_size (int): page sizes

    Returns:
        tuple: of start and end of page
    """
    start = page_size * (page - 1)
    end = page_size * page

    return (start, end)
