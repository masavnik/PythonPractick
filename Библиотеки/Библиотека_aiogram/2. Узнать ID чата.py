import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6352473081:AAGlclRiCSS0SuieG241cht09MrNIk-Udlw")
# Диспетчер
dp = Dispatcher()

ID_GROUP = '-4003665636'

@dp.message(Command('help'))
async def id_user(message: types.Message):
    # await message.answer(f'{message.chat.id}')
    # await bot.send_message(chat_id=message.from_user.id, text='Привет') # Индитификаатор пользователя
    # await bot.send_message(chat_id=message.from_user.id, text='Привет') # Индитификатор группы
    # await message.answer(f'{message.from_user.id}') # ID пользователя
    # await message.answer(f'{message.from_user.first_name}')  # Имя пользователя
    # await bot.send_message(message.from_user.id, f'{message.chat.id}')  # Все о группе
    await bot.forward_message(ID_GROUP, message.from_user.id, message.message_id) # Отправить комануду help в группу



async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
