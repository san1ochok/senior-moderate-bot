from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config.config import *
from config.db import *

storage = MemoryStorage()
bot = Bot(token=token, parse_mode=parse_mode)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['report'], commands_prefix='/')
async def reportCommand(message: types.Message):
    try:
        msg = message.reply_to_message.text
    except AttributeError:
        pass
    await update_reports(message.reply_to_message.from_user.full_name, message.reply_to_message.from_user.id,
                         message.chat.id, 1)
    await update_messages(message.reply_to_message.from_user.full_name, message.reply_to_message.from_user.id,
                          message.chat.id, 1)
    await update_reportsGlobal(message.reply_to_message.from_user.full_name, message.reply_to_message.from_user.id, 1)
    await update_messagesGlobal(message.reply_to_message.from_user.full_name, message.reply_to_message.from_user.id, 1)
    date = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    l11n = get_localization(message.chat.id)
    match l11n:
        case 'uk':
            await bot.send_message(message.chat.id,
                                   f'❗ *Новий репорт*\n\n*Скарга від:* [{message.from_user.full_name}](tg://user?id={message.from_user.id})\n*Скарга на:* [{message.reply_to_message.from_user.full_name}](tg://user?id={message.reply_to_message.from_user.id})\n*Текст повідомлення:* `{msg}`\n\nЧас: `{date}`')
        case _:
            await bot.send_message(message.chat.id,
                                   f'❗ *Новый репорт*\n\n*Жалоба от:* [{message.from_user.full_name}](tg://user?id={message.from_user.id})\n*Жалоба на:* [{message.reply_to_message.from_user.full_name}](tg://user?id={message.reply_to_message.from_user.id})\n*Текст сообщения:* `{msg}`\n\nВремя: `{date}`')


def register_handlers_report(dp: Dispatcher):
    dp.register_message_handler(reportCommand, commands=['report'], commands_prefix='/!')
