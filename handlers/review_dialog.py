from aiogram import Router, F, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


review_router = Router()

class RestourantReview(StatesGroup):
    name = State()
    phone_number = State()
    visit_date = State()
    food_rating = State()
    cleanliness_rating = State()
    extra_comments = State()

@review_router.callback_query(F.data == "review")
async def start_review(callback_query: types.CallbackQuery, state: FSMContext):
    await state.set_state(RestourantReview.name)
    await callback_query.message.answer("Как вас зовут?")

@review_router.message(RestourantReview.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.set_state(RestourantReview.phone_number)
    await message.answer("Ваш номер телефона")

@review_router.message(RestourantReview.phone_number)
async def process_phone_number(message: types.Message, state: FSMContext):
    await state.set_state(RestourantReview.visit_date)
    await message.answer("Дата вашего визита")

@review_router.message(RestourantReview.visit_date)
async def process_food_rating(message: types.Message, state: FSMContext):
    await state.set_state(RestourantReview.food_rating)
    await message.answer("Как оцениваете качество еды\n"
                         "1-4 - плохо\n"
                         "5-7 - хорошо\n"
                         "7-10 - отлично")

@review_router.message(RestourantReview.food_rating)
async def process_cleanliness_rating(message: types.Message, state: FSMContext):
    await state.set_state(RestourantReview.cleanliness_rating)
    await message.answer("Как оцениваете чистоту заведенияе\n"
                         "1-4 - плохо\n"
                         "5-7 - хорошо\n"
                         "7-10 - отлично")

@review_router.message(RestourantReview.cleanliness_rating)
async def process_extra_comments(message: types.Message, state: FSMContext):
    await state.set_state(RestourantReview.extra_comments)
    await message.answer("Дополнительные коментарии/Жалобы")

@review_router.message(RestourantReview.extra_comments)
async def process_extra_comments(message: types.Message, state: FSMContext):
    await message.answer("Спасибо за оставленый отзыв!")
    await state.clear()