#!/usr/bin/env python3
"""
  floor - func that return the floor of the float
  @n: float
  return: the floor of the float (int)
"""
import math


def floor(n: float) -> int:
    result: int = int(math.floor(n))
    return result
