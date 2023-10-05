#!/usr/bin/env python3
"""module that define safe_first_element function
"""
from typing import TypeVar, Dict, Any, Union, Mapping


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[TypeVar("T"), None] = None) -> Union[
                         Any, TypeVar("T")]:
    """get first value of dictionary or None

    Args:
        dct (Mapping): dictionary of key & values
        key (Any): key to get its corresponding value from dct
        default (Union[~T, None]): default value to be returned
        if the key not found in dct

    Returns:
        Union[Any, ~T]: return the value corresponding
        to input key or return None
    """
    if key in dct:
        return dct[key]
    else:
        return default
