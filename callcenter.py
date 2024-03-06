
from bot import dp, bot
from aiogram import types
from Keyboards.defult import *
from bot import States
from aiogram.dispatcher import FSMContext


databace = {}
@dp.message_handler(text="Оператор call-центра")
async def callcentessr(message: types.Message):
    databace['vakansiya'] = message.text
    photo = open('images/callcenter.jpg', 'rb')
    await message.answer_photo(photo, caption="""
📌 Возраст от 18 до 35 

🇷🇺/🇺🇿 Владение русским и узбекским языком

🕑 Полная занятость

👨‍💼/👩‍💼 Опрятный внешний вид

🧑‍💻/👩‍💻 Наличие ноутбука/компьютера

Мы предоставляем:
-Официальное трудоустройство
-Питание за счет компании
-Предоставление обучения(оплачиваемая)
-Почасовая оплата труда

Период стажировки 2 недели
    """)
    await message.answer("Выберите район где данный момент открыты вакансии.",reply_markup=callcenter)




@dp.message_handler(text="Назад ⬅")
async def backkkk(message: types.Message):
    await message.answer("💼 Выберите интересующую Вас вакансию", reply_markup=toshkent)


@dp.message_handler(text="Чиланзарский р-н")
async def yusobod(message: types.Message):
    databace['region'] = message.text
    await message.answer("❇️ В каком филиале вы хотите работать?", reply_markup=yunusobod)


@dp.message_handler(text="📍 Боходир")
async def boho(message: types.Message):
    databace['filial'] = message.text
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


@dp.message_handler(text="📍Алайский")
async def boho(message: types.Message):
    databace['filial'] = message.text
    await message.answer("""
Ташкент, просп. Амира Темура, 42
    """)
    await bot.send_location(message.from_user.id, 41.320045, 69.282388)
    await message.answer("""
👤 Введите полное ФИО.
(пример: Иван Иванов Иванович)    
    """, reply_markup=bak)
    await States.name.set()


@dp.message_handler(text="📍Юнусабад")
async def boho(message: types.Message):
    databace['filial'] = message.text
    await message.answer("""
улица Майкурган, 11B, Ташкент
    """)
    await bot.send_location(message.from_user.id, 41.360131, 69.277341)
    await message.answer("""
👤 Введите полное ФИО.
(пример: Иван Иванов Иванович)    
    """, reply_markup=bak)
    await States.name.set()

@dp.message_handler(text="📍Универсам")
async def boho(message: types.Message):
    databace['filial'] = message.text
    await message.answer("""
Юнусабадский район, 4 квартал, ул. Ахмад Дониша, 1 дом
    """)
    await bot.send_location(message.from_user.id,41.364632, 69.28619)
    await message.answer("""
👤 Введите полное ФИО.
(пример: Иван Иванов Иванович)    
    """, reply_markup=bak)
    await States.name.set()


@dp.message_handler(text="Назад 🔙")
async def backkksdsd(message:types.Message):
    photo = open('images/univers.jpg', 'rb')
    await message.answer_photo(photo, caption="""
📌Возраст от 18 до 35 

🇷🇺/🇺🇿 Владение русским и узбекским языком

🕑 Свободный график(желательно)

✔️Опрятный внешний вид 

💰 Зарплата от 15000( с учетом вычета НДФЛ) тысяч сум за 1 час    
        """)
    await message.answer("Выберите район где данный момент открыты вакансии.", reply_markup=rayonlar)


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
        await message.answer("🏠 Адрес проживания (Район, улица/квартал, дом, квартира):", reply_markup=bak)
        await state.finish()
        await States.adress.set()
    else:
        await message.answer("📅 Укажите дату своего рождения (пример, 18.03.1995):", reply_markup=bak)
        await States.age.set()


@dp.message_handler(state=States.adress)
async def adresss(message: types.Message, state: FSMContext):
    databace['adress'] = message.text
    await message.answer("📱 Укажите Ваш контактный номер телефона (пример: +998XXXXXXXXX)", reply_markup=phone)
    await state.finish()
    await States.phone.set()


@dp.message_handler(state=States.phone, content_types=types.ContentType.CONTACT)
async def phonee(message: types.Message, state: FSMContext):
    databace['phone'] = message.contact.phone_number
    await message.answer("👨‍🎓 Являетесь ли вы студентом?", reply_markup=student)
    await state.finish()
    await States.student.set()


