from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config.config import *
from config.db import *


storage = MemoryStorage()
bot = Bot(token=token, parse_mode=parse_mode)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['ban'], commands_prefix='!/')
async def banCommand(message):
    await update_limitations(message.reply_to_message.from_user.full_name, message.reply_to_message.from_user.id, message.chat.id, 1)
    await update_limitationsGlobal(message.reply_to_message.from_user.full_name, message.reply_to_message.from_user.id, 1)
    await update_messages(message.reply_to_message.from_user.full_name, message.reply_to_message.from_user.id, message.chat.id, 1)
    await update_messagesGlobal(message.reply_to_message.from_user.full_name, message.reply_to_message.from_user.id, 1)
    l11n = get_localization(message.chat.id)
    match l11n:
        case 'uk':
            if not message.reply_to_message:
                await message.reply("Ця команда має бути відповіддю на повідомлення!")
                return
            else:
                await message.reply_to_message.delete()
                await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False))
                await message.answer(f'❗ *Новий забанений користувач у цьому чаті:* [{message.reply_to_message.from_user.full_name}](tg://user?id={message.reply_to_message.from_user.id})')

        case _:
            if not message.reply_to_message:
                await message.reply("Эта команда должна быть ответом на сообщение!")
                return
            else:
                await message.reply_to_message.delete()
                await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False))
                await message.answer(f'❗ *Новый забаненный пользователь в этом чате:* [{message.reply_to_message.from_user.full_name}](tg://user?id={message.reply_to_message.from_user.id})')


@dp.message_handler(commands=['unban'], commands_prefix='!/')
async def unbanCommand(message):
    await update_messages(message.reply_to_message.from_user.full_name, message.reply_to_message.from_user.id, message.chat.id, 1)
    await update_messagesGlobal(message.reply_to_message.from_user.full_name, message.reply_to_message.from_user.id, 1)
    l11n = get_localization(message.chat.id)
    match l11n:
        case 'uk':
            if not message.reply_to_message:
                await message.reply("Ця команда має бути відповіддю на повідомлення!")
                return
            await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(True, True, True, True))
            await message.reply(f'❗ *Забанений користувач був заблокований у цьому чаті:* [{message.reply_to_message.from_user.full_name}](tg://user?id={message.reply_to_message.from_user.id})')

        case _:
            if not message.reply_to_message:
                await message.reply("Эта команда должна быть ответом на сообщение!")
                return
            await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(True, True, True, True))
            await message.reply(f'❗ *Забаненный пользователь был разблокирован в этом чате:* [{message.reply_to_message.from_user.full_name}](tg://user?id={message.reply_to_message.from_user.id})')


def register_handlers_limitation(dp: Dispatcher):
    dp.register_message_handler(banCommand, commands=['ban'], commands_prefix='!/', is_chat_admin=True)
    dp.register_message_handler(unbanCommand, commands=['unban'], commands_prefix='!/', is_chat_admin=True)
