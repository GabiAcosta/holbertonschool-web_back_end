#!/usr/bin/env python3
"""
Async Wait Random Function

This module defines an asynchronous function that generates a random delay and
then asynchronously waits for that delay using asyncio.sleep().
The generated delay is returned as the output.
"""
import asyncio
import random


async def wait_random(max_delay=10):
    """Asynchronously waits for a random delay."""
    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