@dp.message_handler(state=States.student)
async def studentt(message: types.Message, state: FSMContext):
    databace['student'] = message.text
    await message.answer("🏢 Введите название учебного заведения", reply_markup=bak, parse_mode=None)
    await state.finish()
    await States.oqishjoyinomi.set()



@dp.message_handler(state=States.oqishjoyinomi)
async def oqishjoyino(message: types.Message, state: FSMContext):
    databace['oqishjoyinomi'] = message.text
    await message.answer("Укажите форму обучения", reply_markup=status)
    await state.finish()
    await States.time.set()


@dp.message_handler(state=States.time)
async def timeeee(message: types.Message, state: FSMContext):
    databace['timework'] = message.text
    await message.answer("""
🕜 Введите время начала и конца занятий

Например: 08:30-12:50 или 13:30-17:10    
    """, reply_markup=bak)
    await state.finish()
    await States.ishvaqt.set()


@dp.message_handler(state=States.ishvaqt)
async def ishvaqtt(message: types.Message, state: FSMContext):
    databace['ishvaqt'] = message.text
    await message.answer("🇺🇿 Уровень знания узбекского языка", reply_markup=status)
    await state.finish()
    await States.ozbektili.set()


@dp.message_handler(state=States.ozbektili)
async def ishvaqtt(message: types.Message, state: FSMContext):
    databace['ozbektili'] = message.text
    await message.answer("🇷🇺 Уровень знания русского языка", reply_markup=status)
    await state.finish()
    await States.rustili.set()


@dp.message_handler(state=States.rustili)
async def rustilii(message: types.Message, state: FSMContext):
    databace['rustili'] = message.text
    await message.answer("""
Введите названию Вашего последнего места работы:
Период, занимаемая должность и причина увольнения

Например: Dream chase Company, Менеджер по продажам, за низкой ЗП    
    """, reply_markup=bak)
    await state.finish()
    await States.ishjoyiohirgi.set()


@dp.message_handler(state=States.ishjoyiohirgi)
async def ishjoyiohirigiii(message: types.Message, state: FSMContext):
    databace['ishjoyiohirgi'] = message.text
    await message.answer("""
🤵 Отправьте ваше фото (можно селфи с телефона)    
    """)
    await state.finish()
    await States.image.set()


@dp.message_handler(content_types=types.ContentType.PHOTO, state=States.image)
async def photoo(message: types.Message, state: FSMContext):
    databace['image'] = f"{message.from_user.first_name}.jpg"
    await message.answer("""
❓ Как Вы узнали о вакансии? 
Выберите один из вариантов, если нет правильного ответа выбери вариант "другое".    
    """, reply_markup=btn)
    await state.finish()
    await States.social.set()


@dp.message_handler(state=States.social)
async def sociall(message: types.Message, state: FSMContext):
    databace['social'] = message.text
    await message.answer("Я соглашаюсь на сбор и обработку моих персональных данных", reply_markup=soglasen)
    await state.finish()


@dp.message_handler(text="✅ Согласен.")
async def soglasennn(message: types.Message):
    await message.answer(f"""
Регион: {databace['shaxar']}
💼 Вакансия: {databace['vakansiya']}
Район: { databace['region'] }
Выбор филиала: {databace['filial']}
👤 ФИО: {databace['name']}
Пол: {databace['pol']}
📅 Дата рождения: {databace['age']}
🏠 Адрес: {databace['adress']}
📱 Контакт:  {databace['phone']}
Являетесь ли вы студентом?: {databace['student']}
Названия учебного заведения: {databace['oqishjoyinomi']}
Форма обучения: {databace['timework']}
время начала и конца занятий: {databace['ishvaqt']}
Уровень узбекского языка: {databace['ozbektili']}
Уровень русского языка: {databace['rustili']}
Название последний место работы: {databace['ishjoyiohirgi']}
Главное фото: {databace['image']}
Источники: {databace['social']}
Персональные данные: ✅ Согласен.    
    """)
    await message.answer("✅ Подтверждаете ли вы что все данные были правильно заполнено?", reply_markup=soglasenns)


@dp.message_handler(text="Отправить")
async def send(message: types.Message):
    await message.answer("""
Благодарим Вас.
Вы включены в список кандидатов на рассмотрение.
Если вы хотите сдать анкету на другую вакансию, нажмите на раздел Вакансии.    
    """, reply_markup=menu)