from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("🏢 О компании"),
            KeyboardButton("📍 Филиалы")
        ],
        [
            KeyboardButton("💼 Вакансии")
        ],
        [
            KeyboardButton("📱 Меню"),
            KeyboardButton("🗣 Новости"),
        ],
        [
            KeyboardButton("📞 Контакты/Адрес"),
            KeyboardButton("🇺🇿/🇷🇺 Язык")

        ],
    ],
    resize_keyboard=True

)

filials_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("☕️ Показать ближайший филиал"),
        ],
        [
            KeyboardButton("🏢 Головной офис"),
            KeyboardButton("г. Ташкент"),
        ],
        [
            KeyboardButton("Назад ↩️"),
        ],
    ],
    resize_keyboard=True
)

location = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Отправить местоположение", request_location=True),
        ],
        [
            KeyboardButton(text="Назад↩️"),
        ],
    ],
    resize_keyboard=True
)

filiallar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("📍 Samarqand Darvoza"),
            KeyboardButton("📍 Алайский базар"),

        ],
        [
            KeyboardButton("📍 Малика"),
            KeyboardButton("📍 Яхъё Гулямова, 94")
        ],
        [
            KeyboardButton("Назад ↩"),
        ]
    ],
    resize_keyboard=True
)

regions = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Ташкент"),
        ],
        [
            KeyboardButton("❌ Отмена ❌"),
            KeyboardButton("Назад")
        ],
    ],
    resize_keyboard=True
)

toshkent = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Универсальный сотрудник"),
            KeyboardButton("Оператор call-центра"),
        ],
        [
            KeyboardButton("Курьер"),
        ],
        [
            KeyboardButton("❌ Отмена ❌"),
            KeyboardButton("Назад ⬅️")
        ]
    ],
    resize_keyboard=True
)

rayonlar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Юнусабадский р-н"),
            KeyboardButton("Мирзо Улугбекский р-н")
        ],
        [
            KeyboardButton("Яшнабадский р-н"),
            KeyboardButton("Яккасарский р-н")
        ],
        [
            KeyboardButton("Сергелинский р-н"),
            KeyboardButton("Чиланзарский р-н")
        ],
        [
            KeyboardButton("Мирабадский р-н"),
            KeyboardButton("Шайхонтохурский р-н")
        ],
        [
            KeyboardButton("Алмазарский р-н"),
            KeyboardButton("Бектемирский р-н")
        ],
        [
            KeyboardButton("❌ Отмена ❌"),
            KeyboardButton("Назад ⬅")
        ]
    ],
    resize_keyboard=True
)

yunusobod = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("📍 Боходир"),
            KeyboardButton("📍Алайский"),
            KeyboardButton("📍Юнусабад"),
        ],
        [
            KeyboardButton("📍Универсам")
        ],
        [
            KeyboardButton("❌ Отмена ❌"),
            KeyboardButton("Назад 🔙")
        ]
    ],
    resize_keyboard=True
)

bak = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("❌ Отмена ❌"),
            KeyboardButton("Назад 🔙")
        ]
    ],
    resize_keyboard=True
)
pol = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("👩‍🦰  Женщина"),
            KeyboardButton("👨‍🦰  Мужчина")
        ],
        [
            KeyboardButton("❌ Отмена ❌"),
            KeyboardButton("Назад 🔙")
        ]
    ],
    resize_keyboard=True
)
