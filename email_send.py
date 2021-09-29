import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

EMAIL_SEND = os.getenv('EMAIL_SENDER')
EMAIL_PASS = os.getenv('EMAIL_PASSWORD')
RECEIVER = os.getenv('MAILTRAP_RECEIVER')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_SEND, EMAIL_PASS)

    subject = 'Test email sent'
    body = 'Test email sent'

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_SEND, RECEIVER, msg)