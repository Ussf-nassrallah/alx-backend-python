#!/usr/bin/env python3
'''
4. Tasks
'''
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    ''' task_wait_n '''
    output: List[float] = []
    for idx in range(n):
        value = await task_wait_random(max_delay)
        output.append(value)
    return sorted(output)
