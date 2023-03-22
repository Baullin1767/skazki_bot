from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from data.config import support_ids

from data import db
import time

from keyboards.inline.support import support_keyboard, support_callback
from loader import dp, bot


@dp.message_handler(Command("send_foto"))
async def ask_support(message: types.Message):
    text = "Хотите отпривить скрин оплаты? Нажмите на кнопку под сообщением"
    keyboard = await support_keyboard(messages="one")
    await message.answer(text, reply_markup=keyboard)


@dp.callback_query_handler(support_callback.filter(messages="one"))
async def send_to_support(call: types.CallbackQuery, state: FSMContext, callback_data: dict):
    await call.answer()
    user_id = int(callback_data.get("user_id"))
    if call.from_user.id == support_ids:
        await call.message.answer("Пришлите ваше сообщение, которым вы хотите поделиться")
    else:
        await call.message.answer("Пришлите скрин оплаты")
    await state.set_state("wait_for_support_message")
    await state.update_data(second_id=user_id)



@dp.message_handler(state="wait_for_support_message", content_types=types.ContentTypes.ANY)
async def get_support_message(message: types.Message, state: FSMContext):
    data = await state.get_data()
    second_id = data.get("second_id")

    await bot.send_message(second_id,
                           f"Вам письмо!")
    keyboard = await support_keyboard(messages="one", user_id=message.from_user.id)
    
    if message.from_user.id == support_ids:
        
        time_sub = int(time.time()) + db.days_to_seconds(30)
        await db.set_time_sub(second_id, time_sub)
        await bot.unban_chat_member(-111111111111, second_id, only_if_banned=True)
        invite_link = await bot.create_chat_invite_link(-1111111111111, expire_date=time_sub, member_limit=1)
        await bot.send_message(second_id, f"Вы преобрели подписку на месяц. Воспользуйтесь ссылкой, чтобы снова подключиться к каналу:\n{invite_link['invite_link']}")
    else:
        await message.copy_to(second_id, reply_markup=keyboard)
        await message.answer("Вы отправили скрин. Подождите пока администратор подтвердит подписку!")



    await state.reset_state()
