#!/usr/bin/env python3
'''
Measure the runtime
'''
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    ''' measure_time '''
    # start recording time
    start_time: float = time.time()
    # run wait_n(n, max_delay)
    asyncio.run(wait_n(n, max_delay))
    # finish recording time
    end_time: float = time.time()
    # calc total_time
    total_time: float = (end_time - start_time) / n
    # return total_time
    return total_time
