import config.db as db

from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config.config import *
from keyboards.admin.inlines import *
from states.mailing import BotMailing

storage = MemoryStorage()
bot = Bot(token, parse_mode='markdown')
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(text='Рассылка 📧')
async def start_mailing(message):
    if message.from_user.id != admin:
        await message.answer(f'⚡ Введи текст для розсилки з *Markdown-маркуванням*')
        await BotMailing.text.set()
    else:
        pass


@dp.message_handler(state=BotMailing.text)
async def mailing_text(message, state: FSMContext):
    answer = message.text
    await state.update_data(text=answer)
    await message.answer(text=answer, reply_markup=menuMailing)
    await BotMailing.state.set()


@dp.callback_query_handler(text='next', state=BotMailing.state)
async def startma(call, state: FSMContext):
    data = await state.get_data()
    text = data.get('text')
    for coll in db.list_collection_names():
        try:
            if coll == 'global':
                continue
            await bot.send_message(coll, text=text)
        except Exception:
            pass
    await call.message.answer('Успішна розсилка!')


@dp.callback_query_handler(text='add_photo', state=BotMailing.state)
async def add_photo(call):
    await call.message.answer('Надішли фото')
    await BotMailing.photo.set()


@dp.message_handler(state=BotMailing.photo, content_types=types.ContentType.PHOTO)
async def mailing_photo(message, state: FSMContext):
    photo_file_id = message.photo[-1].file_id
    await state.update_data(photo=photo_file_id)
    data = await state.get_data()
    text = data.get('text')
    photo = data.get('photo')
    await message.answer_photo(photo=photo, caption=text, reply_markup=menuMailing2)


@dp.callback_query_handler(text='next', state=BotMailing.photo)
async def startm(call, state: FSMContext):
    await state.finish()
    data = await state.get_data()
    text = data.get('text')
    photo = data.get('photo')
    for coll in db.list_collection_names():
        try:
            if coll == 'global':
                continue
            await bot.send_photo(coll, photo=photo, caption=text)
        except Exception:
            pass
    await call.message.answer('Успішна розсилка!')
    

@dp.message_handler(state=BotMailing.text)
async def no_photo(message):
    await message.answer('Надішли фото', reply_markup=menuCancel)


@dp.callback_query_handler(text='quit', state=[BotMailing.text, BotMailing.photo, BotMailing.state])
async def quit(call, state: FSMContext):
    await state.finish()
    await call.message.answer('Розсилка відмінена')


def register_handlers_mailing(dp: Dispatcher):
    dp.register_message_handler(start_mailing, text='Рассылка 📧')
    dp.register_message_handler(mailing_text, state=BotMailing.text)
    dp.register_callback_query_handler(startma, text='next', state=BotMailing.state)
    dp.register_callback_query_handler(add_photo,text='add_photo', state=BotMailing.state)
    dp.register_message_handler(mailing_photo, state=BotMailing.photo, content_types=types.ContentType.PHOTO)
    dp.register_callback_query_handler(startm, text='next', state=BotMailing.photo)
    dp.register_message_handler(no_photo, state=BotMailing.text)
    dp.register_callback_query_handler(quit, text='quit', state=[BotMailing.text, BotMailing.photo, BotMailing.state])
