from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config.config import *

from keyboards.admin.replies import *

storage = MemoryStorage()
bot = Bot(token=TOKEN, parse_mode=PARSE_MODE)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands='admin')
async def adminMenuCommand(message):
    if message.from_user.id == ADMIN:
        await message.answer('✅ Доступ разрешён!', reply_markup=menuAdmin)
    else:
        pass


def register_handlers_adminMenu(dp: Dispatcher):
    dp.register_message_handler(adminMenuCommand, commands='admin')
