#!/usr/bin/env python3
"""
This script defines a function for calculating a range of indices for
paginating data.
"""


def index_range(page, page_size):
    """
    Calculate the range of indices to retrieve a specific page of data.
    """
    return ((page - 1) * page_size, page_size * page)
