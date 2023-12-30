#!/usr/bin/env python3
"""
0-simple_helper_function.py - Provides one function:
    index_range(page, page_size)
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start and end indices corresponding to the
     range of indexes to return in a list for those particular
     pagination parameters

    Args:
        page (int): page number to be requested (starts from 1)
        page_size (int): the element count in a page

    Returns:
        Tuple[int, int]: the start (inclusive) and end (not
         inclusive) indices
    """
    return ((page - 1) * page_size, page * page_size)


if __name__ == "__main__":
    res = index_range(1, 7)
    print(type(res))
    print(res)

    res = index_range(page=3, page_size=15)
    print(type(res))
    print(res)
