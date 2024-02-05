import asyncio
from aiogram import Bot, Dispatcher

from aiogramBot.handlers import bot_messages, user_commands, questionaire
from aiogramBot.callback import pagination


async def main():
    bot = Bot('6352473081:AAGlclRiCSS0SuieG241cht09MrNIk-Udlw', parse_mode='HTML')
    dp = Dispatcher()
    dp.include_routers(
        user_commands.router,
        pagination.router,
        questionaire.router,
        bot_messages.router
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
