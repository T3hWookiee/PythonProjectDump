#!/usr/bin/env python3

import datetime



now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day
print('Today is {}/{}/{}'.format(month, day, year))
user_birthday = input('Please enter your date of birth in the above format: ')
print('You entered: {}'.format(user_birthday))


# making a count down.

split_birthday = user_birthday.split('/')
birthday_month = split_birthday[0]
birthday_day = split_birthday[1]
birthday_year = split_birthday[2]

countdown_month = int(birthday_month) - month
countdown_day = int(birthday_day) - day
countdown_year = int(birthday_year) - year

print('Your birthday is in {} months and {} days.'.format(countdown_month, countdown_day))



