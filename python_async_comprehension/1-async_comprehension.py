#!/usr/bin/env python3
"""
This module provides an asynchronous comprehension that generates a list
of random floats.
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Asynchronous comprehension that generates a list of random floats."""
    numbers = [num async for num in async_generator()]
    return numbers
