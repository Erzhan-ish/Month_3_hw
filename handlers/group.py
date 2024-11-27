from aiogram import Router, F, types
from aiogram.filters import Command
from datetime import timedelta

group_router = Router()

@group_router.message(Command("ban", prefix="!"))
async def ban_user(message: types.Message):
    if not message.reply_to_message:
        await message.answer("Направте команду на пользователя")
    else:
        id = message.reply_to_message.from_user.id
        await message.bot.ban_chat_member(
            chat_id=message.chat.id,
            user_id=id,
            until_date=timedelta(hours=2)
        )


bad_words = ['дурак','тупой','простофиля','недоумок','тапок','идиот']

@group_router.message(F.text)
async def ms_group(message: types.Message):
    for word in bad_words:
        if word in message.text.lower():
            await message.answer("Данные слова запрещены")
            await message.delete()
            await message.bot.ban_chat_member(
                chat_id=message.chat.id,
                user_id=message.from_user.id
            )
            break

