from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

from form import BillForm

load_dotenv()

MAIL_USERNAME = os.getenv('MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
MAIL_SENDER = os.getenv('MAIL_SENDER')
MAIL_RECEIVER = ()