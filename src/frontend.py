import shutil                       
from colorama import Fore, Style
import os

def printLogo(color:str = 'white') -> None:
    supportedColors = ["BLACK", 
                       "RED", 
                       "GREEN", 
                       "YELLOW", 
                       "BLUE", 
                       "MAGENTA", 
                       "CYAN", 
                       "WHITE", 
                       "RESET", 
                       "LIGHTBLACK_EX", 
                       "LIGHTRED_EX", 
                       "LIGHTGREEN_EX", 
                       "LIGHTYELLOW_EX", 
                       "LIGHTBLUE_EX", 
                       "LIGHTMAGENTA_EX", 
                       "LIGHTCYAN_EX", 
                       "LIGHTWHITE_EX"]

    if color.upper() not in supportedColors:
        print(f"ERROR: unsupported color given, supported colors:\n{supportedColors}")
        return

    text_color = getattr(Fore, color.upper())
    logo = f"""         
        {text_color} ██████╗ ██████╗  █████╗ ███╗   ███╗███████╗██╗     ███████╗██╗   ██╗████████╗██╗  ██╗   ██████╗ {Style.RESET_ALL}
        {text_color}██╔════╝ ██╔══██╗██╔══██╗████╗ ████║██╔════╝██║     ██╔════╝██║   ██║╚══██╔══╝██║  ██║   ╚════██╗{Style.RESET_ALL}
        {text_color}██║  ███╗██████╔╝███████║██╔████╔██║███████╗██║     █████╗  ██║   ██║   ██║   ███████║    █████╔╝{Style.RESET_ALL}
        {text_color}██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║╚════██║██║     ██╔══╝  ██║   ██║   ██║   ██╔══██║   ██╔═══╝ {Style.RESET_ALL}
        {text_color}╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║███████║███████╗███████╗╚██████╔╝   ██║   ██║  ██║   ███████╗{Style.RESET_ALL}
        {text_color} ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝   ╚══════╝{Style.RESET_ALL}
        {text_color}By: MessyToilet{Style.RESET_ALL}""" 
                                                                                     
    terminal_size = shutil.get_terminal_size()
    lines = logo.split('\n')
    max_length = max(len(line) for line in lines)
    centered_lines = [(line.center(terminal_size.columns, ' ') if len(line.strip()) > 0 else ' ' * terminal_size.columns) for line in lines]
    os.system("cls")
    print('\n'.join(centered_lines))

def numberBoarder(num: str) -> str:
    return f'{Fore.YELLOW}[{Fore.GREEN}{num}{Fore.YELLOW}]{Fore.RESET}'

def systemBoarder(sys:str = 'ERROR', msg:str = None) -> str:
    if sys.upper() == 'ERROR':
        return f'\n{Fore.YELLOW}[{Fore.RED}{sys}{Fore.YELLOW}]{Fore.RESET} {msg}'
    elif sys.upper() == 'SYSTEM':
        return f'{Fore.YELLOW}[{Fore.BLUE}{sys}{Fore.YELLOW}]{Fore.RESET} {msg}' 


def options() -> str:
    while True:
        print(f'\n{numberBoarder(1)} Get user info')
        print(f'{numberBoarder(2)} Get user followers')
        print(f'{numberBoarder(3)} Get user following')

        print(f'\n{numberBoarder(4)} Get target info')
        print(f'{numberBoarder(5)} Get target followers')
        print(f'{numberBoarder(6)} Get target following')

        print(f'\n{numberBoarder(7)} Quit')
        
        try:
            if (output := int(input(f'\n# '))) in [x for x in range(1,8)]:
                return str(output)
            else:
                print(systemBoarder(sys='ERORR', msg='Bad Args'))
        except:
            print(systemBoarder(sys='ERORR', msg='Bad Args'))