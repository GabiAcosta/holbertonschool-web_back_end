#!/usr/bin/env python3
"""
This module provides an asynchronous function for waiting on multiple
random delays.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronously waits for 'n' random delays of up to 'max_delay' each."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
