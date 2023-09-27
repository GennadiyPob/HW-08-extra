# Імпортуємо необхідні модулі
from datetime import date, datetime, timedelta
from collections import defaultdict

# Функція для отримання ім'ян та днів народження користувачів, які святкують їх у цей тиждень
def get_birthdays_per_week(users):
    today = date.today()                #визначаємо поточний день
    current_year = today.year           #визначаємо поточний рік

    # Створюємо словник для зберігання імен користувачів, впорядкованих за днями тижня
    birthdays_per_week = defaultdict(list)

    if users:
        for user in users:
            name = user['name']  # Отримуємо ім'я користувача
            birthday = user['birthday']  # Отримуємо день народження користувача
            birthday_this_year = birthday.replace(year=current_year)  # Встановлюємо поточний рік для дня народження

            # Якщо місяць народження - січень, то рік народження - поточний рік + 1, інакше - поточний рік
            if birthday.month == 1:
                birthday_this_year = birthday.replace(year=current_year + 1)
            else:
                birthday_this_year = birthday.replace(year=current_year)

            # Якщо день народження вже минув у поточному році, пропускаємо цього користувача
            if birthday_this_year < today:
                continue

            # Якщо день народження випав на вихідний, переміщуємо його на понеділок
            if birthday_this_year.weekday() >= 5:
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))

            day_name = birthday_this_year.strftime('%A')  # Отримуємо назву дня тижня
            birthdays_per_week[day_name].append(name)  # Додаємо ім'я до відповідного дня тижня

    else:
        return dict()  # Якщо немає користувачів, повертаємо пустий словник

    return birthdays_per_week  # Повертаємо словник з ім'ями користувачів, впорядкованими за днями тижня

if __name__ == "__main__":
    # Приклад списку користувачів
    users = [
        {"name": "Bill", "birthday": date(2023, 6, 12).date()},
        {"name": "Jan", "birthday": date(2023, 6, 14).date()},
        {"name": "Kim", "birthday": date(2023, 9, 24).date()},
        {"name": "Alice", "birthday": date(2021, 1, 1).date()}

    ]

    result = get_birthdays_per_week(users)  # Викликаємо функцію і отримуємо результат
    print(result)  # Виводимо результат

    # Виводимо імена користувачів відповідно до днів тижня
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
