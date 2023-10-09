#!/usr/bin/env python3
"""wait_random functionality module
"""
import asyncio
import random


async def wait_random(max_delay: int = 0) -> float:
    """Asyncronsly make random number and return it

    Args:
        max_delay (int): max number that the programm
        will have to wait. Defaults to 0.

    Returns:
        float: random number that has been generated
    """
    random_num = random.random() * max_delay
    await asyncio.sleep(random_num)
    return random_num
