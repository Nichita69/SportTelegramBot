import logging
import random
from uuid import uuid4

import maxim
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineQueryResult, InlineQuery, InputTextMessageContent, \
    InlineQueryResultArticle, InlineKeyboardMarkup, InlineKeyboardButton
from asgiref.sync import sync_to_async
from unsync import unsync

from .keyboards.keyboard import user_kb, mainMenu, user_go, user_goo, user_gooo, user_izmeniti, \
    user_jim, dataa_kb, category, max_kb, minipeka, kb_user, ikb_menu, ikb_menaiu, fingers
from .. import exercise
from ..exercise.models import Exercise, MaximExersise
from ..user.models import TelegramUser

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
    dubbell = State()
    all_exersise = State()
    add_maxim = State()
    maxxim = State()
    work_day = State()


class MaximExersiseState(StatesGroup):
    grey = State()


# ****************КЛИЕНТСКАЯ ЧАСТЬ************


def get_user(user_id: int):
    return TelegramUser.objects.filter(chat_id=user_id).first()


def get_exercise(exercise_id: int):
    return MaximExercise.objects.filter(user_id=exercise_id).first()


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


@unsync
def update_height(message):
    user = TelegramUser.objects.get(chat_id=message.from_exercise.id)
    user.height = message.text
    user.save()


def get_all_exercise():
    return Exercise.objects.all()


def get_exercise_by_category(category_id):
    return Exercise.objects.filter(category_id=category_id)


def get_all_exersise():
    return MaximExercise.objects.all()


def get_inline_query(exercises, user):
    results = []
    for exercise in exercises:
        max_kb = InlineKeyboardMarkup(row_width=1)
        Button = InlineKeyboardButton(text='Добавить', callback_data=f'add-maximum-{exercise.id}')
        # Button = InlineKeyboardButton(text='Добавить', callback_data=f'1')
        max_kb.add(Button)
        exercise_maximum = getattr(exercise.maximexercise_set.filter(user=user).last(), 'maxim', None)
        n = exercise_maximum

        title = f'{exercise.name}, {exercise.category.category}, {n}'
        results.append(
            InlineQueryResultArticle(
                id=exercise.id,
                title=title,
                input_message_content=InputTextMessageContent(exercise.name),
                reply_markup=max_kb
            )
        )
    return results


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
        'Введите максимальную нагрузку:',
    )


def save_maxim(user_id: int, exercise_id: int, maxim: int):
    obj, created = MaximExercise.objects.update_or_create(
        user_id=user_id,
        exercise_id=exercise_id,
        defaults={'maxim': maxim},
    )
    return obj


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
    await message.answer(text='Посмотрите свои силовые ', reply_markup=mainMenu)


@dp.message_handler(lambda message: message.text and 'МОИ СИЛЛОВЫЕ💪' in message.text)
async def home_work(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        'Возвращение назад',
        reply_markup=minipeka
    )


@dp.inline_handler()
async def my_dataa(inline_query: InlineQuery):
    user = await sync_to_async(get_user, thread_sensitive=True)(user_id=inline_query.from_user.id)
    exercises = await sync_to_async(get_all_exercise, thread_sensitive=True)()
    results = list(await sync_to_async(get_inline_query, thread_sensitive=True)(exercises, user))

    await bot.answer_inline_query(inline_query_id=inline_query.id, results=results, cache_time=1)


################Моb eghf;ytybz #########################
@dp.message_handler(lambda message: message.text and 'Теперь укажите максимуум в жиме лежа' in message.text)
async def name_step(message: types.Message, state: FSMContext):
    await UserState.bench.set()
    if message.answer(text='The first exersaise is bench press'):
        await bot.send_message(message.from_user.id, text='https://www.borntoworkout.com/wp-content/uploads/2017/11'
                                                          '/Incline-Bench-Press.jpg')
    if message.answer(text='https://www.borntoworkout.com/wp-content/uploads/2017/11/Incline-Bench-Press.jpg'):
        await bot.send_message(message.from_user.id, 'Теперь укажите свой максимум на раз в жиме лежа',
                               reply_markup=mainMenu)


@unsync
def update_bench_press(message):
    user = TelegramUser.objects.get(chat_id=message.from_user.id)
    user.bench_presss = message.text
    user.save()


