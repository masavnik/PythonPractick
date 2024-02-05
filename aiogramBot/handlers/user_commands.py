import random

from aiogram import Router, Bot
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.types import Message
from aiogramBot.keyboards import reply

router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет, <b>{message.from_user.first_name}</b>', reply_markup=reply.main)


@router.message(Command(commands=['rn', 'random-number']))
async def get_random_number(message: Message, command: CommandObject):
    a, b = [int(n) for n in command.args.split('-')]  # [1-100]
    rnum = random.randint(a, b)
    await message.reply(f'Рандомное число: {rnum}')


@router.message(Command('test'))
async def test(message: Message, bot: Bot):
    await bot.send_message(message.chat.id, 'test')
