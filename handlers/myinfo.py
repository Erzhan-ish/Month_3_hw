from aiogram import Router, types
from aiogram.filters import Command

myinfo_router = Router()

@myinfo_router.message(Command("myinfo"))
async def myinfo_handler(message: types.Message):
    id = message.from_user.id
    name = message.from_user.username
    if message.from_user.username is None:
        name = 'Не указан'
    first_name = message.from_user.first_name
    msg = f'id: {id}\nname: {name}\nfirst_name: {first_name}'
    await message.answer(msg)