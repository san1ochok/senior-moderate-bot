from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config.config import *
from config.db import *


storage = MemoryStorage()
bot = Bot(token=token, parse_mode=parse_mode)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(text=['+r'])
async def rCommand(message):
    await update_messages(message.from_user.full_name, message.from_user.id, message.chat.id, 1)
    await update_messagesGlobal(message.from_user.full_name, message.from_user.id, 1)
    l11n = get_localization(message.chat.id)
    match l11n:
        case 'uk':
            if not message.reply_to_message:
                await message.reply("Ця команда має бути відповіддю на повідомлення!")
                return

            if message.reply_to_message.from_user.id != message.from_user.id:
                await update_popularity(message.from_user.full_name, message.from_user.id, message.chat.id, 1)
                await update_popularityGlobal(message.from_user.full_name, message.from_user.id, 1)
                await message.reply(
                    f'[Ви](tg://user?id={message.from_user.id}) додали популярність [{message.reply_to_message.from_user.full_name}](tg://user?id={message.reply_to_message.from_user.id})')
            else:
                await message.reply('Ця дія не припустима!')
        case _:
            if not message.reply_to_message:
                await message.reply("Эта команда должна быть ответом на сообщение!")
                return

            if message.reply_to_message.from_user.id != message.from_user.id:
                await update_popularity(message.from_user.full_name, message.from_user.id, message.chat.id, 1)
                await update_popularityGlobal(message.from_user.full_name, message.from_user.id, 1)
                await message.reply(
                    f'[Вы](tg://user?id={message.from_user.id}) добавили популярность [{message.reply_to_message.from_user.full_name}](tg://user?id={message.reply_to_message.from_user.id})')
            else:
                await message.reply('Данное действие не допустимо!')


@dp.message_handler(commands="рейтинг", commands_prefix='!')
async def dashboardCommand(message):
    await update_messages(message.from_user.full_name, message.from_user.id, message.chat.id, 1)
    await update_messagesGlobal(message.from_user.full_name, message.from_user.id, 1)
    l11n = get_localization(message.chat.id)
    match l11n:
        case 'uk':
            leadermsg = '📊 СТАТИСТИКА АКТИВНИХ КОРИСТУВАЧІВ ЧАТУ\n\n'
            parsed = db[f"{message.chat.id}"].find().sort("count_messages", -1).limit(10)
            for j in range(1):
                for user in parsed:
                    j += 1
                    names = f"{user['full_name']}"
                    leadermsg += f" {j}. {names} — {user['count_messages']}\n"
                    """fl3 = leadermsg.replace(" 3.", " 🥉|")
                    fl2 = fl3.replace(" 2.", " 🥈|")
                    fl = fl2.replace(" 1.", " 🥇|")"""
            await message.reply(str(leadermsg), disable_web_page_preview=True, parse_mode='html')
        case _:
            leadermsg = '📊 СТАТИСТИКА ОБЩИТЕЛЬНЫХ ПОЛЬЗОВАТЕЛЕЙ ЧАТА\n\n'
            parsed = db[f"{message.chat.id}"].find().sort("count_messages", -1).limit(10)
            for j in range(1):
                for user in parsed:
                    j += 1
                    names = f"{user['full_name']}"
                    leadermsg += f" {j}. {names} — {user['count_messages']}\n"
                    """fl3 = leadermsg.replace(" 3.", " 🥉|")
                    fl2 = fl3.replace(" 2.", " 🥈|")
                    fl = fl2.replace(" 1.", " 🥇|")"""
            await message.reply(str(leadermsg), disable_web_page_preview=True, parse_mode='html')


def register_handlers_popularity(dp: Dispatcher):
    dp.register_message_handler(rCommand, text=['+r'])
    dp.register_message_handler(dashboardCommand, commands="рейтинг", commands_prefix='/!')
