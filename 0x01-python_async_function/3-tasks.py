#!/usr/bin/env python3
"""task_wait_random functionality module
"""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """create task from async function

    Args:
        max_delay (int): max number for delay

    Returns:
        asyncio.Task: return instance of asyncio Task object
    """
    return asyncio.create_task(wait_random(max_delay))
