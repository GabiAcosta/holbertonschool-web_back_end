#!/usr/bin/env python3
"""
This module provides an asynchronous function for waiting on multiple
random delays.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronously waits for 'n' random delays of up to 'max_delay' each."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
