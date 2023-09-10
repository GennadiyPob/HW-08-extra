from datetime import date, timedelta

def get_birthdays_per_week(users):
    # Визначаємо сьогоднішню дату і рік
    today = date.today()
    current_year = today.year
    
    # Створюємо словник для днів тижня
    days_of_week = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }

    # Створюємо порожні словники для кожного дня тижня 
    birthdays_this_week = {day: [] for day in days_of_week.values()}   #поточний тиждень
    print('birthdays_this_week = ', birthdays_this_week)
    birthdays_next_week = {day: [] for day in days_of_week.values()}   #наступний тиждень
    print('birthdays_next_week = ', birthdays_next_week)

    # Ітеруємося по користувачах та їх днях народження
    for user in users:
        name = user['name']
        birthday = user['birthday']
        
        # Перевіряємо, чи день народження вже минув цього року
        birthday_this_year = birthday.replace(year=current_year)
        if birthday.month == 1:
            birthday_this_year = birthday.replace(year=current_year + 1)
        else:
            birthday_this_year = birthday.replace(year=current_year)
        
        if birthday_this_year < today:
            continue
        
        if birthday_this_year.weekday() >= 5:
            # Якщо день народження випав на вихідний, то відображаємо його в понеділок
            birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))


        # Визначаємо день тижня для дня народження
        day_of_week = birthday.weekday()
        
        birthdays_next_week[days_of_week[day_of_week]].append(name)

        # # Додаємо користувача до відповідного словника
        # # Якщо день дня народження більший або дорівнює сьогоднішньому та менше 
        # if today.weekday() <= day_of_week < (today + timedelta(days=7)).weekday():
        #     birthdays_this_week[days_of_week[day_of_week]].append(name)
            
        # else:
        #     birthdays_next_week[days_of_week[day_of_week]].append(name)


    

    # Видаляємо пусті значення в словниках
    birthdays_this_week = {key: value for key, value in birthdays_this_week.items() if value}
    birthdays_next_week = {key: value for key, value in birthdays_next_week.items() if value}

    # Об'єднуємо обидва словники
    combined_birthdays = dict(birthdays_this_week, **birthdays_next_week)

    return combined_birthdays

# # Приклад використання



# if __name__ == "__main__":

users = [
    {"name": "Bill", "birthday": date(2023, 6, 12)},
    {"name": "Jan", "birthday": date(2023, 6, 14)},
    {"name": "Kim", "birthday": date(2023, 6, 15)},
    {"name": "Alice", "birthday": date(2023, 1, 1)}
    ]


birthdays = get_birthdays_per_week(users)
print(birthdays)
