#!/usr/bin/env python3
'''
2. Run time for four parallel comprehensions
'''

import time
import asyncio
from importlib import import_module as using
async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' measure_runtime() '''
    start = time.time()
    await asyncio.gather(*(async_comprehension() for idx in range(4)))
    end = time.time()
    return end - start
