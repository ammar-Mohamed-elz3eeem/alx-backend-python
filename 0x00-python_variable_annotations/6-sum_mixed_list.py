#!/usr/bin/env python3
""" module that define sum_mixed_list function
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum all the number in the input list and
    return the summision

    Args:
        mxd_lst (list[float | int]): list of mixed numbers
        float and integers to get the total for them

    Returns:
        float: sum of all numbers in mixed list
    """
    return sum(mxd_lst)
