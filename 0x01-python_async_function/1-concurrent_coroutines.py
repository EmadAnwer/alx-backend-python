#!/usr/bin/env python3
"""
    1-concurrent_coroutines.py
"""
import asyncio

from typing import List, Callable


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n
    @n: times to call wait_random
    @max_delay: max delay of wait_random
    Return: list of all delays
    """

    delays: List[asyncio.Future[float]] = []
    for _ in range(n):
        delays.append(wait_random(max_delay))

    result: List[float] = []
    for delay in asyncio.as_completed(delays):
        result.append(await delay)
    return result
