from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

links_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='YouTube', url='https://www.avito.ru/'),
            InlineKeyboardButton(text='Telegram', url='tg://resolve?domain=masavnik')
        ]
    ]
)
