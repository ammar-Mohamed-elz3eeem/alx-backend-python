#!/usr/bin/env python3
from typing import Callable
""" module that define sum_mixed_list function
"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """multiplier function that returns another function
    that accepts float also which will return
    the multiplication of both floats

    Args:
        multiplier (float): parameter to be multiplied in the callback

    Returns:
        Callable[[float], float]: the function in
        which we will make the multiplication
    """
    def fun(a: float) -> float:
        return a * multiplier
    return fun
