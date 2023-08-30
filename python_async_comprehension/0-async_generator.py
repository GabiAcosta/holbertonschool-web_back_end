#!/usr/bin/env python3
"""
This module provides an asynchronous generator that yields random floats.
"""
import asyncio
import random


async def async_generator() -> float:
    """
    Asynchronous generator that yields random floats with a delay of 1 second.
    """
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
