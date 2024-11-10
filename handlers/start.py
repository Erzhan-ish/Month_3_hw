from aiogram import Router, types
from aiogram.filters import Command

start_router = Router()

@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    msg = f"Привет, {name}!"
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(
                text="Наш инстаграм профиль",
                url="https://instagram.com/barashek.restaurant"
                )

            ],
            [types.InlineKeyboardButton(
                text="Наш сайт",
                url="https://barashek.kg"
                )

            ],
            [types.InlineKeyboardButton(
                text="Оставить отзыв",
                callback_data="review"
                )
            ]
        ]
    )
    await message.answer(msg, reply_markup=kb)