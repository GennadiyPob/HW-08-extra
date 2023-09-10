from datetime import date, timedelta

def get_birthdays_per_week(users):
    # Створюємо словник для збереження ім'я користувача за кожним днем тижня
    birthday_dict = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": [],
    }

    # Перевірка наявності користувачів
    if not users:
        return birthday_dict

    # Отримуємо поточну дату
    today = date.today()

    # Цикл для кожного користувача
    for user in users:
        birthday = user["birthday"]
        name = user["name"]

        # Розраховуємо різницю між днем народження та поточною датою
        days_until_birthday = (birthday - today).days

        # Перевірка чи день народження вже минув у цьому році
        if days_until_birthday < 0:
            continue

        # Визначаємо день тижня для дня народження
        birthday_weekday = (today + timedelta(days=days_until_birthday)).strftime("%A")

        # Додаємо ім'я користувача в відповідний день тижня
        birthday_dict[birthday_weekday].append(name)

    # Перевірка випадку, коли сьогодні неділя і був вчора (субота)
    if today.strftime("%A") == "Sunday":
        yesterday = today - timedelta(days=1)
        if birthday_dict["Saturday"]:
            birthday_dict["Monday"].extend(birthday_dict["Saturday"])
            birthday_dict["Saturday"] = []

    return birthday_dict

# Приклад користувачів
users = [
    {"name": "Bill", "birthday": date(2023, 6, 27)},
    {"name": "Jan", "birthday": date(2023, 6, 28)},
    {"name": "Kim", "birthday": date(2023, 6, 29)},
]

# Виклик функції з прикладом користувачів
birthday_dict = get_birthdays_per_week(users)
print(birthday_dict)
