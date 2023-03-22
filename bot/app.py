from aiogram import executor
import asyncio

from loader import dp
import middlewares, handlers
from utils.misc.set_bot_commands import set_default_commands
from utils.notify_admins import on_startup_notify
from data import db


async def on_startup(dispatcher):
    db.connected_db()
    # Уведомляет про запуск
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)
    loop = asyncio.get_event_loop()
    loop.create_task(check_sub())


async def check_sub():
    while True:
        await asyncio.sleep(60)
        user_list = await db.get_user_list()
        for user in user_list:
            if not await db.get_sub_status(user) and await db.get_time_sub(user) != 0:
                await dp.bot.send_message(user, "У вас кончилась подписка. Нажмите кнопку скрин оплаты и следуйте инструкции")
                await db.set_time_sub(user, 0)
                await dp.bot.ban_chat_member(-11111111111, user)
        



if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
