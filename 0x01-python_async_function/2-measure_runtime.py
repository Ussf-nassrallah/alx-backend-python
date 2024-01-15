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
    start = time.time()
    # run wait_n(n, max_delay)
    asyncio.run(wait_n(n, max_delay))
    # return total_time / n
    return (time.time() - start) / n