@dp.message_handler(state=UserState.bench)
async def put_formula(message, state):
    update_bench_press(message)
    await state.finish()
    await message.answer(text='Отлично сейчас сделаем вам тренировку')


@unsync
def update_dumbbell_presss(message):
    user = TelegramUser.objects.get(chat_id=message.from_user.id)
    user.dumbell_press = message.text
    user.save()


@dp.message_handler(state=UserState.dubbell)
async def def_dumbbell(message, state):
    update_dumbbell_presss(message)
    await state.finish()
    await message.answer('Ваше Имя было успешно обновлjено!!!!!!!')


@dp.message_handler(lambda message: message.text and 'МОИ ДАННЫЕ💪' in message.text)
async def my_data(message: types.Message):
    user = await sync_to_async(
        TelegramUser.objects.get,
        thread_sensitive=True
    )(
        chat_id=message.from_user.id
    )

    b1 = KeyboardButton(f'ИЗМЕНИТЬ ИМЯ💼 ({user.first_name})')
    b2 = KeyboardButton(f'ИЗМЕНИТЬ ФАМИЛИЮ💼({user.last_name})')
    b3 = KeyboardButton(f'ИЗМЕНИТЬ ВЕС💼({user.weight})')
    b4 = KeyboardButton(f'ИЗМЕНИТЬ РОСТ💼({user.height})')

    b6 = KeyboardButton('Назад⬅')

    data_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    data_kb.add(b1, b2)
    data_kb.add(b3, b4)
    data_kb.add(b6)

    await bot.send_message(
        message.from_user.id,
        f'First name: {user.first_name},\nLast name: {user.last_name},\nChat ID: {user.chat_id},\nWeight kg: {user.weight}'
        f',\nHeight cm: {user.height}',
        reply_markup=data_kb
    )


@dp.message_handler(lambda message: message.text and 'ИЗМЕНИТЬ ИМЯ💼' in message.text)
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
    if not message.text.isdigit():
        update_first_name(message)
        await state.finish()
        await message.answer('Ваше Имя было успешно обновлено!!!!!!!', reply_markup=mainMenu)
    else:
        await message.answer('Введите правильные данные')


@dp.message_handler(lambda message: message.text and 'ИЗМЕНИТЬ РОСТ💼' in message.text)
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
    if message.text.isdigit():
        update_height(message)
        await state.finish()
        await message.answer('Ваш Рост был успешно обновлен!!!!!!!', reply_markup=mainMenu)
    else:
        await message.answer('Ведите Правильные Данные')


@dp.message_handler(lambda message: message.text and 'ИЗМЕНИТЬ ВЕС💼' in message.text)
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
    if message.text.isdigit():
        update_weight(message)
        await state.finish()
        await message.answer('Ваш Вес был успешно обновлен!!!!!!!', reply_markup=mainMenu)
    else:
        await message.answer('Введите правильные данные!')


@dp.message_handler(lambda message: message.text and 'ИЗМЕНИТЬ ФАМИЛИЮ💼' in message.text)
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
    if not message.text.isdigit:
        update_last_name(message)
        await state.finish()
        await message.answer('Ваша фамилия была успешно обновлена!!!!!!!', reply_markup=mainMenu)
    else:
        await message.answer('Введите правильные данные!')


@dp.message_handler(lambda message: message.text and 'Назад⬅' in message.text)
async def back_command(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        'Возвращение назад',
        reply_markup=mainMenu
    )


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
def update_bench_press(message):
    user = TelegramUser.objects.get(chat_id=message.from_user.id)
    user.bench_presss = message.text
    user.save()


@dp.message_handler(state=UserState.bench)
async def put_formula(message, state):
    update_bench_press(message)
    await state.finish()
    await message.answer(text='Сейчас составим для вас формулу !!!!!!!', reply_markup=mainMenu)


