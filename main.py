from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token="your token")
dp = Dispatcher(bot)


@dp.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
    print(message, 'message')
    user_name = message.new_chat_member[0].username
    bot.send_message(message.chat.id, f"Добро пожаловать, @{user_name}! Сколько лет занимаешься волейболом? :)")


@dp.message_handler(regexp="Привет")
async def check_language(message: types.Message):
    await message.reply("Привет :D")





executor.start_polling(dp, skip_updates=True)
