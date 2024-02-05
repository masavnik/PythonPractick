import asyncio
import random

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.types import Message

bot = Bot('6352473081:AAGlclRiCSS0SuieG241cht09MrNIk-Udlw', parse_mode='HTML')
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет, <b>{message.from_user.first_name}</b>')


@dp.message(Command(commands=['rn', 'random-number']))
async def get_random_number(message: Message, command: CommandObject):
    a, b = [int(n) for n in command.args.split('-')]  # [1-100]
    rnum = random.randint(a, b)
    await message.reply(f'Рандомное число: {rnum}')


@dp.message(F.text == 'play')
async def play_games(message: Message):
    x = await message.answer_dice(DiceEmoji.DICE)


@dp.message()
async def echo(message: Message):
    await message.answer('Я тебя не понимаю')


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())