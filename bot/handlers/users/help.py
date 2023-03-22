from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            '/support - Отправить скрин оплаты',
            '/support_call - Пообщаться с техподдержкой',
            "/user_base - База пользователей",
            '/help - Получить справку')
    
    await message.answer("\n".join(text))
