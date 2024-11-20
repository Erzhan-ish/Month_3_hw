from aiogram import Router, F, types
from aiogram.fsm.state import State, StatesGroup, default_state
from aiogram.fsm.context import FSMContext

from bot_config import review_answer

review_router = Router()

class RestourantReview(StatesGroup):
    name = State()
    phone_number = State()
    visit_date = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()


food_rating_num = {
    "Плохо": 1,
    "Хорошо": 3,
    "Отлично": 5
}

@review_router.message(F.text.in_(["stop", "стоп"]))
async def stop_review(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("Отзыв прерван")


@review_router.callback_query(F.data == "review", default_state)
async def start_review(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(RestourantReview.name)
    await callback_query.message.answer("Как вас зовут?")


@review_router.message(RestourantReview.name)
async def process_name(message: types.Message, state: FSMContext):
    name = message.text
    if not name.isalpha():
        await message.answer("Вводите только буквами!")
        return

    if len(name) > 15:
        await message.answer("Вводите не больше 15 символов!")
        return

    await state.update_data(name=message.text)
    await state.set_state(RestourantReview.phone_number)
    await message.answer("Ваш номер телефона")


@review_router.message(RestourantReview.phone_number)
async def process_phone_number(message: types.Message, state: FSMContext):
    number = message.text
    if not number.isdigit():
        await message.answer("Вводите только номер(цифрами)!")
        return
    await state.update_data(phone_number=message.text)
    await state.set_state(RestourantReview.visit_date)
    await message.answer("Дата вашего визита")

@review_router.message(RestourantReview.visit_date)
async def process_food_rating(message: types.Message, state: FSMContext):
    await state.update_data(visit_date=message.text)
    await state.set_state(RestourantReview.food_rating)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Плохо"),
                types.KeyboardButton(text="Хорошо"),
                types.KeyboardButton(text="Отлично")
            ]
        ]
    )
    await message.answer("Как оцениваете качество еды", reply_markup=kb)



@review_router.message(RestourantReview.food_rating, F.text.in_(["Плохо","Хорошо","Отлично"]))
async def process_cleanliness_rating(message: types.Message, state: FSMContext):
    kb = types.ReplyKeyboardRemove()
    food_ratingg = message.text
    if food_ratingg in food_rating_num:
        food_rating_val = food_rating_num[food_ratingg]
        await state.update_data(food_rating=food_rating_val)
        await state.set_state(RestourantReview.cleanliness_rating)
        await message.answer("Как оцениваете чистоту заведения\n"
                         "от 1 до 10", reply_markup=kb)


@review_router.message(RestourantReview.cleanliness_rating)
async def process_extra_comments(message: types.Message, state: FSMContext):
    ball = message.text
    if not ball.isdigit() or int(ball) < 1 or int(ball) > 10:
        await message.answer("Вводите только цифры от 1 до 10!")
        return
    await state.update_data(cleanliness_rating=message.text)
    await state.set_state(RestourantReview.extra_comments)
    await message.answer("Дополнительные коментарии/Жалобы")


@review_router.message(RestourantReview.extra_comments)
async def process_extra_comments(message: types.Message, state: FSMContext):
    await message.answer("Спасибо за оставленый отзыв!")
    await state.update_data(extra_comments=message.text)
    data = await state.get_data()
    print(data)
    await state.clear()

    review_answer.execute(
        query="""
            INSERT INTO reviews (name, phone_number, visit_date, food_rating, cleanliness_rating, extra_comments)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
        params=(data["name"], data["phone_number"], data["visit_date"], data["food_rating"], data["cleanliness_rating"],
                data["extra_comments"]),
    )
    await state.clear()