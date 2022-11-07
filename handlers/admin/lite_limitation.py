from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config.config import *
from config.db import *
from datetime import datetime
from datetime import timedelta


storage = MemoryStorage()
bot = Bot(token=token, parse_mode=parse_mode)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['mute'], commands_prefix='!/')
async def muteCommand(message):
    l11n = get_localization(message.chat.id)
    match l11n:
        case 'uk':
            if not message.reply_to_message:
                await message.reply("Ця команда має бути відповіддю на повідомлення!")
                return
            try:
                muteint = int(message.text.split()[1])
                mutetype = message.text.split()[2]
                comment = " ".join(message.text.split()[3:])
            except IndexError:
                await message.reply('Бракує аргументів!')
                return
            await update_messages(message.reply_to_message.from_user.full_name, message.reply_to_message.from_user.id, message.chat.id, 1)
            await update_messagesGlobal(message.reply_to_message.from_user.full_name, message.reply_to_message.from_user.id, 1)
            await update_limitations(message.reply_to_message.from_user.full_name, message.reply_to_message.from_user.id, message.chat.id, 1)
            await update_limitationsGlobal(message.reply_to_message.from_user.full_name, message.reply_to_message.from_user.id, 1)
            match mutetype:
                case 'ч':
                    dt = datetime.now() + timedelta(hours=muteint)
                    timestamp = dt.timestamp()
                    date = dt.strftime('%Y/%m/%d %H:%M:%S')
                    await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date=timestamp)
                    await message.answer(f"❗ *Новий зам'ючений користувач у цьому чаті: * [{message.reply_to_message.from_user.full_name}](tg://user?id={message.reply_to_message.from_user.id})\nЗняття блокування: `{date}`")
                case 'h':
                    dt = datetime.now() + timedelta(hours=muteint)
                    timestamp = dt.timestamp()
                    date = dt.strftime('%Y/%m/%d %H:%M:%S')
                    await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date=timestamp)
                    await message.answer(f"❗ *Новий зам'ючений користувач у цьому чаті: * [{message.reply_to_message.from_user.full_name}](tg://user?id={message.reply_to_message.from_user.id})\nЗняття блокування: `{date}`")
                case 'м':
                    dt = datetime.now() + timedelta(minutes=muteint)
                    timestamp = dt.timestamp()
                    date = dt.strftime('%Y/%m/%d %H:%M:%S')
                    await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = timestamp)
                    await message.answer(f"❗ *Новий зам'ючений користувач у цьому чаті: * [{message.reply_to_message.from_user.full_name}](tg://user?id={message.reply_to_message.from_user.id})\nЗняття блокування: `{date}`")
                case 'm':
                    dt = datetime.now() + timedelta(minutes=muteint)
                    timestamp = dt.timestamp()
                    date = dt.strftime('%Y/%m/%d %H:%M:%S')
                    await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = timestamp)
                    await message.answer(f"❗ *Новий зам'ючений користувач у цьому чаті: * [{message.reply_to_message.from_user.full_name}](tg://user?id={message.reply_to_message.from_user.id})\nЗняття блокування: `{date}`")
                case 'д':
                    dt = datetime.now() + timedelta(days=muteint)
                    timestamp = dt.timestamp()
                    date = dt.strftime('%Y/%m/%d %H:%M:%S')
                    await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = timestamp)
                    await message.answer(f"❗ *Новий зам'ючений користувач у цьому чаті: * [{message.reply_to_message.from_user.full_name}](tg://user?id={message.reply_to_message.from_user.id})\nЗняття блокування: `{date}`")
                case 'd':
                    dt = datetime.now() + timedelta(days=muteint)
                    timestamp = dt.timestamp()
                    date = dt.strftime('%Y/%m/%d %H:%M:%S')
                    await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = timestamp)
                    await message.answer(f"❗ *Новий зам'ючений користувач у цьому чаті: * [{message.reply_to_message.from_user.full_name}](tg://user?id={message.reply_to_message.from_user.id})\nЗняття блокування: `{date}`")
        case _:
            if not message.reply_to_message:
                await message.reply("Эта команда должна быть ответом на сообщение!")
                return
            try:
                muteint = int(message.text.split()[1])
                mutetype = message.text.split()[2]
                comment = " ".join(message.text.split()[3:])
            except IndexError:
                await message.reply('Не хватает аргументов!\nПример:\n`/mute 1 ч причина`')
                return
            await update_messages(message.reply_to_message.from_user.full_name, message.reply_to_message.from_user.id, message.chat.id, 1)
            await update_messagesGlobal(message.reply_to_message.from_user.full_name, message.reply_to_message.from_user.id, 1)
            await update_limitations(message.reply_to_message.from_user.full_name, message.reply_to_message.from_user.id, message.chat.id, 1)
            await update_limitationsGlobal(message.reply_to_message.from_user.full_name, message.reply_to_message.from_user.id, 1)
            match mutetype:
                case 'ч':
                    dt = datetime.now() + timedelta(hours=muteint)
                    timestamp = dt.timestamp()
                    date = dt.strftime('%Y/%m/%d %H:%M:%S')
                    await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date=timestamp)
                    await message.answer(f"❗ *Новый замьюченый пользователь в этом чате: * [{message.reply_to_message.from_user.full_name}](tg://user?id={message.reply_to_message.from_user.id})\nСнятие бокировки: `{date}`")
                case 'h':
                    dt = datetime.now() + timedelta(hours=muteint)
                    timestamp = dt.timestamp()
                    date = dt.strftime('%Y/%m/%d %H:%M:%S')
                    await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date=timestamp)
                    await message.answer(f"❗ *Новый замьюченый пользователь в этом чате: * [{message.reply_to_message.from_user.full_name}](tg://user?id={message.reply_to_message.from_user.id})\nСнятие бокировки: `{date}`")
                case 'м':
                    dt = datetime.now() + timedelta(minutes=muteint)
                    timestamp = dt.timestamp()
                    date = dt.strftime('%Y/%m/%d %H:%M:%S')
                    await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = timestamp)
                    await message.answer(f"❗ *Новый замьюченый пользователь в этом чате: * [{message.reply_to_message.from_user.full_name}](tg://user?id={message.reply_to_message.from_user.id})\nСнятие бокировки: `{date}`")
                case 'm':
                    dt = datetime.now() + timedelta(minutes=muteint)
                    timestamp = dt.timestamp()
                    date = dt.strftime('%Y/%m/%d %H:%M:%S')
                    await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = timestamp)
                    await message.answer(f"❗ *Новый замьюченый пользователь в этом чате: * [{message.reply_to_message.from_user.full_name}](tg://user?id={message.reply_to_message.from_user.id})\nСнятие бокировки: `{date}`")
                case 'д':
                    dt = datetime.now() + timedelta(days=muteint)
                    timestamp = dt.timestamp()
                    date = dt.strftime('%Y/%m/%d %H:%M:%S')
                    await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = timestamp)
                    await message.answer(f"❗ *Новый замьюченый пользователь в этом чате: * [{message.reply_to_message.from_user.full_name}](tg://user?id={message.reply_to_message.from_user.id})\nСнятие бокировки: `{date}`")
                case 'd':
                    dt = datetime.now() + timedelta(days=muteint)
                    timestamp = dt.timestamp()
                    date = dt.strftime('%Y/%m/%d %H:%M:%S')
                    await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = timestamp)
                    await message.answer(f"❗ *Новый замьюченый пользователь в этом чате: * [{message.reply_to_message.from_user.full_name}](tg://user?id={message.reply_to_message.from_user.id})\nСнятие бокировки: `{date}`")