@dp.message_handler(lambda message: message.text and 'ТРЕНИРОВКИ💪' in message.text)
async def names_steps_with_markdапавкown(message: types.Message, state: FSMContext):
    await message.answer(f"{'<b>'}УКАЗЫВАЙТЕ ВЕРНЫЙ ВЕС,РОСТ И МАКСИМУМ В УПРАЖНЕНИЯХ ТАК КАК ПО ЭТИМ ДАННЫМ "
                         f"СОСТАВЛЯЕТСЯ ТРЕНИРОВКА {'</b>'}", parse_mode='HTML', reply_markup=kb_user)


@dp.message_handler()
async def bot_message(message: types.Message):
    # Depend on message.text we can send different messages using match
    category_id = 0
    match message.text:
        case 'Monday':
            category_id = 1
        case 'Thursday':
            category_id = 2
        case 'Wednesday':
            category_id = 3
        case 'Tuesday':
            category_id = 4
        case 'Friday':
            category_id = 5
        case 'Saturday':
            category_id = 1
        case 'Sunday':
            category_id = 2
    if category_id != 0:
        kb = await sync_to_async(get_exercise_keyboard)(category_id)
        await bot.send_message(
            chat_id=message.from_user.id,
            text=f"Let's get exercises!",
            reply_markup=kb
        )


# @dp.callback_query_handler(lambda c: c.data.startswith('Показать Тренировку'))
# async def start_maxim(message: types.Message, state: FSMContext, exercises, user):
#     for exercise in exercises:
#         exercise_maximum = getattr(exercise.maximexersise_set.filter(user=user).last(), 'maxim', None)
#     await bot.send_message(
#         message.from_user.id,
#         'exercise_maximum',
#         reply_markup=mainMenu
#     )


#                    CHEST AND TRICEPS

@dp.callback_query_handler(lambda c: c.data.startswith('◀️Назад'))
async def go_back(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        'Возвращение назад',
        reply_markup=mainMenu
    )


@dp.callback_query_handler(lambda c: c.data.startswith('1)Bench_Press'))
async def start_maxim(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Первое упражнение это жим лежа'
                           )
    if message.answer(text='Теперь укажите свой максимум на раз в жиме лежа'):
        await bot.send_message(message.from_user.id,
                               text='https://bodybuilding-and-fitness.ru/wp-content/webp-express/webp-images/doc-root/wp-content/uploads/2020/07/zhim-lezha.jpg.webp')
    if message.answer(
            text='https://bodybuilding-and-fitness.ru/wp-content/webp-express/webp-images/doc-root/wp-content/uploads/2020/07/zhim-lezha.jpg.webp'):
        await bot.send_message(message.from_user.id, 'Теперь укажите свой максимум на раз в жиме лежа',
                               reply_markup=ikb_menaiu)


@dp.callback_query_handler(lambda c: c.data.startswith('2)Dumbell_Press'))
async def start_sdds(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Второе упражнение жим гантелей'
                           )
    if message.answer(text='Теперь укажите свой максимум на раз в жиме лежа'):
        await bot.send_message(message.from_user.id,
                               text='https://recordregion.ru/wp-content/uploads/8/1/4/814c2feb603bd2370584c7d9f12b8eec.jpeg')
    if message.answer(
            text='https://recordregion.ru/wp-content/uploads/8/1/4/814c2feb603bd2370584c7d9f12b8eec.jpeg'):
        await bot.send_message(message.from_user.id, 'Нажми сюда и мы составим формулу',
                               reply_markup=ikb_menaiu)


@dp.callback_query_handler(lambda c: c.data.startswith('3)Bars'))
async def start_sddsds(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Третье упражнение брусья с доп весом'
                           )
    if message.answer(text='Теперь укажите свой максимум на раз в жиме лежа'):
        await bot.send_message(message.from_user.id,
                               text='https://alfagym.ru/wp-content/uploads/5/f/7/5f799e907140eff78af9aceda73b2e7f.jpeg')
    if message.answer(text='https://alfagym.ru/wp-content/uploads/5/f/7/5f799e907140eff78af9aceda73b2e7f.jpeg'):
        await bot.send_message(message.from_user.id, 'Нажми сюда и мы составим формулу',
                               reply_markup=ikb_menaiu)


