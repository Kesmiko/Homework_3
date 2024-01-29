import datetime as dt
from datetime import datetime as dtdt
import random
import re


# Задача перша
def get_days_from_today(date):
    try:
        user_date = dtdt.strptime(date, '%Y-%m-%d')
        currently_date = dtdt.today()
        delta_days = currently_date - user_date
        result = print(f'Difference between {date} and current day is: {delta_days.days} days')
        return result
    except ValueError:
            print("Incorrect input, enter please (YYYY-MM-DD)")

get_days_from_today(date='2024-02-02')


# Задача друга
def get_numbers_ticket(min_, max_, quantity):
    list_1 = []
    if (min_ < 1 or 1 > min_ >= 1000) or (max_ < 1 or max_ > 1000) or (min_ >= max_) or quantity > (max_ - min_): 
        return []
    else: 
        while len(list_1) < quantity:
            num = random.randint(min_, max_)
            if num not in list_1: 
                list_1.append(num)      
    return sorted(list_1)

lottery_numbers = get_numbers_ticket(10, 14, 6)
print(lottery_numbers)


# Задача третя
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11    ",
    "432 11 222 22 22",
    "+123456789012"
]
def normalize_phone(phone_number):
    pattern = r'\+|\d+'
    phone_number = ''.join(re.findall(pattern, phone_number))
    if len(phone_number) == 10:
        phone_number = '+38' + phone_number
    elif len(phone_number) == 12:
        phone_number = '+' + phone_number
    elif len(phone_number) == 13:
        return phone_number
    return phone_number

sanitized_numbers = [normalize_phone(phone) for phone in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)


# Задача четверта
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.02.03"}
]

def get_upcoming_birthdays(users=None):
    today_date = dtdt.today().date()
    birthdays = [] 
    for user in users: 
        birthday_date = user["birthday"] 
        birthday_date = str(today_date.year) + birthday_date[4:] 
        birthday_date = dtdt.strptime(birthday_date, "%Y.%m.%d").date() 
        week_day = birthday_date.isoweekday() 
        days_between= (birthday_date - today_date).days 
        if 0 <= days_between < 7: 
            if week_day < 6: 
                birthdays.append({'name':user['name'], 'congratulation_date':birthday_date.strftime("%Y.%m.%d")}) 
            else:
                if (birthday_date + dt.timedelta(days = 1)).weekday() == 0:
                    birthdays.append({'name':user['name'], 'congratulation_date':(birthday_date + dt.timedelta(days = 1)).strftime("%Y.%m.%d")})
                elif (birthday_date+dt.timedelta(days = 2)).weekday() == 0: 
                    birthdays.append({'name':user['name'], 'congratulation_date':(birthday_date + dt.timedelta(days = 2)).strftime("%Y.%m.%d")})
    return birthdays

print(get_upcoming_birthdays(users))




