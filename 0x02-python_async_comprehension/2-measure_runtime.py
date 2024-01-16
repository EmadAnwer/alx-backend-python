#!/usr/bin/env python3
"""
    2-measure_runtime.py
"""
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """measure_runtime"""
    start = time.perf_counter()
    await async_comprehension()
    end = time.perf_counter()

    return end - start
