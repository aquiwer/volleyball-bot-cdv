import asyncio
from aiogram import Bot, Dispatcher, executor, types
import requests
# from bs4 import BeautifulSoup
import re
import math
import time
import functools

# import numpy as np

bot = Bot(token="2123107411:AAEcsw9wKqG7B_TFHPMr5brQC3Rozqbu6Q4")
dp = Dispatcher(bot)


@dp.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
    print(message, 'message')
    user_name = message.new_chat_member[0].username
    bot.send_message(message.chat.id, f"Добро пожаловать, @{user_name}! Сколько лет занимаешься волейболом? :)")


@dp.message_handler(regexp="Привет")
async def check_language(message: types.Message):
    await message.reply("Привет :D")


#
# @dp.message_handler(content_types=["sticker"])
# async def delete_stickers(message: types.Message):
#     if message["from"].username == "dimovski5":
#         await bot.delete_message(message.chat.id, message.message_id)


executor.start_polling(dp, skip_updates=True)
