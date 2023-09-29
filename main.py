import asyncio
import db
import config
from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot(config.TOKEN)


@bot.message_handler(func=lambda m: m.text.lower() == '/start' and m.chat.type == 'private')
async def send_welcome(message):
    user_id = message.from_user.id
    fname = message.from_user.first_name
    lname = message.from_user.last_name
    uname = message.from_user.username
    db.insert_member(user_id, fname, lname, uname)
    await bot.send_message(message.chat.id, "Теперь Вы будете в курсе всех наших анонсов!")


@bot.message_handler(func=lambda m: m.text.lower().split()[0] == '/public' and m.chat.type == 'private')
async def info_message(message):
    if message.chat.id == config.admin:
        await bot.send_message("@bottestim", ' '.join(message.text.split()[1:]))


@bot.message_handler(func=lambda m: m.text.lower().split()[0] == '/public' and m.chat.type == 'private')
async def info_message(message):
    if message.chat.id == config.admin:
        await bot.send_message("@bottestim", ' '.join(message.text.split()[1:]))


@bot.message_handler(func=lambda m: m.text.lower().split()[0] == '/all' and m.chat.type == 'private')
async def private_message(message):
    if message.chat.id == config.admin:
        data = db.select_members()
        for id in data:
            await bot.send_message(id[0], ' '.join(message.text.split()[1:]))


asyncio.run(bot.polling())
