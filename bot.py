import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import Message, CallbackQuery

# --------------------STATE--------------------#

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from Keyboards.defult import menu, filials_btn, location, filiallar, toshkent, regions, rayonlar, yunusobod

API_TOKEN = "7042370431:AAGlrQ-fw8IhiHNNAB64FBBLG7fMluuYeGI"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())


class States(StatesGroup):
    location = State()
    name = State()
    pol = State()
    age = State()
    adress = State()
    phone = State()
    student = State()
    oqishjoyinomi = State()
    time = State()
    ishvaqt = State()
    ozbektili = State()
    rustili = State()
    ishjoyiohirgi = State()
    image = State()
    social = State()


@dp.message_handler(commands=['start'])
async def startt(message: types.Message):
    photo = open('images/evos.jpg', 'rb')
    await message.answer_photo(photo, reply_markup=menu)


@dp.message_handler(text="🏢 О компании")
async def company(message: types.Message):
    photo = open('images/kopm.jpg', 'rb')
    await message.answer_photo(photo, caption="""
Информация о компании:

Сеть ресторанов быстрого обслуживания EVOS® не стоит на месте, а постоянно растет и развивается вместе с вами и для вас! Мы расширяем свою географию и открываем новые филиалы практически каждый месяц. 
Сейчас в нашей сети насчитывается более 70 филиалов по всему Узбекистану. Поэтому мы всегда в поиске динамичных и активных людей, которые хотят стать частью нашей команды и готовы строить свою карьеру в EVOS®. 
EVOS® – это надежный бренд, которому доверяют. Работа в EVOS® – гарантия стабильного заработка и перспективы карьерного роста. 
Начни свою карьеру в EVOS® уже сейчас!    
    """)


@dp.message_handler(text="📍 Филиалы")
async def filal(message: types.Message):
    photo = open('images/filial.jpg', 'rb')
    await message.answer_photo(photo, caption="""
EVOS - крупнейшая фастфуд-компания в Узбекистане. На данный момент открыто более 70 торговых точек и современное многопрофильное производство.

Сотрудники компании это большая семья, которая развивается вместе и растет изо дня в день. Компания EVOS расширяется каждый день, сегодня нас более полутора тысяч. Стань частью нашей команды, добро пожаловать в семью EVOS!    
    """, reply_markup=filials_btn)


@dp.message_handler(text="☕️ Показать ближайший филиал")
async def pokazat(message: types.Message, state: FSMContext):
    await message.answer("Отправьте свое местоположение для определения ближайшего филиала", reply_markup=location)
    await States.location.set()


@dp.message_handler(state=States.location, content_types=types.ContentType.LOCATION)
async def locationnn(message: types.Message, state: FSMContext):
    await message.answer("""
Ташкент, улица Янги Сергели
+998712031212

<a href="https://www.google.com/maps?q=41.211752,+69.229986&ll=41.211752,+69.229986&z=16">📍 Локация</a>
Дистанция: 3.05 км    
    """)
    photo = open('images/loc.jpg', 'rb')
    await message.answer_photo(photo, caption="""
Сергелинский район, ул. Янги Сергели - 27
+998712031212

<a href="https://www.google.com/maps?q=41.222990,+69.221526&ll=41.222990,+69.221526&z=16">📍 Локация</a>
Дистанция: 3.72 км
    """)
    await message.answer("""
улица Кипчак, Ташкент
<a href="https://www.google.com/maps?q=41.203622,+69.216008&ll=41.203622,+69.216008&z=16">📍 Локация</a>
Дистанция: 4.44 км    
    """)


@dp.message_handler(text="Назад↩️", state=States.location)
async def backk(message: types.Message, state: FSMContext):
    photo = open('images/filial.jpg', 'rb')
    await message.answer_photo(photo, caption="""
EVOS - крупнейшая фастфуд-компания в Узбекистане. На данный момент открыто более 70 торговых точек и современное многопрофильное производство.

Сотрудники компании это большая семья, которая развивается вместе и растет изо дня в день. Компания EVOS расширяется каждый день, сегодня нас более полутора тысяч. Стань частью нашей команды, добро пожаловать в семью EVOS!    
                """, reply_markup=filials_btn)


