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

    dataMenu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    dataMenu.add(b1, b2)
    dataMenu.add(b3, b4)
    dataMenu.add(b5)
    return dataMenu


def search_kb() -> InlineKeyboardMarkup:
    searchMenu = InlineKeyboardMarkup(row_width=2)
    bthSomething = InlineKeyboardButton(text='Поиск', switch_inline_query_current_chat='')
    searchMenu.insert(bthSomething)
    return searchMenu


def get_inline_keyboard(exercises: list[Exercise], user: TelegramUser) -> list[InlineQueryResultArticle]:
    results = []
    for exercise in exercises:
        max_kb = InlineKeyboardMarkup(row_width=1)
        Button = InlineKeyboardButton(text='Добавить', callback_data=f'add-maximum-{exercise.id}')
        max_kb.add(Button)

        exercise_maximum = getattr(exercise.maximexercise_set.filter(user=user).last(), 'maxim', 0)

        title = f'{exercise.name}, {exercise.category.category}, {exercise_maximum}'
        results.append(
            InlineQueryResultArticle(
                id=str(exercise.id),
                title=title,
                input_message_content=InputTextMessageContent(exercise.name),
                reply_markup=max_kb
            )
        )
    return results
