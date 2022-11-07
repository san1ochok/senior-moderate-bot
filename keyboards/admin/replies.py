from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnMailing = KeyboardButton('Рассылка 📧')

menuAdmin = ReplyKeyboardMarkup(resize_keyboard=True).add(btnMailing)
