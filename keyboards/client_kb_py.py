from aiogram.types import ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove

b1 = KeyboardButton('/Monday')
b2 = KeyboardButton('/Thuesday')
b3 = KeyboardButton('/Wednesday')
b4 = KeyboardButton('/Thursday')
b5 = KeyboardButton('/Friday')
b6 = KeyboardButton('/Saturday')
b7 = KeyboardButton('/Sunday')
kb_client = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)

kb_client.row(b1,b2,b3,b4).add(b5,b6,b7)
