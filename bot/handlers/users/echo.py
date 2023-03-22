from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp


# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(f"Нажмите на кнопку меню слева от линии ввода сообщения и выберите пункт: Отправить скрин оплаты, а дальше следуйте инструкции ☺️")
