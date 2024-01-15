#!/usr/bin/env python3
'''
Let's execute multiple coroutines
at the same time with async
'''
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    ''' wait_n '''
    output: List[float] = []
    for idx in range(n):
        value = await wait_random(max_delay)
        output.append(value)
    return sorted(output)
