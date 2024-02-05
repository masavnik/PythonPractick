import asyncio


async def count(counter):
    print(f'Количество записей в цикле {len(counter)}')

    while True:
        await asyncio.sleep(1 / 1000)
        counter.append(1)


async def print_every1(counter):
    while True:
        await asyncio.sleep(1)
        print(f'- 1 секунда прошла.'
              f'Количество записей в списке: {len(counter)}')


async def print_every5():
    while True:
        await asyncio.sleep(5)
        print(f'---- 5 секунда прошла.')


async def print_every10():
    while True:
        await asyncio.sleep(10)
        print(f'-------- 10 секунда прошла.')


async def main():
    counter = list()

    task = [count(counter),
            print_every1(counter),
            print_every5(),
            print_every10()
            ]

    await asyncio.gather(*task)


asyncio.run(main())
