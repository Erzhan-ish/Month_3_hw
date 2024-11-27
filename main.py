from bot_config import dp, bot, database
import asyncio

from handlers.admin_restaurant import admin_rest_router
from handlers.dishes import dish_router
from handlers.group import group_router
from handlers.myinfo import myinfo_router
from handlers.random import random_router
from handlers.review_dialog import review_router
from handlers.start import start_router

async def on_startup(bot):
    await bot.send_message(chat_id=5747517813,text="Я тут")
    database.create_tables()

async def main():
    dp.include_router(random_router)
    dp.include_router(myinfo_router)
    dp.include_router(start_router)
    dp.include_router(review_router)
    dp.include_router(admin_rest_router)
    dp.include_router(dish_router)
    dp.include_router(group_router)

    dp.startup.register(on_startup)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())