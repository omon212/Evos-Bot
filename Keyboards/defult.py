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

phone = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("📞 Отправить номер", request_contact=True),
        ],
        [
            KeyboardButton("❌ Отмена ❌"),
            KeyboardButton("Назад 🔙")
        ]
    ],
    resize_keyboard=True
)

student = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("✅ Да"),
            KeyboardButton("❌ Нет")
        ],
        [
            KeyboardButton("❌ Отмена ❌"),
            KeyboardButton("Назад 🔙")
        ]
    ],
    resize_keyboard=True
)

status = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Очное"),
            KeyboardButton("Заочное")
        ],
        [
            KeyboardButton("Вечернее")
        ],
        [
            KeyboardButton("❌ Отмена ❌"),
            KeyboardButton("Назад 🔙")
        ],
    ],
    resize_keyboard=True
)

btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Тг каналы"),
            KeyboardButton("Наружная реклама")
        ],
        [
            KeyboardButton("OLX"),
            KeyboardButton("Вакансия ПБО")
        ],
        [
            KeyboardButton("Вакансии на ПБО"),
            KeyboardButton("Метро")
        ],
        [
            KeyboardButton("От друга"),
            KeyboardButton("Instagram")
        ],
        [
            KeyboardButton("Подъезды"),
            KeyboardButton("Автобусы")
        ]
    ],
    resize_keyboard=True
)

soglasen = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("✅ Согласен.")
        ],
        [
            KeyboardButton("❌ Отмена ❌"),
            KeyboardButton("Назад 🔙")
        ]
    ],
    resize_keyboard=True
)
soglasenns = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Отправить")
        ],
        [
            KeyboardButton("❌ Отмена ❌"),
            KeyboardButton("Назад 🔙")
        ]
    ],
    resize_keyboard=True
)


callcenter = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Чиланзарский р-н")
        ],
        [
            KeyboardButton("❌ Отмена ❌"),
            KeyboardButton("Назад 🔙")
        ]
    ],
    resize_keyboard=True
)