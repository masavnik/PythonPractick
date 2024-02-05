from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    KeyboardButtonPollType,
    ReplyKeyboardRemove
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Смайлики'),
            KeyboardButton(text='Ссылки')
        ],
        [
            KeyboardButton(text='Колькулятор'),
            KeyboardButton(text='Спец кнопки')
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выберите действие из меню',
    selective=True
)

spec = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Отправить гео', request_location=True),
            KeyboardButton(text='Отправить контакт', request_contact=True),
            KeyboardButton(text='Отправить викторину', request_poll=KeyboardButtonPollType(type='regular'))
        ],
        [
            KeyboardButton(text='Назад')
        ]
    ],
    resize_keyboard=True
)


rmk = ReplyKeyboardRemove()