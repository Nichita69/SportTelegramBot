from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('Дни недели')
b11 = KeyboardButton('Назад⬅')

user_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
user_kb.row(b1).add(b11)

bthRandom = KeyboardButton('Мои данные🎫')
bthOther = KeyboardButton('Другое№')

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(bthRandom, bthOther)

b15 = KeyboardButton('Monday')
b16 = KeyboardButton('Thuesday')
b17 = KeyboardButton('Wednesday')
b18 = KeyboardButton('Thursday')
b19 = KeyboardButton('Friday')
b20 = KeyboardButton('Saturday')
b21 = KeyboardButton('Sunday')
b11 = KeyboardButton('Назад⬅')
kb_user = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_user.add(b15, b16, b17, b18, b19, b20, b21, b11)

b24 = KeyboardButton('Тренировка')
b11 = KeyboardButton('Назад⬅')
user_go = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
user_go.add(b24, b11)

b25 = KeyboardButton('Тренировка утром')
b26 = KeyboardButton('Тренировка вечером')
b11 = KeyboardButton('Назад⬅')
user_goo = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
user_goo.add(b25, b26, b11)

b27 = KeyboardButton('Нажми сюда если отдыхаеш')
b28 = KeyboardButton('Нежми сюда если пидор')
b11 = KeyboardButton('Назад⬅')
user_gooo = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
user_gooo.add(b27, b28, b11)

b30 = KeyboardButton('10-15кг')
b31 = KeyboardButton('15-25кг')
b32 = KeyboardButton('25-35кг')
b33 = KeyboardButton('35-45кг')
b34 = KeyboardButton('45-55кг')
b35 = KeyboardButton('55-65кг')
b36 = KeyboardButton('65-75кг')
b37 = KeyboardButton('75-85кг')
b38 = KeyboardButton('85-95кг')
b39 = KeyboardButton('95-105кг')
b40 = KeyboardButton('105-115кг')
b41 = KeyboardButton('115-125кг')
b42 = KeyboardButton('125-135кг')
b11 = KeyboardButton('Назад⬅')
user_kg = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
user_kg.add(b30, b31, b32).add(b33, b34, b35, b36, b37, b38, b39, b40, b41, b42, b11)

b9 = KeyboardButton('Изменить имя🖊')
b10 = KeyboardButton('Изменить фамилию🖊')
b11 = KeyboardButton('Назад⬅')
b23 = KeyboardButton('ИЗМЕНИТЬ ВЕС💪')
b70 = KeyboardButton('ИЗМЕНИТЬ РОСТ💪')
user_izmeniti = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
user_izmeniti.add(b9, b10, b11, b23).row(b70)

b50 = KeyboardButton('Нажми сюда чтобы указать свой максимум в жиме лежа')


b75 = KeyboardButton('СДЕЛАЛ ПРЕХОДИМ К СЛЕДУЮЩЕМУ УПРАЖНЕНИЮ')
b76 = KeyboardButton('Я СЛАБЫЙ')
b11 = KeyboardButton('Назад⬅')
user_jim = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
user_jim.row(b75).add(b76,b11)