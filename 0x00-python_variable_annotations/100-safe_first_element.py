#!/usr/bin/env python3
"""module that define safe_first_element function
"""
from typing import Iterable, Sequence, Tuple, List, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """determine if list is empty or not
    and if not empty we return the first element in it
    otherwise return None

    Args:
        lst (Sequence[Any]): list of any types

    Returns:
        Union[Any, None]: return first element of list or None
    """
    if lst:
        return lst[0]
    else:
        return None
