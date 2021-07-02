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
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.message import EmailMessage
from email.mime.text import MIMEText


def ReadEmailTemplate():
    oFile = open('EmailTemplate.txt', 'r')
    Subject = oFile.readline().strip()
    allLines = oFile.readlines()
    Body = "".join([f'<p> {x} </p>\n' for x in allLines[:4]])
    Body2 = "".join([f'<p> {x} </p>' for x in allLines[4:]])
    return [Subject, Body, Body2]


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
Body2 = txt[2]

# READ VALUES FROM CSV FILE AND RUN THROUGH THEM
allDonators = ReadCSVFile()

# CREATE EMAIL WITH THOSE VALUES
for donator in allDonators:
    print(f'Sending email to: {donator.Name} at {donator.Email}...')

    Body = Body.replace('REPLACE_DATE', donator.Date).replace('DONATION_AMOUNT', donator.Amount).replace('DONATION_DATE',
                                                                                                      donator.Date)
    msg = MIMEMultipart()
    msg['From'] = os.environ['PERS_EMAIL']
    msg['To'] = donator.Email
    msg['Subject'] = Subject.replace('CUSTOMER_NAME', donator.Name)

    BodyM = '''
    <html>
        <head></head>
        <body>
            <img src="cid:image1"
            style="width:136px; height 101px;">
            {bodytext}
            <img src="cid:image2"
            style="width:226px; height 114px;">
            {bodytext2}
        </body>
    </html>
    '''.format(bodytext=Body,bodytext2=Body2)

    msg.attach(MIMEText(BodyM, 'html'))

    file_image1 = open("topTitle.jpg", 'rb')
    file_image2 = open("sig.jpeg", 'rb')
    email_image1 = MIMEImage(file_image1.read())
    email_image2 = MIMEImage(file_image2.read())
    file_image1.close()
    file_image2.close()

    email_image1.add_header('Content-ID', '<image1>')
    msg.attach(email_image1)
    email_image2.add_header('Content-ID', '<image2>')
    msg.attach(email_image2)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(os.environ['PERS_EMAIL'], os.environ['PERS_EMAILPW'])
        smtp.sendmail(os.environ['PERS_EMAIL'], donator.Email, msg.as_string())
    exit()
smtplib.SMTP_SSL('smtp.gmail.com', 465).quit()