@dp.message_handler(commands=['unmute'], commands_prefix='!/')
async def unmuteCommand(message):
    l11n = get_localization(message.chat.id)
    match l11n:
        case 'uk':
            if not message.reply_to_message:
                await message.reply("Ця команда має бути відповіддю на повідомлення!")
                return
            await update_messages(message.reply_to_message.from_user.full_name, message.reply_to_message.from_user.id, message.chat.id, 1)
            await update_messagesGlobal(message.reply_to_message.from_user.full_name, message.reply_to_message.from_user.id, 1)
            await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(True, True, True, True))
            await message.reply(f"❗ *Зам'ючений користувач був розблокований у цьому чаті:* [{message.reply_to_message.from_user.full_name}](tg://user?id={message.reply_to_message.from_user.id})")
        case _:
            if not message.reply_to_message:
                await message.reply("Эта команда должна быть ответом на сообщение!")
                return
            await update_messages(message.reply_to_message.from_user.full_name, message.reply_to_message.from_user.id, message.chat.id, 1)
            await update_messagesGlobal(message.reply_to_message.from_user.full_name, message.reply_to_message.from_user.id, 1)
            await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(True, True, True, True))
            await message.reply(f'❗ *Замьюченный пользователь был разблокирован в этом чате:* [{message.reply_to_message.from_user.full_name}](tg://user?id={message.reply_to_message.from_user.id})')


def register_handlers_liteLimitation(dp: Dispatcher):
    dp.register_message_handler(muteCommand, commands=['mute'], commands_prefix='!/', is_chat_admin=True)
    dp.register_message_handler(unmuteCommand, commands=['unmute'], commands_prefix='!/', is_chat_admin=True)

