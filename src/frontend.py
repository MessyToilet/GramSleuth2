import shutil                       
from colorama import Fore, Style
import os

def printLogo(color:str = 'white'):
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
        

    text_color = getattr(Fore, color.upper())
    logo = f"""         
        {text_color} ██████╗ ██████╗  █████╗ ███╗   ███╗███████╗██╗     ███████╗██╗   ██╗████████╗██╗  ██╗   ██████╗ {Style.RESET_ALL}
        {text_color}██╔════╝ ██╔══██╗██╔══██╗████╗ ████║██╔════╝██║     ██╔════╝██║   ██║╚══██╔══╝██║  ██║   ╚════██╗{Style.RESET_ALL}
        {text_color}██║  ███╗██████╔╝███████║██╔████╔██║███████╗██║     █████╗  ██║   ██║   ██║   ███████║    █████╔╝{Style.RESET_ALL}
        {text_color}██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║╚════██║██║     ██╔══╝  ██║   ██║   ██║   ██╔══██║   ██╔═══╝ {Style.RESET_ALL}
        {text_color}╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║███████║███████╗███████╗╚██████╔╝   ██║   ██║  ██║   ███████╗{Style.RESET_ALL}
        {text_color} ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝   ╚══════╝{Style.RESET_ALL}
        {text_color}By: MessyToilet x Raeeceip{Style.RESET_ALL}""" 
                                                                                     
    terminal_size = shutil.get_terminal_size()
    lines = logo.split('\n')
    max_length = max(len(line) for line in lines)
    centered_lines = [(line.center(terminal_size.columns, ' ') if len(line.strip()) > 0 else ' ' * terminal_size.columns) for line in lines]
    os.system("cls")
    print('\n'.join(centered_lines))
    

def numberBoarder(num: str) -> str:
    return f'{Fore.YELLOW}[{Fore.GREEN}{num}{Fore.YELLOW}]{Fore.RESET}'

def systemBoarder(sys:str, msg:str) -> str: #MAY CAUSE PROBLEMS!! (COULD CAUSE PRINT NONE)
    if sys.upper() == 'ERROR':
        print(f'{Fore.YELLOW}[{Fore.RED}{sys.upper()}{Fore.YELLOW}]{Fore.RESET}  {msg}')
    
    elif sys.upper() == 'SYSTEM':
        print(f'{Fore.YELLOW}[{Fore.BLUE}{sys.upper()}{Fore.YELLOW}]{Fore.RESET} {msg}')
   
    elif sys.upper() == "USER":
        return(f'\n{Fore.YELLOW}[{Fore.CYAN}{sys.upper()}{Fore.YELLOW}]{Fore.RESET}   {msg}')
        

def options() -> str:
    while True:
        '''
        print(f'\n{numberBoarder(1)} Get user info')
        print(f'{numberBoarder(2)} Get user followers')
        print(f'{numberBoarder(3)} Get user following')

        print(f'\n{numberBoarder(4)} Get target info')
        print(f'{numberBoarder(5)} Get target followers')
        print(f'{numberBoarder(6)} Get target following')

        print(f'\n{numberBoarder(7)} Save to file')
        print(f'{numberBoarder(8)} Settings') #clear history, color, windowed/window-less
        print(f'{numberBoarder(9)} Help') 
        print(f'{numberBoarder(10)} Quit')
        '''
        print(f'\n{numberBoarder(1)} Get user info', end='\t\t')
        print(f'{numberBoarder(4)} Get target info', end='\t\t')
        print(f'{numberBoarder(7)} Save to file', end='\t')
        print(f'{numberBoarder(10)} Quit')

        print(f'{numberBoarder(2)} Get user followers', end='\t\t')
        print(f'{numberBoarder(5)} Get target followers', end='\t')
        print(f'{numberBoarder(8)} Settings') #clear history, color, windowed/window-less

        print(f'{numberBoarder(3)} Get user following', end="\t\t")
        print(f'{numberBoarder(6)} Get target following', end='\t')
        print(f'{numberBoarder(9)} Help') 

        

        try:
            print(f'{systemBoarder(sys="user", msg=">>>")}', end="")
            if (output := int(input(f' '))) in [x for x in range(1,11)]:
                return str(output)
            else:
                systemBoarder(sys='ERORR', msg='Bad Args')  #Do i need this?
        except:
            systemBoarder(sys='ERORR', msg='Bad Args')