#!/usr/bin/env python3
from typing import List
""" module that define sum_list function
"""


def sum_list(input_list: List[float]) -> float:
    """sum all the number in the float list and
    return the summision

    Args:
        input_list (list[float]): list of float numbers
        to get the total for them

    Returns:
        float: sum of all numbers in input list
    """
    return sum(input_list)
