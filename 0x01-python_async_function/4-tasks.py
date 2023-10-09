#!/usr/bin/env python3
"""task_wait_n functionality module
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Asyncronsly make random numbers list and return numbers

    Args:
        n: number of random numbers to make
        max_delay (int): max number that the programm
        will have to wait. Defaults to 0.

    Returns:
        List<float>: numbers that has been generated
    """
    delays = []
    all_delays = []
    for i in range(0, n):
        delays.append(task_wait_random(max_delay))
    for delay in asyncio.as_completed(delays):
        smallest = await delay
        all_delays.append(smallest)
    return all_delays
