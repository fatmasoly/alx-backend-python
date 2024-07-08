#!/usr/bin/env python3


import asyncio
import random


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> float:
    """Wait for a random delay between 0 and max_delay n times"""
    delays = [wait_random(max_delay) for _ in range(n)]
    all_delays = await asyncio.gather(*delays)
    return all_delays
