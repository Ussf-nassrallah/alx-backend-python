#!/usr/bin/env python3
''' Complex types - list of floats '''

from typing import List


def sum_list(input_list: List[float]) -> float:
    ''' sum_list should return a float '''
    result: float = float(sum(input_list))
    return result
