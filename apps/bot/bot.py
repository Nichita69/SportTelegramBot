import logging
from datetime import datetime

from asgiref.sync import sync_to_async
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import InlineQuery

from apps.bot.helpers import (
    get_user, count_exercice_trenirovka, get_my_maxims, update_first_name, update_height, update_weight,
    update_last_name, get_category_by_name)
from apps.bot.keyboard import (
    main_kb, search_kb, week_days, user_redact, get_inline_keyboard, get_exercise_keyboard, save_maxim, add_maxim_kb,
    week_categoryes
)
from apps.exercise.models import Exercise, Category
from apps.user.models import TelegramUser
from config.settings import API_TOKEN

logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)


class UserState(StatesGroup):
    first_name = State()
    last_name = State()
    weight = State()
    height = State()
    add_maxim = State()


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user = message.from_user

    bd_user = await sync_to_async(func=get_user, thread_sensitive=True)(user_id=message.from_user.id)

    if not bd_user:
        await sync_to_async(TelegramUser.objects.create, thread_sensitive=True)(
            chat_id=user.id,
            first_name=user.first_name,
            last_name=user.last_name
        )
        await message.reply(
            f"Привет мой друг,Для начала чтобы бот правильно  работал, укажи свои данные и силовые ! {user.full_name}",
            reply_markup=main_kb()
        )
    else:
        await message.reply(
            f"Давно не виделись,\n"
            f"Для начала чтобы бот правильно  работал, {bd_user.full_name} укажи свои данные и силовые !",
            reply_markup=main_kb()
        )


@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await message.reply(
        f"Мой бот это программа тренировок,мой бот может сделать программму тренеровок на несколько лет он "
        f"расчитывает все "
        f"по высокоточечным формулам и рассчитывает все по "
        f"росту и весу ",
        reply_markup=main_kb()
    )


@dp.callback_query_handler(lambda c: c.data.startswith('add-maximum'))
async def start_maxim(call: types.CallbackQuery):
    user = await sync_to_async(
        TelegramUser.objects.get,
        thread_sensitive=True
    )(
        chat_id=call.from_user.id
    )
    await UserState.add_maxim.set()
    dp.storage.data[str(call.from_user.id)][str(call.from_user.id)]['data']['exercise'] = call.data.split('-')[-1]
    await bot.send_message(
        call.from_user.id,
        'Введите ваш максимум на раз:',
    )


@dp.message_handler(lambda message: message.text.isdigit(), state=UserState.add_maxim)
async def process_age(message: types.Message, state: FSMContext):
    exercise_id = int(state.storage.data[str(message.from_user.id)][str(message.from_user.id)]['data']['exercise'])
    maxim = message.text
    bd_user = await sync_to_async(get_user, thread_sensitive=True)(user_id=message.from_user.id)
    maxim_exercise = await sync_to_async(save_maxim, thread_sensitive=True)(
        user_id=bd_user.id,
        exercise_id=exercise_id,
        maxim=int(maxim)
    )

    await state.finish()
    await message.answer(text='Посмотрите свои силовые ', reply_markup=main_kb())


@dp.message_handler(lambda message: message.text and 'МОИ СИЛЛОВЫЕ💪' in message.text)
async def home_work(message: types.Message):
    user = await sync_to_async(
        TelegramUser.objects.get,
        thread_sensitive=True
    )(
        chat_id=message.from_user.id
    )

    maxim_exercises = user.maximexercise_set.all()

    text = await sync_to_async(get_my_maxims)(maxim_exercises)

    if text:
        await bot.send_message(
            message.from_user.id,
            text,
            reply_markup=search_kb()
        )
    else:
        await bot.send_message(
            message.from_user.id,
            'Вы пока не добавили ни одного максмума!',
            reply_markup=search_kb()
        )


@dp.inline_handler()
async def my_dataa(inline_query: InlineQuery):
    user = await sync_to_async(get_user, thread_sensitive=True)(user_id=inline_query.from_user.id)
    exercises = await sync_to_async(Exercise.objects.all, thread_sensitive=True)()
    results = list(await sync_to_async(get_inline_keyboard, thread_sensitive=True)(exercises, user))

    await bot.answer_inline_query(inline_query_id=inline_query.id, results=results, cache_time=1)


@dp.message_handler(lambda message: message.text and 'ИЗМЕНИТЬ ИМЯ💼' in message.text)
async def name_commands(message: types.Message):
    await UserState.first_name.set()
    await message.answer(text='Введите ваше имя', reply_markup=main_kb())


@dp.message_handler(state=UserState.first_name)
async def def_change_name(message, state):
    if not message.text.isdigit():
        await sync_to_async(update_first_name)(message)
        await state.finish()
        await message.answer('Ваше Имя было успешно обновлено!!!!!!!', reply_markup=main_kb())
    else:
        await message.answer('Введите правильные данные')


@dp.message_handler(lambda message: message.text and 'ИЗМЕНИТЬ РОСТ💼' in message.text)
async def name_height(message: types.Message, state: FSMContext):
    await UserState.height.set()
    await message.answer(text='Введите Ваш Рост', reply_markup=main_kb())


