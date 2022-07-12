from aiogram.types import KeyboardButton

from apps.exercise.models import Category
from apps.user.models import TelegramUser


def get_user(user_id: int):
    return TelegramUser.objects.filter(chat_id=user_id).first()


def count_exercice_trenirovka(chat_id, exercise_id):
    user = TelegramUser.objects.get(chat_id=chat_id)
    maxim = user.maximexercise_set.filter(exercise_id=exercise_id).last()
    if not maxim:
        return 0, ''
    exercise = maxim.exercise
    url = exercise.url

    if form := exercise.formula:
        return eval(form.format(maxim.maxim)), url
    return 0, url


def get_my_maxims(maxim_exercises):
    text = str()

    for exercise in maxim_exercises:
        text += f'{exercise.exercise.name} - {exercise.maxim}\n'
    return text


def update_first_name(message):
    user = TelegramUser.objects.get(chat_id=message.from_user.id)
    user.first_name = message.text
    user.save()


def update_height(message):
    user = TelegramUser.objects.get(chat_id=message.from_user.id)
    user.height = message.text
    user.save()


def update_weight(message):
    user = TelegramUser.objects.get(chat_id=message.from_user.id)
    user.weight = message.text
    user.save()


def update_last_name(message):
    user = TelegramUser.objects.get(chat_id=message.from_user.id)
    user.last_name = message.text
    user.save()


def get_category_by_name(message) -> int:
    category = Category.objects.filter(category__icontains=message.text).first()
    if category:
        return category.id
    return 0


def week_category_urls():
    buttons = list()
    categori = Category.objects.all()
    for i in categori:
        button = KeyboardButton(text=i.category)
        buttons.append(button)
    return buttons
