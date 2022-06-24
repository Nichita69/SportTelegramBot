import logging
import random

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from asgiref.sync import sync_to_async
from unsync import unsync

from .keyboards.keyboard import user_kb, mainMenu, kb_user, user_go, user_goo, user_gooo, user_kg, user_izmeniti, \
    user_jim
from .. import exercise

from ..exercise.models import Exercise
from ..user.models import TelegramUser, MaximExersise

API_TOKEN = '5497853885:AAH7HFM2zgSsXMn_qVM-DBCyz_OLVXcTphs'
logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)


class UserState(StatesGroup):
    name = State()
    family = State()
    weightt = State()
    heightt = State()
    mk_weight = State()
    bench = State()


class MaximExersiseState(StatesGroup):
    user_id = State()


# ****************КЛИЕНТСКАЯ ЧАСТЬ************


def get_user(user_id: int):
    return TelegramUser.objects.filter(chat_id=user_id).first()


def get_exercise(exercise_id: int):
    return MaximExersise.objects.filter(user_id=exercise_id).first()


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user = message.from_user

    bd_user = await sync_to_async(get_user, thread_sensitive=True)(user_id=message.from_user.id)

    if not bd_user:
        await sync_to_async(
            TelegramUser.objects.create,
            thread_sensitive=True
        )(
            chat_id=user.id,
            first_name=user.first_name,
            last_name=user.last_name
        )
        await message.reply(
            f"Hello my Friend, {user.full_name}",
            reply_markup=mainMenu
        )
    else:
        await message.reply(
            f"You are welcome, {bd_user.first_name} {bd_user.last_name}",
            reply_markup=mainMenu
        )


@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await message.reply(
        f"Мой бот это программа тренировок,мой бот может сделать программму тренеровок на несколько лет он "
        f"расчитывает все "
        f"по высокоточечным формулам и рассчитывает все по "
        f"росту и весу ",
        reply_markup=mainMenu
    )


@dp.message_handler(lambda message: message.text and 'Мои Силовые' in message.text)
async def my_date(message: types.Message):
    exercise = await sync_to_async(
      MaximExersise.objects.filter(),
        thread_sensitive=True
    )(

    )

    b20 = KeyboardButton(f'Никита ({exercise.user_id})')
    b21 = KeyboardButton('Назад⬅')
    data_kbb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    data_kbb.add(b21, b20)

    await bot.send_message(
        message.from_user.id,
        f'Firsfdt name: {exercise.user_id},\nLast namkje: {exercise.maxim}',
        reply_markup=data_kbb
    )


@dp.message_handler(lambda message: message.text and 'Никита' in message.text)
async def names_of_commands(message: types.Message, state: FSMContext):
    await MaximExersiseState.user_id.set()
    await message.answer(text='Введите ваше имя', reply_markup=mainMenu)


# @unsync
# def update_height(message):
#     user = TelegramUser.objects.get(chat_id=message.from_exercise.id)
#     user.height = message.text
#     user.save()


@dp.message_handler(lambda message: message.text and 'Мои данные🎫' in message.text)
async def my_data(message: types.Message):
    user = await sync_to_async(
        TelegramUser.objects.get,
        thread_sensitive=True
    )(
        chat_id=message.from_user.id
    )

    b1 = KeyboardButton(f'Изменить имя🖊 ({user.first_name})')
    b2 = KeyboardButton(f'Изменить фамилию🖊({user.last_name})')
    b3 = KeyboardButton(f'ИЗМЕНИТЬ ВЕС💪({user.weight})')
    b4 = KeyboardButton(f'ИЗМЕНИТЬ РОСТ💪({user.height})')
    b5 = KeyboardButton('Назад⬅')
    b6 = KeyboardButton('Тренировка')
    data_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    data_kb.add(b1, b2)
    data_kb.add(b3, b4)
    data_kb.add(b5,b6)

    await bot.send_message(
        message.from_user.id,
        f'First name: {user.first_name},\nLast name: {user.last_name},\nChat ID: {user.chat_id},\nWeight kg: {user.weight},\nHeight cm: {user.height},\nHeight cm: {user.bench}',
        reply_markup=data_kb
    )


@dp.message_handler(lambda message: message.text and 'Изменить имя🖊' in message.text)
async def name_commands(message: types.Message, state: FSMContext):
    await UserState.name.set()
    await message.answer(text='Введите ваше имя', reply_markup=mainMenu)


@unsync
def update_first_name(message):
    user = TelegramUser.objects.get(chat_id=message.from_user.id)
    user.first_name = message.text
    user.save()


@dp.message_handler(state=UserState.name)
async def def_name(message, state):
    update_first_name(message)
    await state.finish()
    await message.answer('Ваше Имя было успешно обновлено!!!!!!!')


@dp.message_handler(lambda message: message.text and 'ИЗМЕНИТЬ РОСТ💪' in message.text)
async def name_height(message: types.Message, state: FSMContext):
    await UserState.heightt.set()
    await message.answer(text='Введите Ваш Рост', reply_markup=mainMenu)


@unsync
def update_height(message):
    user = TelegramUser.objects.get(chat_id=message.from_user.id)
    user.height = message.text
    user.save()


@dp.message_handler(state=UserState.heightt)
async def height_height(message, state):
    update_height(message)
    await state.finish()
    await message.answer('Ваш Рост был успешно обновлен!!!!!!!')


@dp.message_handler(lambda message: message.text and 'ИЗМЕНИТЬ ВЕС💪' in message.text)
async def weight_go(message: types.Message, state: FSMContext):
    await UserState.weightt.set()
    await message.answer(text='Укажите ваш вес', reply_markup=mainMenu)


@unsync
def update_weight(message):
    user = TelegramUser.objects.get(chat_id=message.from_user.id)
    user.weight = message.text
    user.save()


