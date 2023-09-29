from frontend import printLogo, options, systemBoarder
from backend import bot
import sys


printLogo('RED')

if len(sys.argv) >= 2:
    if sys.argv[1].upper() ==  "D":
        print(systemBoarder(sys='system', msg='Enter Dev Mode...'))
        while (option := options()):
            print()
            print(systemBoarder(sys='SYSTEM', msg='SYSTEM'))
            print(systemBoarder(sys='ERROR', msg='ERROR'))
            print(systemBoarder(sys='User', msg='USER'))
            if int(option) >= 1 and int(option) <= 3:
                if option == '1':
                    pass
                elif option == '2':
                    pass
                elif option == '3':
                    pass
            elif int(option) >= 4 and int(option) < 7:
                target = str(input(f'Target @: '))
                if option == '4':
                    pass
                elif option == '5':
                    pass
                elif option == '6':
                    pass
            elif option == "7":
                pass
            elif option == "8":
                pass 
            elif option == '9':
                pass 
            elif option == '10':
                sys.exit()      

printLogo("red")

myBot = bot()
myBot.login()

printLogo("red")

while (option := options()):
    print()
    if int(option) >= 1 and int(option) <= 3:
        if option == '1':
            myBot.get_your_info()
        elif option == '2':
            myBot.get_your_followers()
        elif option == '3':
            myBot.get_your_following()
    elif int(option) >= 4 and int(option) < 7:
        target = str(input(f'Target @: '))
        print()
        if option == '4':
            myBot.get_target_info(target)
        elif option == '5':
            myBot.get_target_followers(target)
        elif option == '6':
            myBot.get_target_following(target)
    elif option == "7":
        pass
    elif option == "8":
        pass 
    elif option == '9':
        pass 
    elif option == '10':
        myBot.quit()


       