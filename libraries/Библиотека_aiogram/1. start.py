import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6352473081:AAGlclRiCSS0SuieG241cht09MrNIk-Udlw")
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!")


@dp.message(Command("answer"))
async def cmd_answer(message: types.Message):
    await message.answer("Это простой ответ")


@dp.message(Command("reply"))
async def cmd_reply(message: types.Message):
    await message.reply('Это ответ с "ответом"')


# @dp.message(Command("dice"))
# async def cmd_dice(message: types.Message):
#     await message.answer_dice(emoji="🎲")

@dp.message(Command("dice"))
async def cmd_dice(message: types.Message, bot: Bot):
    chat = message.chat.id
    await message.answer(f'{chat}')
    await bot.send_dice(6673085582, emoji=DiceEmoji.DICE)


# Запуск процесса поллинга новых апдейтов6352473081
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