@dp.message_handler(text="🏢 Головной офис")
async def offfice(message: types.Message):
    photo = open('images/ofic.jpg', 'rb')
    await message.answer_photo(photo, caption="""
Адрес:  ул. Фурката 175, 1 подъезд, 4 этаж.
Ориентир: MAKRO THE TOWER    
    """)
    await bot.send_location(message.from_user.id, 41.302196, 69.248867)


@dp.message_handler(text="г. Ташкент")
async def tashkent(message: types.Message):
    await message.answer("г. Ташкент", reply_markup=filiallar)


@dp.message_handler(text="📍 Samarqand Darvoza")
async def samarqandd(message: types.Message):
    photo = open('images/samarqand.jpg', 'rb')
    await message.answer_photo(photo, caption="""
Филиал: "Самарканд дарвоза"

Адрес: ул. Коратош, 5А    
    """)
    await bot.send_location(message.from_user.id, 41.316428, 69.230965)


@dp.message_handler(text="📍 Алайский базар")
async def alayskiy(message: types.Message):
    photo = open('images/alayskiy.jpg', 'rb')
    await message.answer_photo(photo, caption="""
Филиал: Алайский базар

Адрес: просп. Амира Темура, 42

Контакты: +998 71 203 12 12    
    """)
    await bot.send_location(message.from_user.id, 41.32, 69.282572)


@dp.message_handler(text="📍 Малика")
async def malika(message: types.Message):
    photo = open('images/malika.jpg', 'rb')
    await message.answer_photo(photo, caption="""
Филиал: Малика

Адрес: ул. Богиравон, 29

Контакты: +998 71 203 12 12    
    """)
    await bot.send_location(message.from_user.id, 41.342807, 69.264684)


@dp.message_handler(text="📍 Яхъё Гулямова, 94")
async def yahyo(message: types.Message):
    photo = open('images/yahyo.jpg', 'rb')
    await message.answer_photo(photo, caption="""
Филиал: улица Яхъё Гулямова, 94

Адрес: улица Яхъё Гулямова, 94

Контакты: +998 71 203 12 12 
    """)
    await bot.send_location(message.from_user.id, 41.304758, 69.284565)


@dp.message_handler(text="Назад ↩️")
async def backkk(message: types.Message):
    photo = open('images/evos.jpg', 'rb')
    await message.answer_photo(photo, reply_markup=menu)


@dp.message_handler(text="Назад ↩")
async def baccc(message: types.Message):
    photo = open('images/filial.jpg', 'rb')
    await message.answer_photo(photo, caption="""
EVOS - крупнейшая фастфуд-компания в Узбекистане. На данный момент открыто более 70 торговых точек и современное многопрофильное производство.

Сотрудники компании это большая семья, которая развивается вместе и растет изо дня в день. Компания EVOS расширяется каждый день, сегодня нас более полутора тысяч. Стань частью нашей команды, добро пожаловать в семью EVOS!    
            """, reply_markup=filials_btn)


@dp.message_handler(text="📱 Меню")
async def menyu(message:types.Message):
    photo = open('images/menu.jpg', 'rb')
    await message.answer_photo(photo, caption="""
<a href="https://evos.uz/">Перейти на сайт Evos</a>    
    """)
    await message.answer("""
<a href="https://www.instagram.com/evosuzbekistan/">Instagram</a>|<a href="https://t.me/cloneevos_bot">Telegram</a>|<a href="https://t.me/cloneevos_bot">Facebook</a>     
    """)


@dp.message_handler(text="🗣 Новости")
async def novosti(message:types.Message):
    await message.answer("""
Kompaniya yangiliklari
Aksiya
Yangi filiallar
Yangi tortlar va hk.    
    """)

@dp.message_handler(text="📞 Контакты/Адрес")
async def kontakt(message: types.Message):
    photo = open('images/kontakt.jpg', 'rb')
    await message.answer_photo(photo, caption="""
📍Адрес:  ул. Фурката 175, 1 подъезд, 2 этаж.
📌Ориентир: MAKRO THE TOWER

📲 Контакты: +998 71 203 12 12
    """)
    await bot.send_location(message.from_user.id, 41.302196, 69.248867)



@dp.message_handler(content_types=types.ContentType.LOCATION)
async def asdfasd(message: types.Message):
    loc = message.location
    print(loc.longitude)
    print(loc.latitude)


if __name__ == '__main__':
    from vakansiya import dp
    from callcenter import dp
    from kuryer import dp
    executor.start_polling(dp, skip_updates=True)