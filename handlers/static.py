from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config.config import *
from config.db import *

storage = MemoryStorage()
bot = Bot(token=token, parse_mode=parse_mode)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(content_types=['new_chat_members'])
async def newMemberEvent(message):
    full_name = message.from_user.full_name
    user_id = message.from_user.id
    group_id = message.chat.id
    # Create DB if it doesn't exist
    CreateDB(group_id)
    if message.chat.type != 'private':
        search_user_id = db[f"{message.chat.id}"].find_one({"_id": user_id})
        if search_user_id:
            # If exists in DB
            pass
            l11n = get_localization(message.chat.id)
            match l11n:
                case 'uk':
                    await message.answer(
                        f"Ласкаво просимо, [{message.from_user.full_name}](tg://user?id={message.from_user.id}) !\n"
                        f"\n_Приєднавшись до чату, Ви автоматично приймаєте його внутрішні правила. Не знання правил, "
                        f"не звільняє Вас від відповідальності!_\n\nВи можете допомогти розробці в розробці боту ставши контрібутором на GitHub!",
                        parse_mode='markdown')
                case _:
                    await message.answer(
                        f"Добро пожаловать, [{message.from_user.full_name}](tg://user?id={message.from_user.id}) !"
                        f"\n_Подключившись к чату, Вы автоматически принимаете его внутренние правила. Не знание "
                        f"правил, не освобождает Вас от ответственности!_",
                        parse_mode='markdown')
        else:
            # If doesn't exists in DB
            await add_user(full_name, user_id, group_id)
            await add_userGlobal(full_name, user_id)
    else:
        search_user_id_global = db["global"].find_one({"_id": user_id})
        if search_user_id_global:
            pass
        else:
            await add_userGlobal(full_name, user_id)
        await message.answer('Бот работает только в группах :(')


def register_handlers_static(dp: Dispatcher):
    dp.register_message_handler(newMemberEvent, content_types=['new_chat_members'])
