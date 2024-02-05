from aiogram import Router, F
from aiogram.types import Message
from aiogramBot.keyboards import reply, inline, builders, fabrics
from aiogramBot.data.subloader import get_json

router = Router()


@router.message(F.text.lower().in_(['хай', 'хелоу', 'привет']))
async def greetings(message: Message):
    await message.reply('Привееееет!')


@router.message()  # Ловит все сообщения. ее вниз
async def echo(message: Message):
    msg = message.text.lower()
    smiles = await get_json('smiles.json')

    if msg == 'ссылки':
        await message.answer('Вот ваши ссылки', reply_markup=inline.links_kb)
    elif msg == 'спец кнопки':
        await message.answer('Спец. кнопки', reply_markup=reply.spec)
    elif msg == 'колькулятор':
        await message.answer('Выведите выражение', reply_markup=builders.calc())
    elif msg == 'смайлики':
        await message.answer(f'{smiles[0][0]} <b>{smiles[0][1]}</b>', reply_markup=fabrics.paginator())
