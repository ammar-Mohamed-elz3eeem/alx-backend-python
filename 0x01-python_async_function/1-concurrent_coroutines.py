#!/usr/bin/env python3
"""wait_random functionality module
"""
import asyncio
import random
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int = 0) -> List[float]:
    """Asyncronsly make random numbers list and return it

    Args:
        n: number of random numbers to make
        max_delay (int): max number that the programm
        will have to wait. Defaults to 0.

    Returns:
        List<float>: random numbers that has been generated
    """
    delays: List[float] = []
    all_delays: List[float] = []
    for i in range (0, n):
        delays.append(wait_random(max_delay))
    for delay in asyncio.as_completed(delays):
        fifo = await delay
        all_delays.append(fifo)
    return all_delays
