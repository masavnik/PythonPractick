import asyncio

# Цикл событий (event loop) — это программная конструкция, которая ожидает возникновения событий, а
# затем передает их обработчику событий.
#
# Событием может быть клик пользователя на кнопку интерфейса пользователя,
# запуск процесса загрузки файла или получение ответа от стороннего сервера.


async def do_something_important():
    await asyncio.sleep(2)
    l = 20
    print(l)

if __name__ == "__main__":
  asyncio.run(do_something_important())