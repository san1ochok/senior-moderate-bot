from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config.config import *
from config.db import *


storage = MemoryStorage()
bot = Bot(token=token, parse_mode=parse_mode)
dp = Dispatcher(bot, storage=storage)


async def iamCommand(message):
    await update_messages(message.from_user.full_name, message.from_user.id, message.chat.id, 1)
    await update_messagesGlobal(message.from_user.full_name, message.from_user.id, 1)
    l11n = get_localization(message.chat.id)
    match l11n:
        case 'uk':
            await message.reply(f'Це [{message.from_user.full_name}](tg://user?id={message.from_user.id})\n⏱ У моєму всесвіті: з {await get_joiningDateGlobal(message.from_user.id)}\n👩🏻‍💼 Девіз: {await get_motto(message.from_user.id, message.chat.id)}')
        case _:
            await message.reply(f'Это [{message.from_user.full_name}](tg://user?id={message.from_user.id})\n⏱ В моей вселенной: с {await get_joiningDateGlobal(message.from_user.id)}\n👩🏻‍💼 Девиз: {await get_motto(message.from_user.id, message.chat.id)}')


async def addMotto(message):
    await update_messages(message.from_user.full_name, message.from_user.id, message.chat.id, 1)
    await update_messagesGlobal(message.from_user.full_name, message.from_user.id, 1)
    l11n = get_localization(message.chat.id)
    match l11n:
        case 'uk':
            try:
                text = str(message.text[7:])
            except IndexError:
                await message.reply('Бракує аргументів!')
                return
            match text:
                case "":
                    await message.reply('Бракує аргументів!')
                    return
                case _:
                    await message.answer(f'✅ Ваш девіз змінено на «{text}»')
                    await update_motto(message.from_user.full_name, message.from_user.id, message.chat.id, text)
        case _:
            try:
                text = str(message.text[7:])
            except IndexError:
                await message.reply('Не хватает аргументов!')
                return
            match text:
                case "":
                    await message.reply('Не хватает аргументов!')
                    return
                case _:
                    await message.answer(f'✅ Ваш девиз изменён на «{text}»')
                    await update_motto(message.from_user.full_name, message.from_user.id, message.chat.id, text)


async def removeMotto(message):
    await update_messages(message.from_user.full_name, message.from_user.id, message.chat.id, 1)
    await update_messagesGlobal(message.from_user.full_name, message.from_user.id, 1)
    await update_motto(message.from_user.full_name, message.from_user.id, message.chat.id, index="null")
    l11n = get_localization(message.chat.id)
    match l11n:
        case 'uk':
            await message.answer(f'❎ Девіз видалено')
        case _:
            await message.answer(f'❎ Девиз удалён')


async def myMotto(message):
    await update_messages(message.from_user.full_name, message.from_user.id, message.chat.id, 1)
    await update_messagesGlobal(message.from_user.full_name, message.from_user.id, 1)
    l11n = get_localization(message.chat.id)
    match l11n:
        case 'uk':
            motto_status = await get_motto(message.from_user.id, message.chat.id)
            match motto_status:
                case 'null':
                    await message.answer("📝 Девіз поки не встановлено")
                case _:
                    await message.answer(f'🗓 Девіз користувача: «{await get_motto(message.from_user.id, message.chat.id)}»')
        case _:
            motto_status = await get_motto(message.from_user.id, message.chat.id)
            match motto_status:
                case 'null':
                    await message.answer("📝 Девиз пока не установлен")
                case _:
                    await message.answer(f'🗓 Девиз пользователя: «{await get_motto(message.from_user.id, message.chat.id)}»')


def register_handlers_me(dp: Dispatcher):
    dp.register_message_handler(iamCommand, commands=['me'], commands_prefix='/!')
    dp.register_message_handler(addMotto, commands=['девиз', 'девіз'], commands_prefix='+')
    dp.register_message_handler(removeMotto, commands=['девиз', 'девіз'], commands_prefix='-')
    dp.register_message_handler(myMotto, commands=['девиз', 'девіз'], commands_prefix='!')

