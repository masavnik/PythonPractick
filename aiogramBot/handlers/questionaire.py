from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from aiogramBot.utils.states import Form
from aiogramBot.keyboards.builders import profile
from aiogramBot.keyboards.reply import rmk

router = Router()


@router.message(Command('profile'))
async def file_profile(message: Message, state: FSMContext):
    await state.set_state(Form.name)
    await message.answer(
        'Давай начнем, введи свое имя',
        reply_markup=profile(message.from_user.first_name)
    )


@router.message(Form.name)
async def form_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Form.age)
    await message.answer('Отлично, теперь введи свой возраст', reply_markup=rmk)


@router.message(Form.age)
async def form_age(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(age=message.text)
        await state.set_state(Form.sex)
        await message.answer('Теперь давай определимся с полом', reply_markup=profile(['парень', 'девушка']))
    else:
        await message.answer('Введи число еще раз')


@router.message(Form.sex, F.text.casefold().in_(['парень', 'девушка']))
async def form_sex(message: Message, state: FSMContext):
    await state.update_data(sex=message.text)
    await state.set_state(Form.about)
    await message.answer('Расскажи о себе', reply_markup=rmk)


@router.message(Form.sex)
async def incorrct(message: Message, state: FSMContext):
    if len(message.text) < 5:
        await message.answer('Введи что-нибудь поинтереснее')
    else:
        await state.update_data(about=message.text)
        await state.set_state(Form.photo)
        await message.answer('Отправь свое фото')


@router.message(Form.photo, F.photo)
async def form_photo(message: Message, state: FSMContext):
    photo_file_id = message.photo[-1].file_id
    data = await state.get_data()
    await state.clear()

    formates_text = []

    [
        formates_text.append(f'{key}: {value}')
        for key, value in data.items()
    ]

    await message.answer_photo(
        photo_file_id,
        '\n'.join(formates_text)
    )


@router.message(Form.photo, ~F.photo)
async def incorrect_form_photo(message: Message, state: FSMContext):
    await message.answer('Отправь фото')


