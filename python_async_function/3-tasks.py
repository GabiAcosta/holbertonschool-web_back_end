#!/usr/bin/env python3
"""
This module provides a function that returns an asyncio.Task created with
the function wait_random
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """This function returns an asyncio.Task"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
