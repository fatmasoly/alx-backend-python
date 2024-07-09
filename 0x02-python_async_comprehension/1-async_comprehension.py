#!/usr/bin/env python3
"""Async comprehension"""

import asyncio
import random
from typing import Generator, List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random numbers by async comprehensing over async_generator"""
    return [i async for i in async_generator()]
