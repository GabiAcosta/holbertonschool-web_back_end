#!/usr/bin/env python3
"""
Sum List Function

This module defines a function that calculates the sum of a list of
floating-point numbers.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Calculate the sum of a list of floating-point numbers."""
    sum = 0
    for num in input_list:
        sum += num
    return sum
