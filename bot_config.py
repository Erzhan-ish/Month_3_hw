from aiogram import Bot, Dispatcher
from dotenv import dotenv_values

from database.review_answers import Database

token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()

review_answer = Database("review_answers.sqlite")

