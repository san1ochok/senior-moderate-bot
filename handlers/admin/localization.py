from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config.config import *
from config.db import *

storage = MemoryStorage()
bot = Bot(token=token, parse_mode=parse_mode)
dp = Dispatcher(bot, storage=storage)


# localize_types = ['uk', 'ru']
@dp.message_handler(commands='localization', commands_prefix="!/", is_chat_admin=True)
async def setLocalization(message):
    try:
        Intype = message.text.split()[1]
    except IndexError:
        await message.reply('No args')
        return
    await update_messages(message.from_user.full_name, message.from_user.id, message.chat.id, 1)
    await update_messagesGlobal(message.from_user.full_name, message.from_user.id, 1)
    match Intype:
        case 'uk':
            await update_localization(message.chat.id, index=Intype)
            await message.answer('🇺🇦 Мова боту для вашого чату успішно змінена!')
        case 'ru':
            await update_localization(message.chat.id, index=Intype)
            await message.answer('Язык бота для вашего чата успешно изменен!')
        case _:
            await message.answer('ERROR')


def register_handlers_localization(dp: Dispatcher):
    dp.register_message_handler(setLocalization, commands='localization', commands_prefix="!/", is_chat_admin=True)
