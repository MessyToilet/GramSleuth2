from frontend import printLogo
from backend import bot
import sys
import pwinput

printLogo("red")

username = str(input("Username: "))
password = str(input("Password: "))
myBot = bot(username=username, password=password)

myBot.login()
myBot.get_your_followers()