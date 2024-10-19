import asyncio
from asyncio import Future


# Future представляет вычисления, которые либо уже выполняются,
# либо будут запланированы в будущем. Это специальный низкоуровневый ожидаемый объект,
# который представляет собой конечный результат асинхронной операции


import asyncio


# Определение асинхронной функции, которая возвращает Future
async def async_function():
    print("Начало выполнения асинхронной функции")

    # Создаем объект Future
    future = asyncio.Future()

    # Имитация асинхронной операции
    await asyncio.sleep(2)

    # Устанавливаем результат Future
    future.set_result("Результат асинхронной функции")

    return future  # Возвращаем объект Future


# Основная функция
async def main():
    print("Вызов асинхронной функции")
    # Вызываем асинхронную функцию и получаем объект Future
    future_result = await async_function()

    # Ожидание результата Future и вывод его
    result = await future_result
    print(f"Результат асинхронной функции: {result}")


# Запуск основной асинхронной программы
asyncio.run(main())
