# 1.Follow Link and Enable Less Secure Applications (If you have two factor authentication it must be removed)
# Link: https://myaccount.google.com/lesssecureapps

# 2. Set up Enviroment variables. This is done differently for each operating system (Mac OS, Windows 10, Linux, etc.)
# On Big Surr this is done by editing the '.zprofile' hidden file located in 'Macintosh HD/Users/[Your Name]'
# The shortcut to reveal hidden files on Macs is Command + Shift + .
# On a new line add 'export PERS_EMAIL = '[Your Email]' and on the next line 'export PERS_EMAILPW = [Your email PW]'
# After saving the file, you will need to restart the terminal/IDE for these changes to be applied

import donator
import csv
import os
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText


def ReadEmailTemplate():
    oFile = open('EmailTemplate.txt', 'r')
    Subject = oFile.readline().strip()
    Body = oFile.read()
    return [Subject, Body]


def ReadCSVFile():
    with open('ExampleData.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        allDonators = []
        for line in csv_reader:
            allDonators.append(donator.Donator(*line))
    return allDonators


txt = ReadEmailTemplate()
Subject = txt[0]
Body = txt[1]

# READ VALUES FROM CSV FILE AND RUN THROUGH THEM
allDonators = ReadCSVFile()

# CREATE EMAIL WITH THOSE VALUES
for donator in allDonators:
    if donator.Name =='Name': continue
    print(f'Sending email to: {donator.Name} at {donator.Email}...')
    msg = EmailMessage()
    Body = Body.replace('REPLACE_DATE', donator.Date).replace('DONATION_AMOUNT', donator.Amount).replace('DONATION_DATE',
                                                                                                      donator.Date)
    BodyM = MIMEText(Body)
    msg.set_content(Body)
    msg['From'] = os.environ['PERS_EMAIL']
    msg['To'] = donator.Email
    msg['Subject'] = Subject.replace('CUSTOMER_NAME', donator.Name)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(os.environ['PERS_EMAIL'], os.environ['PERS_EMAILPW'])
        smtp.sendmail(os.environ['PERS_EMAIL'], donator.Email, msg.as_string())


smtplib.SMTP_SSL('smtp.gmail.com', 465).quit()





