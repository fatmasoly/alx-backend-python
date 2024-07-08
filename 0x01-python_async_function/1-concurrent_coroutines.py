#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""

from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Let's execute multiple coroutines at the same time with async"""

    delays_list: List[float] = []

    for idx in range(n):
        delay: float = await wait_random(max_delay)

        delays_list.append(delay)

    return sorted(delays_list)
