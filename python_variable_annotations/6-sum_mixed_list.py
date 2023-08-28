#!/usr/bin/env python3
"""
Sum Mixed List Function

This module defines a function that calculates the sum of a list containing
a mix of integers and floating-point numbers.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list containing a mix of integers
    and floating-point numbers.
    """
    sum = 0
    for num in mxd_lst:
        sum += num
    return sum
