#!/usr/bin/env python3
"""measure_time functionality module
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 0) -> float:
    """measure time taking to excute one of async code

    Args:
        n (int): number of operations
        max_delay (int, optional): max num of seconds to wait
        for each operation. Defaults to 0.

    Returns:
        float: elapsed time per operation
    """
    current = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (time.perf_counter() - current) / n
