import asyncio
import aiohttp
import requests
from bs4 import BeautifulSoup as bs
import os
import time
import random
from time import perf_counter


# Корутина
# async def a_square(x):
#     print(f'Asynchronously squaring {x}!')
#     return x ** 2


async def delayed_print(text, time=1):
    await asyncio.sleep(time)
    print(text)


async def main_coro():
    # python >= 3.7
    task = [
        asyncio.create_task(delayed_print("I'm printed second!", 2)),
        asyncio.create_task(delayed_print("I'm printed first!", 3)),
        asyncio.create_task(delayed_print("I'm printed last!1231231", 1))
    ]
    # python >= 3.3
    await asyncio.gather(*task,
                         delayed_print("I'm printed last!", 3)
                         )

    # python >= 3.7
asyncio.run(main_coro())