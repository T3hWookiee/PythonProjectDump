#!/usr/bin/env python3


import time
import webbrowser
import calendar
from datetime import date


link = 'https://www.youtube.com/watch?v=kfVsfOSbJY0'
seconds = '900'

# 900 seconds = 15 minutes
# 1800 seconds = 30 minutes
# 3600 seconds = 60 minutes / 1 hour


def menu():
    print('Menu:')
    print('1. Timer')
    print('2. Upset Co-Workers')
    user_input = input('Please select a number from the above menu: ')
    if user_input == '1':
        print('You have selected: Timer.')
        th_timer()
    if user_input == '2':
        print('You have selected: upset co-worker..')
        pissed()


def th_timer():
    user_input = input('Please enter a value in seconds: ')
    user_input = int(user_input)
    while user_input >= 0:
        print(user_input)
        user_input = user_input - 1
        time.sleep(1)
        if user_input == 0:
            webbrowser.open(link)


def pissed():
    sec = int(seconds)
    mdate = date.today()
    x = (calendar.day_name[mdate.weekday()])
    if x == 'Friday':
        starttime=time.time()
        while True:
            webbrowser.open('link')
            time.sleep(sec - ((time.time() - starttime) % sec))




menu()
