#!/usr/bin/env python3
"""
To Key-Value Tuple Function

This module defines a function that converts a key and a value into a
tuple where the value is squared.

"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Convert a key and a value into a tuple with the value squared."""
    tup = (k, v * v)
    return tup
