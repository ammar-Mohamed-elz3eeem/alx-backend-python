#!/usr/bin/env python3
from typing import Tuple, Dict, Union
""" module that define sum_mixed_list function
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """convert k & v to a tuple

    Args:
        k (str): key
        v (Union[int, float]): value associated with the key

    Returns:
        Tuple[str, float]: tuble that represnts k & v
        associated with it
    """
    return tuple([k, v**2])
