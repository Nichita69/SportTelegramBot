from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('Дни недели')
b11 = KeyboardButton('Назад⬅')

user_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
user_kb.row(b1).add(b11)

bthRandom = KeyboardButton('Мои данные🎫')
bthOther = KeyboardButton('Другое№')
erf = KeyboardButton('Мои Силовые')

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(bthRandom, bthOther,erf)

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
b28 = KeyboardButton('Нежми сюда если ')
b11 = KeyboardButton('Назад⬅')
user_gooo = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
user_gooo.add(b27, b28, b11)



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

b7 = KeyboardButton(f'Теперь укажите максимуум в жиме лежа')
b5 = KeyboardButton(f'Укажите максимум в жиме гантелей')
b88 = KeyboardButton(f'Укажите максимум в отжимании на брусьях с весом')
b8 = KeyboardButton('Назад⬅')

dataa_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
dataa_kb.add(b5, b7, b8,b88)


b100 = KeyboardButton('Chest and Triceps')
b101 = KeyboardButton('Brush and Fingers')
b102 = KeyboardButton('Biceps and Back')
b103 = KeyboardButton('Arm Training')
b104 = KeyboardButton('Legs and Shoulders')

category = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
category.add(b100, b101).add(b102,b103).row(b104)