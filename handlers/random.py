from aiogram import Router, types
from aiogram.filters import Command
from random import choice

random_router = Router()

@random_router.message(Command("random"))
async def random_handler(message: types.Message):
    plov = types.FSInputFile("images/plov.jpg")
    beshbarmak = types.FSInputFile("images/beshbarmak.jpg")
    ashlyanfu = types.FSInputFile("images/ashlyanfu.jpg")
    menu = [plov, beshbarmak, ashlyanfu]
    random_dish = choice(menu)

    if random_dish == plov:
        await message.answer_photo(
            photo=plov,
            caption="----------ПЛОВ----------\n"
                    "Баранина - 1кг\nДлиннозерный рис - 500г\nРепчатый лук - 4шт\nРастительное масло - 300мл\nЧеснок - 2 шт\n"
                    "Морковь - 1кг\nСушеный красный перец - 2шт\nМолотый кумин(зира) - 1 столовая ложка\nСемена кориандра - 1 чайная ложка\n"
                    "Соль - по вкусу\nСушеный барбарис - 1 столовая лошка ")

    if random_dish == beshbarmak:
        await message.answer_photo(
            photo=beshbarmak,
            caption="----------БЕШБАРМАК----------\n"
                    "Баранина - 500гр\n"
                    "Говядина - 500гр\n"
                    "Морковь - 1шт\n"
                    "Лук - 2-3шт\n"
                    "Мука - 1,5ст\n"
                    "Яйца - 2шт\n"
                    "Черный перец - 1 чайная ложка\n"
                    "Душистый перец - 1 чайная ложка\n"
                    "Лаврушка - по вкусу\n"
                    "Соль - повкусу")

    if random_dish == ashlyanfu:
        await message.answer_photo(
            photo=ashlyanfu,
            caption="----------АШЛЯНФУ----------\n"
                    "Чеснок - 2зуб\n"
                    "Соевый соус - 2 столовых ложек\n"
                    "Сахар - 1 чайная ложка\n"
                    "Сладкий перец - 150гр\n"
                    "Огурец - 150гр\n"
                    "Морковь - 100гр\n"
                    "Растительное масло - 110мл\n"
                    "Зеленый лук перо - 20гр\n"
                    "Соль - по вкусу\n"
                    "Черный молотый перец - по вкусу\n"
                    "Кориандр - по вкусу\n"
                    "Говядина - 250гр\n"
                    "Порошок перца чили - по вкусу\n"
                    "Фунчоза - 100гр\n"
                    "Уксусная эссенция - 1 чайная ложка"
        )