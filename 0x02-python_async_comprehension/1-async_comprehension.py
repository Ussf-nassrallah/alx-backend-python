#!/usr/bin/env python3
'''
1. Async Comprehensions
'''

from importlib import import_module as using
from typing import List
async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    async_comprehension()
    '''

    return [num async for num in async_generator()]
