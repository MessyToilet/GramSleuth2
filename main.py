from frontend import printLogo
from backend import bot
import sys
import pwinput

printLogo("blue")

username = str(input("Username: "))
password = str(input("Password: "))
myBot = bot(username=username, password=password, path="GramSleuth2\\requirments\\chromedriver.exe")

myBot.login()
input("waiting...")
myBot.get_your_followers()