from frontend import printLogo, options
from backend import bot
import pwinput

printLogo("Green")

username = str(input("Username: "))
password = str(input("Password: "))
myBot = bot(username=username, password=password, path="GramSleuth2\\chromedriver.exe")

myBot.login()
printLogo("Green")
options()
