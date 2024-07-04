#!/usr/bin/env python3
"""Type-annotated function to_kv that takes a string k and an int OR float v"""

from typing import Union


def to_kv(k: str, v: Union[int, float]) -> float:
    """Return a tuple containing k and the square of v."""
    return (k, v ** 2)