@dp.callback_query_handler(lambda c: c.data.startswith('4)Elastic'))
async def start_sddds(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Третье упражнение брусья с доп весом'
                           )
    if message.answer(text='Теперь укажите свой максимум на раз в жиме лежа'):
        await bot.send_message(message.from_user.id,
                               text='https://bombatelo.ru/wp-content/uploads/2017/08/Programma-trenirovki-grudi-FST-7'
                                    '-5--768x646.jpg')
    if message.answer(
            text='https://bombatelo.ru/wp-content/uploads/2017/08/Programma-trenirovki-grudi-FST-7-5--768x646.jpg'):
        await bot.send_message(message.from_user.id, 'Нажми сюда и мы составим формулу',
                               reply_markup=ikb_menaiu)


#          Brush and Fingers
@dp.callback_query_handler(lambda c: c.data.startswith('1)Elasticc'))
async def start_sddds(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Разминка Кисти и пальцев с ризиной'
                           )
    if message.answer(text='В этом упражнении нету максимума '):
        await bot.send_message(message.from_user.id,
                               text='https://tutknow.ru/uploads/posts/2016-05/1462470854_princip-vzaimosvyazi-muskulov.jpg')
    if message.answer(
            text='https://tutknow.ru/uploads/posts/2016-05/1462470854_princip-vzaimosvyazi-muskulov.jpg'):
        await bot.send_message(message.from_user.id, 'Нажми сюда и мы составим формулу',
                               reply_markup=ikb_menaiu)


@dp.callback_query_handler(lambda c: c.data.startswith('2)dead lifting Finger'))
async def start_sddds(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Становая тяга пальцами'
                           )
    if message.answer(text='В этом упражнении нету максимума '):
        await bot.send_message(message.from_user.id,
                               text='https://i.pinimg.com/originals/10/f1/e8/10f1e889c471a1b967b221bb6b4e3ec8.jpg')
    if message.answer(
            text='https://i.pinimg.com/originals/10/f1/e8/10f1e889c471a1b967b221bb6b4e3ec8.jpg'):
        await bot.send_message(message.from_user.id, 'Нажми сюда и мы составим формулу',
                               reply_markup=ikb_menaiu)


@dp.callback_query_handler(lambda c: c.data.startswith('3)Block Arm'))
async def start_sddds(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Качаем Кисти на блоке'
                           )
    if message.answer(text='В этом упражнении нету максимума '):
        await bot.send_message(message.from_user.id,
                               text='https://ru.armpower.net/img/o/8bfa35_dsc-8989net.jpg')
    if message.answer(
            text='https://ru.armpower.net/img/o/8bfa35_dsc-8989net.jpg'):
        await bot.send_message(message.from_user.id, 'Нажми сюда и мы составим формулу',
                               reply_markup=ikb_menaiu)


@dp.callback_query_handler(lambda c: c.data.startswith('4)Twisting rod'))
async def start_sddds(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Скручивания штанги на кисть'
                           )
    if message.answer(text='В этом упражнерарапрпар нету максимума '):
        await bot.send_message(message.from_user.id,
                               text='https://alfagym.ru/wp-content/uploads/7/8/c/78cc3024e79fd662e22a519dba38fe1e.jpeg')
    if message.answer(
            text='https://alfagym.ru/wp-content/uploads/7/8/c/78cc3024e79fd662e22a519dba38fe1e.jpeg'):
        await bot.send_message(message.from_user.id, 'Нажми сюда и мы составим формулу',
                               reply_markup=ikb_menaiu)


@dp.callback_query_handler(lambda c: c.data.startswith('5)Luchevaia'))
async def start_sddds(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Упражнение для плечелучевой'
                           )
    if message.answer(text='В этом упражнении нету максимума '):
        await bot.send_message(message.from_user.id,
                               text='https://avatars.mds.yandex.net/get-zen_doc/3517023/pub_5f29786a9bd10957f02e6385_5f2978a1b1ec2205d8bebdff/scale_1200')
    if message.answer(
            text='https://avatars.mds.yandex.net/get-zen_doc/3517023/pub_5f29786a9bd10957f02e6385_5f2978a1b1ec2205d8bebdff/scale_1200'):
        await bot.send_message(message.from_user.id, 'Нажми сюда и мы составим формулу',
                               reply_markup=ikb_menaiu)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])


def register_handlers_clieent(dp: Dispatcher):
    dp.register_message_handler(command_help, commands=['help'])
