from aiogram import types
from aiogram.dispatcher import FSMContext

from data import db
import csv

from loader import dp, bot

async def set_list_in_csv(list_data, name_file):
    with open(name_file, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["user_id", "user_name", "time_sub"], quoting=csv.QUOTE_ALL)
        writer.writeheader()  # Записывает заголовки в файл
        for user_id, values in sorted(list_data.items()):
            writer.writerow(dict(user_id=user_id, user_name=values[0], time_sub=values[1]))


@dp.message_handler(commands=['Список_пользователей'])
async def bot_start(message: types.Message):
    user_data = await db.get_user_data()
    file_name = 'user_data.csv'
    await set_list_in_csv(user_data, file_name)
    with open(file_name, 'rb') as file:
        await bot.send_document(message.from_user.id, file)

