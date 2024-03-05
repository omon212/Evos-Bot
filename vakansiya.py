from bot import dp, bot
from aiogram import types
from Keyboards.defult import *
from bot import States
from aiogram.dispatcher import FSMContext

databace = {}


@dp.message_handler(text="💼 Вакансии")
async def vakansii(message: types.Message):
    await message.answer("Присоединяйтесь в команду EVOS!")
    await message.answer("📍 Выберите регион:", reply_markup=regions)


@dp.message_handler(text="Ташкент")
async def tashkent(message: types.Message):
    await message.answer("💼 Выберите интересующую Вас вакансию", reply_markup=toshkent)


@dp.message_handler(text="Универсальный сотрудник")
async def unoverss(message: types.Message):
    photo = open('images/univers.jpg', 'rb')
    await message.answer_photo(photo, caption="""
📌Возраст от 18 до 35 

🇷🇺/🇺🇿 Владение русским и узбекским языком

🕑 Свободный график(желательно)

✔️Опрятный внешний вид 

💰 Зарплата от 15000( с учетом вычета НДФЛ) тысяч сум за 1 час    
    """)
    await message.answer("Выберите район где данный момент открыты вакансии.", reply_markup=rayonlar)


@dp.message_handler(text="❌ Отмена ❌")
async def canceel(message: types.Message):
    photo = open('images/evos.jpg', 'rb')
    await message.answer_photo(photo, reply_markup=menu)


@dp.message_handler(text="Назад ⬅")
async def backkkk(message: types.Message):
    await message.answer("💼 Выберите интересующую Вас вакансию", reply_markup=toshkent)


@dp.message_handler(text="Юнусабадский р-н")
async def yusobod(message: types.Message):
    await message.answer("❇️ В каком филиале вы хотите работать?", reply_markup=yunusobod)


@dp.message_handler(text="📍 Боходир")
async def boho(message: types.Message):
    photo = open('images/boho.jpg', 'rb')
    await message.answer_photo(photo, caption="""
ул. Юнусата, 25/24    
    """)
    await bot.send_location(message.from_user.id, 41.379405, 69.305609)
    await message.answer("""
👤 Введите полное ФИО.
(пример: Иван Иванов Иванович)    
    """, reply_markup=bak)
    await States.name.set()


@dp.message_handler(state=States.name)
async def nameee(message: types.Message, state: FSMContext):
    databace['name'] = message.text
    await message.answer("🧍‍♂️/🧍‍♀️ Выберите пол:", reply_markup=pol)
    await state.finish()
    await States.pol.set()


@dp.message_handler(state=States.pol)
async def pooll(message: types.Message, state: FSMContext):
    databace['pol'] = message.text
    await message.answer("📅 Укажите дату своего рождения (пример, 18.03.1995):", reply_markup=bak)
    await state.finish()
    await States.age.set()


@dp.message_handler(state=States.age)
async def agee(message: types.Message, state: FSMContext):
    data = message.text

    if len(data) == 10:
        databace['age'] = data
        await message.answer("🏠 Адрес проживания (Район, улица/квартал, дом, квартира):",reply_markup=bak)
        await state.finish()
        await States
    else:
        await message.answer("📅 Укажите дату своего рождения (пример, 18.03.1995):", reply_markup=bak)
        await States.age.set()



@dp.message_handler(text="❌ Отмена ❌", state="*")
async def caccc(message: types.Message):
    photo = open('images/evos.jpg', 'rb')
    await message.answer_photo(photo, reply_markup=menu)
