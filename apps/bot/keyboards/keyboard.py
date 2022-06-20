from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


b2 = KeyboardButton('/Thuesday')
b3 = KeyboardButton('/Wednesday')
b4 = KeyboardButton('/Thursday')
b5 = KeyboardButton('/Friday')
b6 = KeyboardButton('/Saturday')
b7 = KeyboardButton('/Sunday')
kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.row(b2, b3, b4).add(b5, b6, b7)

b8 = KeyboardButton('Мои данные🎫')
menu_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
menu_kb.row(b8)

b1 = KeyboardButton('Дни недели')
b9 = KeyboardButton('Изменить имя🖊')
b10 = KeyboardButton('Изменить фамилию🖊')
b11 = KeyboardButton('Назад⬅')
user_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
user_kb.row(b1 ,b9, b10).add(b11)

# b15 = KeyboardButton('Gjytltkmybr')
# b16 = KeyboardButton('fdvsavvadv')
# kb_user = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# kb_user.add(b15, b16)