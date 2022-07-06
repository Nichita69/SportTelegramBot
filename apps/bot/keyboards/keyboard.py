from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, \
    InlineKeyboardButton

from apps import exercise

b1 = KeyboardButton('Дни недели')
b11 = KeyboardButton('Назад⬅')

user_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
user_kb.row(b1).add(b11)

bthRandom = KeyboardButton('МОИ ДАННЫЕ💪')

erf = KeyboardButton('МОИ СИЛЛОВЫЕ💪')
hfh = KeyboardButton('ТРЕНИРОВКИ💪')

mainMenu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(bthRandom, erf).add(hfh)

b15 = KeyboardButton('Monday')
b16 = KeyboardButton('Tuesday')
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

b9 = KeyboardButton('ИЗМЕНИТЬ ИМЯ💼')
b10 = KeyboardButton('ИЗМЕНИТЬ ФАМИЛИЮ💼')
b11 = KeyboardButton('Назад⬅')
b23 = KeyboardButton('ИЗМЕНИТЬ ВЕС💼')
b70 = KeyboardButton('ИЗМЕНИТЬ РОСТ💼')
user_izmeniti = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
user_izmeniti.add(b9, b10, b11, b23).row(b70)

b50 = KeyboardButton('Нажми сюда чтобы указать свой максимум в жиме лежа')

b75 = KeyboardButton('СДЕЛАЛ ПРЕХОДИМ К СЛЕДУЮЩЕМУ УПРАЖНЕНИЮ')
b76 = KeyboardButton('Я СЛАБЫЙ')
b11 = KeyboardButton('Назад⬅')
user_jim = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
user_jim.row(b75).add(b76, b11)

b7 = KeyboardButton(f'Теперь укажите максимуум в жиме лежа')

b8 = KeyboardButton('Назад⬅')

dataa_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
dataa_kb.add(b7, b8, )

b101 = KeyboardButton('Brush and Fingers')
b102 = KeyboardButton('Biceps and Back')
b103 = KeyboardButton('Arm Training')
b104 = KeyboardButton('Legs and Shoulders')

category = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
category.add(b101).add(b102, b103).row(b104)

max_kb = InlineKeyboardMarkup(row_width=1)
Button = InlineKeyboardButton(text='Добавить', callback_data=f'add-maximum-{exercise}')

max_kb.add(Button)

minipeka = InlineKeyboardMarkup(row_width=2)
bthSomething = InlineKeyboardButton(text='Чото', switch_inline_query_current_chat='')
minipeka.insert(bthSomething)

ikb_menaiu = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='Beancdfgh_Press',
                                                               callback_data='Показать Тренировку'),
                                          InlineKeyboardButton(text='назад', callback_data='◀️Назад'),

                                      ]
                                  ])

ikb_menu = InlineKeyboardMarkup(row_width=4,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='1)Bench_Press', callback_data='1)Bench_Press'),
                                        InlineKeyboardButton(text='2)Dumbell press', callback_data='2)Dumbell_Press'),
                                        InlineKeyboardButton(text='3)Bars', callback_data='3)Bars'),
                                        InlineKeyboardButton(text='4)Elastic', callback_data='4)Elastic'),

                                    ],
                                    [

                                    ]

                                ])

fingers = InlineKeyboardMarkup(row_width=4,
                               inline_keyboard=[
                                   [
                                       InlineKeyboardButton(text='1)Elastic', callback_data='1)Elasticc'),
                                       InlineKeyboardButton(text='2)dead lifting Finger',
                                                            callback_data='2)dead lifting Finger'),
                                       InlineKeyboardButton(text='3)Block Arm', callback_data='3)Block Arm'),
                                       InlineKeyboardButton(text='4)Twisting rod', callback_data='4)Twisting rod'),
                                       InlineKeyboardButton(text='5)Luchevaia', callback_data='5)Luchevaia'),
                                   ],
                                   [

                                   ]

                               ])

# fingers = InlineKeyboardMarkup(row_width=4,
#                                inline_keyboard=[
#                                    [
#                                        InlineKeyboardButton(text='1)Elastic', callback_data='1)Elastic'),
#                                        InlineKeyboardButton(text='2)dead lifting Finger',
#                                                             callback_data='2)dead lifting Finger'),
#                                        InlineKeyboardButton(text='3)Block Arm', callback_data='3)Block Arm'),
#                                        InlineKeyboardButton(text='4)Twisting rod', callback_data='4)Twisting rod'),
#                                        InlineKeyboardButton(text='4)Luchevaia', callback_data='4)Luchevaia'),
#                                    ],
#                                    [
#
#                                    ]
#
#                                ])
