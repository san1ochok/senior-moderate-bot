# = = = = = = = = = = = = = = = = = = = = = = =
#  Project was created by Ukrainian Developer
#  Github: alexndrev
#  Telegram: alexndrev
# = = = = = = = = = = = = = = = = = = = = = = =
from aiogram import Bot, Dispatcher, executor
from config.keep_alive import keep_alive
from handlers.admin.admin_menu import *
from handlers.admin.localization import *

from handlers.admin.mailing import *
from handlers.admin.limitation import *
from handlers.admin.report import *
from handlers.admin.lite_limitation import *

from handlers.client.me import *
from handlers.client.popularity import *
from handlers.client.fun import *

from handlers.static import *
from handlers.help import *

import json

keep_alive()
storage = MemoryStorage()
bot = Bot(token=token, parse_mode=parse_mode)
dp = Dispatcher(bot, storage=storage)

register_handlers_static(dp)
register_handlers_localization(dp)

register_handlers_adminMenu(dp)
register_handlers_mailing(dp)
register_handlers_limitation(dp)
register_handlers_report(dp)
register_handlers_liteLimitation(dp)

register_handlers_me(dp)
register_handlers_popularity(dp)
register_handlers_fun(dp)
register_handlers_help(dp)


@dp.message_handler(commands='data', is_chat_admin=True)
async def anys(message):
    user_id = message.reply_to_message.from_user.id
    chat_id = message.reply_to_message.chat.id
    name = message.reply_to_message.from_user.full_name
    join_date = datetime.now().strftime('%H:%M:%S %d.%m.%Y')

    data = {"_id": {"$numberInt": f"{user_id}"}, "UID": f"{chat_id}", "group_id": {"$numberLong": f"{chat_id}"},
            "full_name": f"{name}", "joining_date": f"{join_date}", "popularity": {"$numberInt": "0"}, "motto": "null",
            "count_messages": {"$numberInt": "0"}, "count_limitations": {"$numberInt": "0"},
            "count_reports": {"$numberInt": "0"}}
    convert_data = json.dumps(data)
    await message.answer(f"<code>{convert_data}</code>", parse_mode='html')


thank_words = ['спасибо', 'спс', 'дякую', 'сенкс', 'фенк', 'спасибі', 'thx', 'thanks', 'thank']


@dp.message_handler()
async def startCommand(message):
    search_localize_id = db[f"localization"].find_one({"group_id": message.chat.id})
    if search_localize_id:
        pass
    else:
        await add_localization(message.chat.id)
    file = open(f"cache/{message.chat.id}.txt", "a", encoding='utf8')
    file.write(f"{datetime.now().strftime('%H:%M:%S %d.%m.%Y')} | {message.from_user.full_name} | {message.text}\n")
    file.close()

    await update_messages(message.from_user.full_name, message.from_user.id, message.chat.id, 1)
    await update_messagesGlobal(message.from_user.full_name, message.from_user.id, 1)

    CreateDB(message.chat.id)
    if message.chat.type != 'private':
        search_user_id = db[f"{message.chat.id}"].find_one({"_id": message.from_user.id})
        if search_user_id:
            if any(word in message.text.lower() for word in thank_words):
                l11n = get_localization(message.chat.id)
                match l11n:
                    case 'uk':
                        await message.reply(
                            "Якщо тобі хтось допоміг, можеш прописати `+r`, відповів на повідомлення, щоб додати йому "
                            "популярність 😉")
                    case _:
                        await message.reply(
                            "Если тебе кто-то помог, можешь прописать `+r`, ответив на сообщение, что б добавить ему "
                            "популярность 😉")

        else:
            await add_user(message.from_user.full_name, message.from_user.id, message.chat.id)
            await add_userGlobal(message.from_user.full_name, message.from_user.id)
            if any(word in message.text.lower() for word in thank_words):
                l11n = get_localization(message.chat.id)
                match l11n:
                    case 'uk':
                        await message.reply(
                            "Якщо тобі хтось допоміг, можеш прописати `+r`, відповів на повідомлення, щоб додати йому "
                            "популярність 😉")
                    case _:
                        await message.reply(
                            "Если тебе кто-то помог, можешь прописать `+r`, ответив на сообщение, что б добавить ему "
                            "популярность 😉")
    else:
        search_user_id_global = db["global"].find_one({"_id": message.from_user.id})
        if search_user_id_global:
            pass
        else:
            await add_userGlobal(message.from_user.full_name, message.from_user.id)
        await message.answer('Бот работает только в группах :(')


if __name__ == '__main__':
    try:
        executor.start_polling(dp, skip_updates=True)
    except BaseException as _ex:
        print('\n\033[31mAn error was detected : ', _ex, '\033[39m')
        print('- - - - - - - - - - - - - -')
