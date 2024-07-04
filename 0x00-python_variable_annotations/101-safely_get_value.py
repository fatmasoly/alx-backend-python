#!/usr/bin/env python3
"""Annotate the below function's parameters and return values with the"""
from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')
ret_t = Union[Any, T]
def_t = Optional[T]


def safely_get_value(dct: Mapping, key: Any, default: def_t = None) -> ret_t:
    """Return the value of a key in a dictionary or None if not found."""
    if key in dct:
        return dct[key]
    else:
        return default
