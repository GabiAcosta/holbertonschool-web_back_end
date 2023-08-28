#!/usr/bin/env python3
"""
In this task we started with this function:

def element_length(lst):
    return [(i, len(i)) for i in lst]

We had to annotate the function's parameters and return values with
the appropriate types
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples containing sequences and their respective lengths.
    """
    return [(i, len(i)) for i in lst]
