import asyncio


# Корутины(соппрограммы) - работают одновременно в одном потоке


async def print1():
    print(1)


async def print2():
    await asyncio.sleep(2)
    print(2)


async def print3():
    print(3)


# Главная корутина
async def main():
    task1 = asyncio.create_task(print1())
    task2 = asyncio.create_task(print2())
    task3 = asyncio.create_task(print3())

    await asyncio.gather(task1, task2, task3)  # Одновременный запуск 3х задач

    # tasks = [task1, task2, task3]
    # await asyncio.gather(*tasks)   - можно так


asyncio.run(main())
