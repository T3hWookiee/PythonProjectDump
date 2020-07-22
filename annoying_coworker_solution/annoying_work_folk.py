#!/usr/bin/env python3

# Python script to get out of awkward social work situations.
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


#NOTE: When entering a phone number for this script, use dashes. Example: 443-123-1234

def friends_to_call():
    message_to_send = 'friends, Please call my phone. I am stuck in a conversation that won\'t end'
    phone_prov = ['@mms.alltelwireless.com', '@mms.att.net', '@mms.cricketwireless.net', '@msg.fi.google.com',
                  '@pm.sprint.com', '@tmomail.net', '@mms.uscc.net', '@vzwpix.com', '@text.republicwireless.com',
                  '@mymetropcs.com']
    contact = {'Friend1_name': 'Phone number', 'Friend2_name': 'Phone number2', 'Friend3_name': 'Phone number3'}
    for phone_parse in contact.values():
        nodash = phone_parse.replace('-','')
        for provider in phone_prov:
            contact_1 = nodash + provider
            toaddr = contact_1
            msg = MIMEMultipart()
            fromaddr = "EMAIL ADDRESS"
            msg['From'] = fromaddr
            msg['To'] = toaddr
            msg['Subject'] = 'SUBJECT LINE'
            body = (message_to_send)
            msg.attach(MIMEText(body, 'plain'))
            server = smtplib.SMTP(host='smtp.gmail.com', port=587, timeout=60)
            server.starttls()
            server.ehlo()
            server.login('EMAIL LOGIN', "PASSWORD")
            text = msg.as_string()
            server.set_debuglevel(2)
            server.sendmail(fromaddr, toaddr, text)
            server.quit()

friends_to_call()
