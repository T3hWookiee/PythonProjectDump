#!/usr/bin/env python3

import yaml
import argparse
from argparse import ArgumentParser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = 'Free Cruise'
email = ''
password = ''
message_to_send = "Hello, Would you be interested in a free Jamaica Cruise? Just respond to the following for your" \
                  "chance to win:" \
                  " 1. Mothers maiden name " \
                  " 2. pets name " \
                  " 3. Road where you grew up " \
                  " 4. First concert "


def phone_target():

    phone_prov = ['@mms.alltelwireless.com', '@mms.att.net', '@mms.cricketwireless.net', '@msg.fi.google.com',
                  '@pm.sprint.com', '@tmomail.net', '@mms.uscc.net', '@vzwpix.com', '@text.republicwireless.com',
                  '@mymetropcs.com']

    parser = ArgumentParser()
    parser.add_argument('-i', dest='yaml_target', required=True)
    args = parser.parse_args()
    phone_list = []
    try:
        with open(args.yaml_target) as stream:
            targets_file_read = yaml.safe_load(stream)
            for key, value in targets_file_read.items():
                print(key, value)
                phone_list.append(value['phone'])
                print(value['phone'])
                for provider in phone_prov:
                    contact = (str(value['phone']) + provider)
                    print(contact)
                    msg = MIMEMultipart()
                    toaddr = contact
                    fromaddr = email
                    msg['From'] = fromaddr
                    msg['To'] = toaddr
                    msg['Subject'] = subject
                    body = message_to_send
                    msg.attach(MIMEText(body, 'plain'))
                    server = smtplib.SMTP(host='smtp.gmail.com', port=587, timeout=60)
                    server.starttls()
                    server.ehlo()
                    server.login(email, password)
                    text = msg.as_string()
                    server.set_debuglevel(2)
                    server.sendmail(fromaddr, toaddr, text)
                    server.quit()

    except Exception as e:
        print(e)


phone_target()
