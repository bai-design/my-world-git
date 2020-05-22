from datetime import datetime
from control.data import suite2data, datatodict, suite_format
from control.testcase import TestCase
from control.utils import Excel, creation_files
from control.log import logger
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from control.junit import Junit
from control.config import *
import threading
import requests
import time

class Autotest(object):
    pass
