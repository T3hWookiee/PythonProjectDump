#!/usr/bin/env python3


#Weather data gathered from: https://openweathermap.org/
# YOU WILL NEED TO GENERATE A FREE API CODE FOR THIS TO WORK:

import requests
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def general():
    api_input = input('What is your API key? ')
    api_key = api_input
    current(api_key)


#lets try to get current forecast via ZIP

def current(api_key):
    # Enter phone number with -
    #example 123-123-1234
    phone_number = '123-123-1234'
    phone_parse = phone_number.replace('-','')
    zip_input = input('Please provide your zip code. ')
    zip_check = input('You entered %s. Is this correct? (Yes/No) '% zip_input).lower()
    if zip_check == 'yes':
        try:
            request = requests.get('http://api.openweathermap.org/data/2.5/weather?zip={}&APPID={}'.format(zip_input, api_key))
            if request.status_code == 200:
                parse = request.json()
                print(parse)
            elif request.status_code == 401:
                sys.exit('API_Key might be broken')
            elif request.status_code == 400:
                sys.exit('Bad request')
            elif request.status_code == 403:
                sys.exit('Forbidden')
            elif request.status_code == 404:
                sys.exit('Resource you tried to access was not found on the server')
        except Exception as err:
            print(err)
    elif zip_check == 'no':
        current(api_key)
    else:
        print('The information you entered for zip code was not valid. Try again')
        current(api_key)
    #
    # Lets parse the data.
    description = parse['weather'][0]['description']
    location = parse['name'] + ',' + parse['sys']['country']
    wind = parse['wind']
    wind_speed = wind[list(wind)[0]]
    print(description)
    print(location)
    print('wind speed: %s' % wind_speed)
    phone_prov = ['@mms.alltelwireless.com', '@mms.att.net', '@mms.cricketwireless.net', '@msg.fi.google.com',
                  '@pm.sprint.com', '@tmomail.net', '@mms.uscc.net', '@vzwpix.com', '@text.republicwireless.com'
                  '@mymetropcs.com']
    fromaddr = "Weather Guy"
    for provider in phone_prov:
        contact = phone_parse + provider
        toaddr = ('%s' % contact)
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = 'Daily Weather Update'
        body = ('Description: {}  \n Wind speed: {}  \n location: {}'.format(description, wind_speed, location))
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP(host='smtp.gmail.com', port=587, timeout=60)
        server.starttls()
        server.ehlo()
        server.login('EMAIL', "Password")
        text = msg.as_string()
        server.set_debuglevel(2)
        server.sendmail(fromaddr, toaddr, text)
        server.quit()





general()
