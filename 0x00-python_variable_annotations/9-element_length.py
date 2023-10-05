#!/usr/bin/env python3
"""module that define sum_mixed_list function
"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """determine the length of every list in the multidimensional lst

    Args:
        lst (Iterable[Sequence]): multidimensional list

    Returns:
        List[Tuple[Sequence, int]]: list of tuples that contains
        every list on the multidimensional list
        and the length of that list
    """
    return [(i, len(i)) for i in lst]