@dp.message_handler(state=UserState.weightt)
async def process_weighting(message, state):
    update_weight(message)
    await state.finish()
    await message.answer('Ваш Вес был успешно обновлен!!!!!!!')


@dp.message_handler(lambda message: message.text and 'Изменить фамилию🖊' in message.text)
async def names_steps_with_markdown(message: types.Message, state: FSMContext):
    await UserState.family.set()
    await message.answer(f"{'<b>'}Ведите вашу фамилию {'</b>'}", parse_mode='HTML', reply_markup=mainMenu)


@unsync
def update_last_name(message):
    user = TelegramUser.objects.get(chat_id=message.from_user.id)
    user.last_name = message.text
    user.save()


@dp.message_handler(state=UserState.family)
async def proccesss_name(message, state):
    update_last_name(message)
    await state.finish()
    await message.answer(text='Ваша фамилия была успешно обновлена!!!!!!!')


@dp.message_handler(lambda message: message.text and 'Назад⬅' in message.text)
async def back_command(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        'Возвращение назад',
        reply_markup=mainMenu
    )


# @dp.message_handler(lambda message: message.text and '10-15кг' in message.text)
# async def names_step(message: types.Message, state: FSMContext):
#     if message.answer(text='ew'):
#         await bot.send_message(message.from_user.id,
#                                text='ПО ВАШЕМУ ВЕСУ И РОСТУ ВАШ РАБОЧИЙ ВЕС РАВЕН== ВАШ МАКСМУМ - 20кг', )
#     if message.answer(text='ПО ВАШЕМУ ВЕСУ И РОСТУ ВАШ РАБОЧИЙ ВЕС РАВЕН== ВАШ МАКСМУМ - 20кг'):
#         await bot.send_message(message.from_user.id,
#                                'ВАША ТРЕНИРОВКА= 4 подхода * 8 повторений * ВАШ РАБОЧИЙ ВЕС',
#                                reply_markup=user_jim)


@dp.message_handler(lambda message: message.text and 'Тренировка' in message.text)
async def name_step(message: types.Message, state: FSMContext):
    await UserState.bench.set()
    if message.answer(text='The first exersaise is bench press'):
        await bot.send_message(message.from_user.id, text='https://www.borntoworkout.com/wp-content/uploads/2017/11'
                                                          '/Incline-Bench-Press.jpg')
    if message.answer(text='https://www.borntoworkout.com/wp-content/uploads/2017/11/Incline-Bench-Press.jpg'):
        await bot.send_message(message.from_user.id, 'Теперь укажите свой максимум на раз в жиме лежа',
                               reply_markup=mainMenu)


@unsync
def update_lasted_name(message):
    user = TelegramUser.objects.get(chat_id=message.from_user.id)
    user.bench_presss = message.text
    user.save()


@dp.message_handler(state=UserState.bench)
async def put_formula(message, state):
    await state.finish()
    await message.answer(text='Сейчас составим для вас формулу !!!!!!!')


@dp.message_handler(lambda message: message.text and 'Тренировка утром' in message.text)
async def name_step(message: types.Message, state: FSMContext):
    await message.answer(text='1. пресс качат'
                              '2. т) бегит'
                              '3. турник'
                              '4. анжумания')


@dp.message_handler(lambda message: message.text and 'Тренировка вечером' in message.text)
async def name_step(message: types.Message, state: FSMContext):
    await message.answer(text=' пресс качат'
                              '2. т) бегит'
                              '3. турник'
                              '4. анжумания'
                              'Гантэбли')


@dp.message_handler(lambda message: message.text and 'Нажми сюда если отдыхаеш' in message.text)
async def name_step(message: types.Message, state: FSMContext):
    await message.answer(text='На чиле на раслабоне пивко хуярить')


@dp.message_handler(lambda message: message.text and 'Нежми сюда если' in message.text)
async def name_step(message: types.Message, state: FSMContext):
    await message.answer(text='🏳️‍🌈🏳️‍🌈🏳️‍🌈🏳️‍🌈🏳️‍🌈🏳️‍🌈🏳️‍🌈')


@dp.message_handler()
async def bot_message(message: types.Message, state: FSMContext):
    if message.text == 'Дни недели':
        await bot.send_message(message.from_user.id, 'Выберите сегодняшний день', reply_markup=kb_user)

    elif message.text == 'Другое№':
        await bot.send_message(message.from_user.id, 'Другое№', reply_markup=user_kb)

    elif message.text == 'Monday':
        await bot.send_message(message.from_user.id, f"{'<b>'}MONDAY IS THE CHEST AND TRICEPS DAY "
                                                     f"🏋🏼🤸🏽⛹🏾‍♀️🏌🏾‍♀️🤼‍♂️🤼{'</b>'}", parse_mode='HTML',
                               reply_markup=user_go)

    elif message.text == 'Thuesday':
        await bot.send_message(message.from_user.id, 'are', reply_markup=user_go)

    elif message.text == 'Wednesday':
        await bot.send_message(message.from_user.id, 'you', reply_markup=user_go)

    elif message.text == 'Thursday':
        await bot.send_message(message.from_user.id, 'I', reply_markup=user_go)

    elif message.text == 'Friday':
        await bot.send_message(message.from_user.id, 'am', reply_markup=user_go)

    elif message.text == 'Saturday':
        await bot.send_message(message.from_user.id, 'fine', reply_markup=user_go)

    elif message.text == 'Sunday':
        await bot.send_message(message.from_user.id, 'and', reply_markup=user_go)


#                    ХЕНДЛЕР ДЛЯ КИЛЛОГРАМОВ


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])


def register_handlers_clieent(dp: Dispatcher):
    dp.register_message_handler(sendd_welcome, commands=['help'])
