#!/usr/bin/env python3



import os
import requests
import subprocess
import time
import pandas

def phish():
    #lets first grab headers to make sure they match the date
    url = 'http://data.phishtank.com/data/online-valid.csv'
    ### PLEASE ENTER A PATH ###
    path = 'ENTER PATH'
    os.chdir(path)
    request = requests.get(url)
    head = request.headers
    print(head)
    for key, value in head.items():
        if key == 'Date':
            tm = value
    print(tm)
    tyme = time.strftime('%a, %d %b %Y')
    day = time.strftime('%d')
    year = time.strftime('%Y')
    hour = time.strftime('%H')
    head, sep, tail = tm.partition(year)
    sephead = head+sep
    print(tail)
    tail = tail.lstrip(' ')
    if sephead == tyme:
        print('The report was updated today: %s' % tail)
        subprocess.check_call(['wget', url])
        subprocess.check_call(['mv', 'online-valid.csv', 'online-valid-{}-{}-{}.csv'.format(day, year, hour)])
        print('Downloading file for parsing')
        colnames = ['phish_id', 'url', 'phish_detail_url', 'submission_time', 'verified', 'verification_time', 'online',
                    'target']
        data = pandas.read_csv(path + '/online-valid-{}-{}-{}.csv'.format(day, year, hour))
        id_phish = data.phish_id.tolist()
        url_names = data.url.tolist()
        verf_time = data.verification_time.tolist()
        dict_id_url = tuple(zip(id_phish, url_names, verf_time))
        print('The below is sorted by || phish_id || urls || verified time ||')
        print(dict_id_url)
    else:
        print('The report is out of date and or hasn\'t been updated today')




phish()
