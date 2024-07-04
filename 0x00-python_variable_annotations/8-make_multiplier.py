#!/usr/bin/env python3
"""Type-annotated function make_multiplier that takes a float multiplier as"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Type-annotated function make_multiplier that returns a function """
    def multi_float(n: float) -> float:
        """Type-annotated function make_multiplier that takes a float"""
        return n * multiplier

    return multi_float