@dp.message_handler(state=UserState.height)
async def change_height_in_databaze(message, state):
    if message.text.isdigit():
        await sync_to_async(update_height)(message)
        await state.finish()
        await message.answer('Ваш Рост был успешно обновлен!!!!!!!', reply_markup=main_kb())
    else:
        await message.answer('Ведите Правильные Данные')


@dp.message_handler(lambda message: message.text and 'ИЗМЕНИТЬ ВЕС💼' in message.text)
async def weight_change(message: types.Message, state: FSMContext):
    await UserState.weight.set()
    await message.answer(text='Укажите ваш вес', reply_markup=main_kb())


@dp.message_handler(state=UserState.weight)
async def change_your_name_in_baza_danih(message, state):
    if message.text.isdigit():
        await sync_to_async(update_weight)(message)
        await state.finish()
        await message.answer('Ваш Вес был успешно обновлен!!!!!!!', reply_markup=main_kb())
    else:
        await message.answer('Введите правильные данные!')


@dp.message_handler(lambda message: message.text and 'ИЗМЕНИТЬ ФАМИЛИЮ💼' in message.text)
async def your_last_name(message: types.Message, state: FSMContext):
    await UserState.last_name.set()
    await message.answer(f"{'<b>'}Ведите вашу фамилию {'</b>'}", parse_mode='HTML', reply_markup=main_kb())


@dp.message_handler(state=UserState.last_name)
async def change_the_last_name(message, state):
    if not message.text.isdigit():
        await sync_to_async(update_last_name)(message)
        await state.finish()
        await message.answer('Ваша фамилия была успешно обновлена!!!!!!!', reply_markup=main_kb())
    else:
        await message.answer('Введите правильные данные!')


@dp.message_handler(lambda message: message.text and 'Назад⬅' in message.text)
async def back_command(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        'Возвращение назад',
        reply_markup=main_kb()
    )


@dp.message_handler(lambda message: message.text and 'ПРОГРАММА ТРЕНИРОВОК💪' in message.text)
async def list_of_days(message: types.Message, state: FSMContext, ):
    current_dt = datetime.now().strftime("%y.%m.%d %H:%M:%S")
    c_date, c_time = current_dt.split()
    msg = f"Текущая дата: {c_date}\nТекущее время: {c_time}"
    user = message.from_user.id
    await bot.send_message(user, msg, reply_markup=week_days())


@dp.message_handler(lambda message: message.text and 'ТВОЯ ТРЕНИРОВКА🍼' in message.text)
async def back_commagnd(message: types.Message, state: FSMContext, ):
    current_dt = datetime.now().strftime("%y.%m.%d %H:%M:%S")
    c_date, c_time = current_dt.split()
    msg = f"Текущая дата: {c_date}\nТекущее время: {c_time}"
    user = message.from_user.id
    categori_kb = await sync_to_async(week_categoryes, thread_sensitive=True)()

    await bot.send_message(user, msg, reply_markup=categori_kb)


@dp.message_handler(lambda message: message.text and 'МОИ ДАННЫЕ💪' in message.text)
async def my_data(message: types.Message):
    user = await sync_to_async(TelegramUser.objects.get, thread_sensitive=True)(chat_id=message.from_user.id)

    await bot.send_message(
        message.from_user.id,
        f'Имя: {user.first_name},\n'
        f'Фамилия: {user.last_name},\n'
        f'Вес: {user.weight} кг,\n'
        f'Рост: {user.height} см',
        reply_markup=user_redact(user)
    )


@dp.callback_query_handler(lambda c: c.data.startswith('work-day'), )
async def your_trenirovka(call: types.CallbackQuery):
    exercise_id = call.data.split('-')[-1]

    number, url = await sync_to_async(count_exercice_trenirovka)(call.from_user.id, exercise_id)

    if number:
        await bot.send_message(
            call.from_user.id,
            f'Ты должен сделать 4 подхода по 10 раз с этим весом =     {number}',
        )
        await bot.send_message(
            call.from_user.id,
            f'{url}',
            reply_markup=week_categoryes()
        )
    else:
        await bot.send_message(
            call.from_user.id,
            f'Сначала добавьте свои максимумы!',
            reply_markup=add_maxim_kb(exercise_id=int(exercise_id))
        )


@dp.message_handler()
async def bot_go_to_bot(message: types.Message):
    # Depend on message.text we can send different messages using match
    category_id = 0
    match message.text:
        case 'Понедельник🏆':
            category_id = 1
        case 'Вторник🏆':
            category_id = 2
        case 'Среда🏆':
            category_id = 3
        case 'Четверг🏆':
            category_id = 4
        case 'Пятница🏆':
            category_id = 5
        case 'Суботта🏆':
            category_id = 2
        case 'Воскресенье🏖':
            category_id = 2
    if category_id == 0:
        category_id = await sync_to_async(get_category_by_name, thread_sensitive=True)(message)
    if category_id != 0:
        kb = await sync_to_async(get_exercise_keyboard)(category_id)
        await bot.send_message(
            chat_id=message.from_user.id,
            text=f"Давай приступим к упражнениям",
            reply_markup=kb
        )


@dp.callback_query_handler(lambda c: c.data.startswith('◀️Назад'))
async def go_back(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        'Возвращение назад',
        reply_markup=main_kb()
    )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])


def register_handlers_clieent(dp: Dispatcher):
    dp.register_message_handler(command_help, commands=['help'])
