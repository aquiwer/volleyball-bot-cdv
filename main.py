import asyncio
from aiogram import Bot, Dispatcher, executor, types
import requests
# from bs4 import BeautifulSoup
import re
import math
import time
import functools
import random

from datetime import datetime

# import numpy as np

bot = Bot(token="2123107411:AAEcsw9wKqG7B_TFHPMr5brQC3Rozqbu6Q4")
dp = Dispatcher(bot)

@dp.message_handler(content_types=["new_chat_members"])
async def handler_new_member(message):
    user_name = message.new_chat_members[0].username
    await bot.send_message(message.chat.id, f"Добро пожаловать, @{user_name}! Какой опыт в волейболе? :)")


@dp.message_handler(regexp="Привет")
async def check_language(message: types.Message):
    list =[
        "Привет :D",
        "Если нужно было бы выбрать только один вариант, вы бы хотели, чтобы ваш ребенок вырос умным или добрым?",
        "Есть какая-то информация или теория, в которую вы просто верите, так как у нее нет доказательств? Почему?",
        "Как делишки?",
        "Чего вы боитесь больше всего на свете?",
        "Если бы у вас была возможность навсегда остаться в каком-то возрасте, какой возраст вы бы выбрали?",
    ]
    random_index = random.randint(0, len(list) - 1)

    await message.reply(list[random_index])

# async def say_good_night(message: types.Message):
#     current_datetime = datetime.now()
#     if current_datetime.hour == 22:
#         await bot.send_message(message.chat.id, "Good night :)")
#
# @dp.message_handler(content_types=["sticker"])
# async def delete_stickers(message: types.Message):
#     if message["from"].username == "dimovski5":
#         await bot.delete_message(message.chat.id, message.message_id)


executor.start_polling(dp, skip_updates=True)
