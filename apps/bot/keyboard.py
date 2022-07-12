from aiogram import types
from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultArticle,
    InputTextMessageContent)
from asgiref.sync import sync_to_async

from apps.exercise.models import Exercise, MaximExercise, Category
from apps.user.models import TelegramUser


def main_kb() -> ReplyKeyboardMarkup:
    b1 = KeyboardButton('МОИ ДАННЫЕ💪')
    b2 = KeyboardButton('МОИ СИЛЛОВЫЕ💪')
    b3 = KeyboardButton('ПРОГРАММА ТРЕНИРОВОК💪')
    b4 = KeyboardButton('ТВОЯ ТРЕНИРОВКА🍼')

    mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).row(b1, b2).add(b3, b4)
    return mainMenu


def week_days() -> ReplyKeyboardMarkup:
    b1 = KeyboardButton('Назад⬅')
    b2 = KeyboardButton('Понедельник🏆')
    b3 = KeyboardButton('Вторник🏆')
    b4 = KeyboardButton('Среда🏆')
    b5 = KeyboardButton('Четверг🏆')
    b6 = KeyboardButton('Пятница🏆')
    b7 = KeyboardButton('Суботта🏆')
    b8 = KeyboardButton('Воскресенье🏖')
    weekMenu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    weekMenu.add(b2, b3, b4, b5, b6, b7, b8, b1)
    return weekMenu


def week_categoryes(buttons) -> ReplyKeyboardMarkup:
    b1 = KeyboardButton('Назад⬅')
    weekcateg = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    buttons.append(b1)

    buttons_per_row = 3
    rows = list()
    row = set()
    for item in buttons:
        if len(row) == buttons_per_row:
            rows.append(row)
            row = set()
        row.add(item)
    if row:
        rows.append(row)

    for row in rows:
        weekcateg.row(*row)
    return weekcateg


def user_redact(user: TelegramUser) -> ReplyKeyboardMarkup:
    b1 = KeyboardButton(f'ИЗМЕНИТЬ ИМЯ💼 ({user.first_name})')
    b2 = KeyboardButton(f'ИЗМЕНИТЬ ФАМИЛИЮ💼({user.last_name})')
    b3 = KeyboardButton(f'ИЗМЕНИТЬ ВЕС💼({user.weight})')
    b4 = KeyboardButton(f'ИЗМЕНИТЬ РОСТ💼({user.height})')
    b5 = KeyboardButton('Назад⬅')

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


def add_maxim_kb(exercise_id: int) -> InlineKeyboardMarkup:
    addMaximMenu = InlineKeyboardMarkup(row_width=2)
    bt1 = InlineKeyboardButton(text='Добавить', callback_data=f'add-maximum-{exercise_id}')
    addMaximMenu.insert(bt1)
    return addMaximMenu


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


def get_exercise_keyboard(category_id):
    exercises = Exercise.objects.filter(category_id=category_id)
    keyboard = types.InlineKeyboardMarkup()
    for exercise in exercises:
        keyboard.add(types.InlineKeyboardButton(text=exercise.name, callback_data=f'work-day-{exercise.id}'))
    return keyboard


def save_maxim(user_id: int, exercise_id: int, maxim: int):
    obj, created = MaximExercise.objects.update_or_create(
        user_id=user_id,
        exercise_id=exercise_id,
        defaults={'maxim': maxim},
    )
    return obj
