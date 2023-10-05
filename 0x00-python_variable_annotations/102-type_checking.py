#!/usr/bin/env python3
"""module that define safe_first_element function
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """get every item in list zoomed in

    Args:
        lst (Tuple): tuple list
        factor (int, optional): zoom factor. Defaults to 2.

    Returns:
        List: zoomed in for every element in tuple
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
