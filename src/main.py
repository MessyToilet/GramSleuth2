from src.frontend import printLogo, options, systemBoarder
from src.backend import bot

printLogo("red")


myBot = bot()
myBot.login()

printLogo("red")
while (option := options()):
    if int(option) >= 1 and int(option) <= 3:
        if option == '1':
            myBot.get_your_info()
        elif option == '2':
            myBot.get_your_followers()
        elif option == '3':
            myBot.get_your_following()
    elif int(option) >= 4 and int(option) < 7:
        target = str(input(f'Target @: '))
        if option == '4':
            myBot.get_target_info(target)
        elif option == '5':
            myBot.get_target_followers(target)
        elif option == '6':
            myBot.get_target_following(target)
    elif option == "7":
        myBot.quit()

       