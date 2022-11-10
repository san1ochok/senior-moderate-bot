from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config.config import *
from config.db import *

storage = MemoryStorage()
bot = Bot(token=token, parse_mode=parse_mode)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands='help', commands_prefix='/')
async def helpCommand(message):
    l11n = get_localization(message.chat.id)
    match l11n:
        case 'uk':
            await message.answer(
                f'Повний список усіх команд можна переглянути за посиланням: _https://teletype.in/@alexndrev/TA8LkHJBbGR_\n\nПропозиції та побажання можна залишити тут: [ᴀʟᴇxɴᴅʀᴇᴠ](t.me/alexndrev)')
        case _:
            await message.answer(
                f'Полный список всех команд можно посмотреть по ссылке: _https://teletype.in/@alexndrev/TA8LkHJBbGR_\n\nПредложения и пожелания можно оставить тут: [ᴀʟᴇxɴᴅʀᴇᴠ](t.me/alexndrev)')


def register_handlers_help(dp: Dispatcher):
    dp.register_message_handler(helpCommand, commands='help', commands_prefix='/')
