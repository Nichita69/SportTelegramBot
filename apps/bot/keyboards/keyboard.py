from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultArticle,
    InputTextMessageContent)

from apps import exercise
from apps.exercise.models import Exercise
from apps.user.models import TelegramUser


def main_kb() -> ReplyKeyboardMarkup:
    b1 = KeyboardButton('МОИ ДАННЫЕ💪')
    b2 = KeyboardButton('МОИ СИЛЛОВЫЕ💪')
    b3 = KeyboardButton('ТРЕНИРОВКИ💪')
    mainMenu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).row(b1, b2).add(b3)
    return mainMenu


def week_days() -> ReplyKeyboardMarkup:
    b1 = KeyboardButton('Назад⬅')
    b2 = KeyboardButton('Monday')
    b3 = KeyboardButton('Tuesday')
    b4 = KeyboardButton('Wednesday')
    b5 = KeyboardButton('Thursday')
    b6 = KeyboardButton('Friday')
    b7 = KeyboardButton('Saturday')
    b8 = KeyboardButton('Sunday')
    weekMenu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    weekMenu.add(b2, b3, b4, b5, b6, b7, b8, b1)
    return weekMenu


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
