from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config.config import *
from config.db import *

from keyboards.admin.inlines import *

storage = MemoryStorage()
bot = Bot(token=token, parse_mode=parse_mode)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(text=["hug", 'обнять', 'обійняти'])
async def hugCommand(message):
    await update_messages(message.from_user.full_name, message.from_user.id, message.chat.id, 1)
    await update_messagesGlobal(message.from_user.full_name, message.from_user.id, 1)
    l11n = get_localization(message.chat.id)
    match l11n:
        case 'uk':
            await message.reply(
                f"<b><a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a></b> обійняв <b><a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.first_name}</a></b> 🤗",
                parse_mode="html")
        case _:
            await message.reply(
                f"<b><a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a></b> обнял <b><a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.first_name}</a></b> 🤗",
                parse_mode="html")


@dp.message_handler(text=["kiss", 'поцеловать', 'поцілувати'])
async def kissCommand(message):
    await update_messages(message.from_user.full_name, message.from_user.id, message.chat.id, 1)
    await update_messagesGlobal(message.from_user.full_name, message.from_user.id, 1)
    l11n = get_localization(message.chat.id)
    match l11n:
        case 'uk':
            await message.reply(
                f"<b><a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a></b> поцілував <b><a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.first_name}</a></b> 💋",
                parse_mode="html")
        case _:
            await message.reply(
                f"<b><a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a></b> поцеловал <b><a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.first_name}</a></b> 💋",
                parse_mode="html")


@dp.message_handler(text=["intim", 'интим', 'інтим'])
async def intimCommand(message):
    await update_messages(message.from_user.full_name, message.from_user.id, message.chat.id, 1)
    await update_messagesGlobal(message.from_user.full_name, message.from_user.id, 1)
    l11n = get_localization(message.chat.id)
    match l11n:
        case 'uk':
            if message.reply_to_message.from_user.id == admin:
                await message.answer('Ай-ай-ай, пустуня')
            else:
                await message.reply(
                    f"<b><a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a></b> примусив до інтиму <b><a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.first_name}</a></b> ❤️‍🔥",
                    parse_mode="html")
        case _:
            if message.reply_to_message.from_user.id == admin:
                await message.answer('Ай-ай-ай, шалунишка')
            else:
                await message.reply(
                    f"<b><a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a></b> принудил к интиму <b><a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.first_name}</a></b> ❤️‍🔥",
                    parse_mode="html")


@dp.message_handler(text=["kill", 'убить', 'вбити'])
async def killCommand(message):
    await update_messages(message.from_user.full_name, message.from_user.id, message.chat.id, 1)
    await update_messagesGlobal(message.from_user.full_name, message.from_user.id, 1)
    l11n = get_localization(message.chat.id)
    match l11n:
        case 'uk':
            if message.reply_to_message.from_user.id == admin:
                await message.answer('Ай-ай-ай, фу так робити')
            else:
                await message.reply(
                    f"<b><a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a></b> вбив <b><a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.first_name}</a></b> 🔫",
                    parse_mode="html")
        case _:
            if message.reply_to_message.from_user.id == admin:
                await message.answer('Ай-ай-ай, фу так делать')
            else:
                await message.reply(
                    f"<b><a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a></b> убил <b><a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.first_name}</a></b> 🔫",
                    parse_mode="html")


def register_handlers_fun(dp: Dispatcher):
    dp.register_message_handler(hugCommand, text=["hug", 'обнять', 'обійняти'])
    dp.register_message_handler(kissCommand, text=["kiss", 'поцеловать', 'поцілувати'])
    dp.register_message_handler(intimCommand, text=["intim", 'интим', 'інтим'])
    dp.register_message_handler(killCommand, text=["kill", 'убить', 'вбити'])
