from frontend import printLogo
from backend import bot
import sys
import pwinput

printLogo("red")

username = str(input("Username: "))
password = str(input("Password: "))
myBot = bot(path="GramSleuth2\\requirments\\chromedriver.exe")

myBot.login(username=username, password=password)
myBot.get_your_followers()