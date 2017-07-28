#-*- coding: utf-8 -*-
from stack import YowsupEchoStack
from config import PHONE_NUMBER, PHONE_PASSWORD
import logging
logging.basicConfig(level=logging.DEBUG)

credentials = (PHONE_NUMBER, PHONE_PASSWORD)
stack = YowsupEchoStack(credentials)
stack.start()