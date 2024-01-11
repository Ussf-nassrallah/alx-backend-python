#!/usr/bin/env python3
''' More involved type annotations '''
from typing import Any, Mapping, Union, TypeVar


dt = Union[TypeVar('T'), None]
rt = Union[Any, TypeVar('T')]


def safely_get_value(dct: Mapping, key: Any, default: dt = None) -> rt:
    ''' function: safely_get_value '''
    if key in dct:
        return dct[key]
    else:
        return default
