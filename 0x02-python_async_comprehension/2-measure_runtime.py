#!/usr/bin/env python3
"""measure_runtime for python
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """run 4 tasks at a time asyncrounously and get
    the time for all of them to finish

    return the total time the async operations took to run
    """
    prev_time = time.perf_counter()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    return time.perf_counter() - prev_time
