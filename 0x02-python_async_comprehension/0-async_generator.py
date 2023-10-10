#!/usr/bin/env python3
"""great async generator for python
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """generator that generates iterable of 10
    random numbers asyncrounously

    Yields:
        Generator[float, None, None]: return iterable of 10 random numbers
    """
    for i in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
