	#1.Follow Link and Enable Less Secure Applications (If you have two factor authentication it must be removed)
	#Link: https://myaccount.google.com/lesssecureapps

	#2. Set up Enviroment variables. This is done differently for each operating system (Mac OS, Windows 10, Linux, etc.)
	#On Big Surr this is done by editing the '.zprofile' hidden file located in 'Macintosh HD/Users/[Your Name]'
	#The shortcut to reveal hidden files on Macs is Command + Shift + .
	#On a new line add 'export PERS_EMAIL = '[Your Email]' and on the next line 'export PERS_EMAILPW = [Your email PW]'
	#After saving the file, you will need to restart the terminal/IDE for these changes to be applied 

import os
import smtplib
from email.message import EmailMessage

def MessageTxt(txt):
	global msg
	msg['From'] = os.environ['PERS_EMAIL']
	msg['To'] = 'MyEmail@gmail.com'
	msg['Subject'] = 'Save Indian Farmer Receipt for [CUSTOMER_NAME]'
	msg.set_content(txt)


txt = """Date: [DATE]

Thank you for your donation of [DONATION_AMOUNT] to Save Indian Farmers received on [DONATION_DATE].\n

Save Indian Farmers is committed to addressing issues related to farmers suicides in India. Your generous
donation will help us reach our goal. For tax purposes, our Tax ID (EIN) is 45-3588545.\n

If you have any questions or comments, let us know at info@saveindianfarmers.org. We look forward to
your monetary support in future as we start work on more projects that positively change lives of farmers in
India.

With Kind Regards,

[IMAGE_INSERT_OF_SIGNATURE]

Jitendra Karkera
President
Save Indian Farmers
501 C (3) organization
http://www.saveindianfarmers.org"""


msg = EmailMessage()
MessageTxt(txt)

#with smtplib.SMTP_SSL('localhost', 1025) as smtp:
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	smtp.login(os.environ['PERS_EMAIL'],os.environ['PERS_EMAILPW'])
	smtp.send_message(msg)


