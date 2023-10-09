#!/usr/bin/env python3
"""wait_random functionality module
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 0) -> float:
    current = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (time.perf_counter() - current) / n
