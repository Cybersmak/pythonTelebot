from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btnProfile = KeyboardButton('ПРОФИЛЬ')
btnSub = KeyboardButton('Сводные показатели')

mainMenu = ReplyKeyboardMarkup(resize_keyboard = True)
mainMenu.add(btnProfile,btnSub)