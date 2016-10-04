from stack import YowsupEchoStack
from config import PHONE_NUMBER, PHONE_PASSWORD

credentials = (PHONE_NUMBER, PHONE_PASSWORD)
stack = YowsupEchoStack(credentials)
stack.start()