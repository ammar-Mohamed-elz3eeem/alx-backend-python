#!/usr/bin/env python3
"""wait_random functionality module
"""
import asyncio
import random


async def wait_random(max_delay = 0):
    random_num = random.random() * 15
    await asyncio.sleep(random_num)
    return random_num
