#!/usr/bin/env python3
''' Complex types - mixed list '''

from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' sum_mixed_list should return a float '''
    result: float = float(sum(mxd_lst))
    return result
