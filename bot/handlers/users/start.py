from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from loader import dp
from data import db

from data.config import support_ids

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if not await db.user_exist(message.from_user.id) and message.from_user.id != support_ids:
        await db.add_user(message.from_user.id, message.from_user.full_name)
    elif message.from_user.id == support_ids:
        await message.answer(f'Привет админ', reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('Подтвердить')).add(KeyboardButton('/Список_пользователей')))
        # await message.answer(await db.get_user_list())
    else:
        await message.answer(f"Привет, {message.from_user.full_name}! Я Настя Ковалёва , та самая создательница Канала с аудиосказками «СКАЗКИ ДЕТКАМ»\n\n\n"
"Добро пожаловать на мой второй Волшебный ✨детский канал, где будут собраны длинные истории и не только ❤️\n\n"
"С помощью аудиосказок детки\n"
"✔️ Развивают свое воображения\n"
"✔️ Намного легче и быстрее за-сы-па-ют 😴\n"
'✔️ При этом хорошо развивается речь на слух, способствуя увеличению словарного запаса\n\n'
'А у мам есть прекрасная возможно отдохнуть. Ведь не всегда к вечеру есть силы читать деткам книжку.\n\n'
'Канал обновляется несколько раз в неделю. Категории историй от привычных нам советских сказок до современных интерпретаций.\n\n'
'Канал с ежемесячной подпиской (299₽ в месяц), пополняю 3 раза в неделю. Читаю сказки сериями( все главы по порядку до конца)\n\n'
'Если хотите присоединиться , то нужно перевести на карту Сбербанк или Тиньков 299₽ по номеру телефона 89118504608.\n'
'Далее нажмите на кнопку меню слева от линии ввода сообщения и выберите пункт: Отправить скрин оплаты, а дальше следуйте инструкции ☺️')
