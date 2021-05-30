from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from aiogram import types

from states import Testing


@dp.message_handler(Command('test'), state=None)
async def enter_test(message: types.Message):
    await message.answer("You starting to test\n Question #1\nWhat's your name?")
    await Testing.Q1.set()


@dp.message_handler(state=Testing.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    print(f"message = {message}")
    answer = message.text
    # Сохраним ответ пользователя в машину состояний
    # Это можно сделать несколькими способами
    # await state.update_data(answer1=answer) # Вариант 1
    #
    # await state.update_data(  # Вариант 2
    #     {
    #         'anwser1': answer
    #     }
    # )
    async with state.proxy() as data:
        data['answer1'] = answer

    await message.answer("You starting to test\n Question #2\nHow old are you?")
    # await Testing.next()
    await Testing.Q2.set()


@dp.message_handler(state=Testing.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    data = await state.get_data()
    answer1 = data.get('answer1')
    answer2 = message.text

    await message.answer(f"Thx for your answers!\n"
                         f"Your answers are:\n"
                         f"{answer1=}\n"
                         f"{answer2=}\n")
    print(f"logger: {answer1=}\n{answer2=}")
    # Для того чтобы пользователь не находился в состоянии ответа на вопрос 2,
    # мы должны его сбросить
    # Есть несколько вариантов как это можно реализовать:
    # Сбрасываются состояние и сбрасываются данные
    await state.finish()    # Это самый простой вариант
    # await state.reset_state()   # Также сбрасываются состояние и данные
    # await state.reset_state(with_data=False)    # Сбросит состояние, но оставит данные в state.get_data!
