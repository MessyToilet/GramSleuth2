from frontend import printLogo, options
from backend import bot

printLogo("red")

myBot = bot()
myBot.login()

printLogo("red")
while (option := options()) != '3':
    if option == '1':
        myBot.get_your_followers()
    elif option == '2':
        pass
myBot.quit()