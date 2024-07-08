#!/usr/bin/env python3
"""Tasks module"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronously waits for random delays and returns a sorted list of"""
    delays = await asyncio.gather(
        *(task_wait_random(max_delay) for _ in range(n))
    )
    sorted_delays = []
    while delays:
        min_delay = min(delays)
        sorted_delays.append(min_delay)
        delays.remove(min_delay)

    return sorted_delays
