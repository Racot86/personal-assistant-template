import time
from src.tools.cls import cls
from settings import Settings
import os
from src.tools.print_at import print_at
import random
from colorama import Fore, Style
move_ln_up = '\033[F'
dw = '''
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣾⣷⣦⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠟⠛⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣄⠀⠀⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⣿⣿⠀⠀⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⠀⣶⣤⣀⠀⠀⠀⠀⠀
        ⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⠀⣿⣿⣿⡇⢰⣤⣀⠀
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⠀⣿⣿⣿⡇⢸⣿⣿⣿
        ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⠀⣿⣿⣿⡇⢸⣿⣿⡇
        ⢸⣿⣿⣿⣿⣿⠉⢻⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⠀⣿⣿⣿⡇⢸⣿⣿⡇
        ⢸⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⠀⣿⣿⣿⡇⢸⣿⣿⡇
        ⢸⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⠀⣿⣿⣿⡇⢸⣿⣿⡇
        ⢸⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⠀⣿⣿⣿⡇⢸⣿⣿⡇
        ⢸⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⠀⣿⣿⣿⡇⢸⣿⣿⡇
        ⢸⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⠀⣿⣿⣿⡇⢸⣿⣿⡇
        ⢸⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⠀⣿⣿⣿⡇⢸⣿⣿⡇
        ⢸⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⠀⣿⣿⣿⡇⢸⣿⣿⡇
        ⢸⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⠀⣿⣿⣿⡇⢸⣿⣿⡇
        ⢸⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⠀⣿⣿⣿⡇⢸⣿⣿⡇
        ⢸⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⠀⣿⣿⣿⡇⢸⣿⣿⡇
        ⢸⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⠀⣿⣿⣿⡇⢸⣿⣿⡇
        ⢸⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⠀⣿⣿⣿⣇⣸⣿⣿⡇
        ⢸⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣤⣿⣿⣿⣿⣿⣿⣿⡇
        ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
        ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿
    ⠀    ⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠁⠀
        ⠀⠀⠀⠀⠀⠉⠛⠿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣿⡿⠀⠀⢿⣿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀

'''

dalek = f"""{Fore.YELLOW}
        ⠀⠀⠀⠀⠀⠀⠀⣴⠛⠒⢄⢀⠀⠀⢀⣀⣀⣀⡀⠀⢀⠀⡴⠚⢳⡄⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠈⠢⢀⣴⣿⣷⡿⢋⣭⣭⣍⠻⣷⣿⣿⣦⣠⠞⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⢾⡁⠀⢈⡇⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣷⣌⣛⢞⣋⣴⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⢈⣉⣉⣉⡉⢉⣉⣉⣉⣉⣉⠉⣉⣉⣉⣉⠁⠀⠀⠀⠀⠀
        ⠀⣀⣤⣤⡀⠀⠀⠀⣾⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
        ⣼⣿⣿⣿⣿⡆⠀⠀⠿⠿⠿⠿⠇⠸⠿⠿⠿⠿⠿⠀⠿⠿⠿⠿⠇⠀⠀⠀⠀⠀
        ⢻⣿⣿⣿⣿⢷⣤⣠⣤⣤⣶⣶⣶⣶⣦⣤⣤⣴⣶⣶⣶⣶⣦⣤⣤⣠⣶⠶⠀⠀
        ⠀⠉⠉⠉⠀⠀⠈⢻⣿⣷⣤⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⢡⣴⠿⣿⠋⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⢸⣿⣤⣤⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣥⣼⣿⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⢈⣉⣉⣉⣉⠉⢉⣉⣉⣉⣉⣉⡉⢉⣉⣉⣉⣉⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⣀⣾⠟⣉⡙⢻⡆⢸⡿⢋⣉⠙⣿⡇⢸⡟⣉⣉⢻⣦⡀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⢿⣿⡘⠿⠟⣸⡇⣸⣇⠻⠿⢃⣿⡇⢸⣇⠻⠟⢠⣿⠇⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⢀⣿⡿⠒⠺⣿⠇⣿⣿⠗⠒⠿⣿⡇⢸⣿⠟⠛⢿⣿⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠰⣿⣿⢰⣿⡇⢸⠀⣿⡏⢴⣿⠆⣿⡇⢸⡇⢾⣿⠄⣿⣷⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⢹⣿⣶⣤⣴⣿⠀⣿⣿⣦⣤⣶⣿⡇⢸⣿⣦⣤⣾⣿⠁⠀⠀⠀
        ⠀⠀⠀⠀⠀⢰⣿⡟⢡⣶⡌⢿⠀⣿⡟⣠⣶⡌⣿⡇⢸⡏⢠⣶⡌⣿⣷⡄⠀⠀
        ⠀⠀⠀⠀⠀⠘⢿⣷⣌⣛⣡⣿⠀⣿⣷⣌⣋⣠⣿⡇⢸⣧⣈⣋⣡⣿⡟⠀⠀⠀
        ⠀⠀⠀⠀⠀⣠⣿⡟⢋⣍⠹⣿⠀⣿⡿⢋⣍⠙⣿⡇⢸⡿⢋⣩⡙⢿⣷⡄⠀⠀
        ⠀⠀⠀⠀⠀⢻⣿⣇⠹⠿⢁⣿⠀⣿⣧⠙⠿⢃⣿⡇⢸⣧⡘⠿⢃⣼⣿⠇⠀⠀
        ⠀⠀⠀⠀⠀⠘⠛⠛⠛⠛⠛⠛⠀⠛⠛⠛⠛⠛⠛⠃⠘⠛⠻⠿⠿⠛⠛⠀⠀⠀
        ⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦
        ⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟
{Style.RESET_ALL}
"""

dalek_defeted = f"""{Style.DIM + Fore.YELLOW}
        ⠀⠀⠀⠀⠀⠀⠀⣴⠛⠒⢄⢀⠀⠀⢀⣀⣀⣀⡀⠀⢀⠀⡴⠚⢳⡄⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠈⠢⢀⣴⣿⣷⡿⢋⣭⣭⣍⠻⣷⣿⣿⣦⣠⠞⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⢾⡁⠀⢈⡇⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣷⣌⣛⢞⣋⣴⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⢈⣉⣉⣉⡉⢉⣉⣉⣉⣉⣉⠉⣉⣉⣉⣉⠁⠀⠀⠀⠀⠀
        ⠀⣀⣤⣤⡀⠀⠀⠀⣾⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⠀⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
        ⣼⣿⣿⣿⣿⡆⠀⠀⠿⠿⠿⠿⠇⠸⠿⠿⠿⠿⠿⠀⠿⠿⠿⠿⠇⠀⠀⠀⠀⠀
        ⢻⣿⣿⣿⣿⢷⣤⣠⣤⣤⣶⣶⣶⣶⣦⣤⣤⣴⣶⣶⣶⣶⣦⣤⣤⣠⣶⠶⠀⠀
        ⠀⠉⠉⠉⠀⠀⠈⢻⣿⣷⣤⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⢡⣴⠿⣿⠋⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⢸⣿⣤⣤⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣥⣼⣿⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⢈⣉⣉⣉⣉⠉⢉⣉⣉⣉⣉⣉⡉⢉⣉⣉⣉⣉⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⣀⣾⠟⣉⡙⢻⡆⢸⡿⢋⣉⠙⣿⡇⢸⡟⣉⣉⢻⣦⡀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⢿⣿⡘⠿⠟⣸⡇⣸⣇⠻⠿⢃⣿⡇⢸⣇⠻⠟⢠⣿⠇⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⢀⣿⡿⠒⠺⣿⠇⣿⣿⠗⠒⠿⣿⡇⢸⣿⠟⠛⢿⣿⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠰⣿⣿⢰⣿⡇⢸⠀⣿⡏⢴⣿⠆⣿⡇⢸⡇⢾⣿⠄⣿⣷⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⢹⣿⣶⣤⣴⣿⠀⣿⣿⣦⣤⣶⣿⡇⢸⣿⣦⣤⣾⣿⠁⠀⠀⠀
        ⠀⠀⠀⠀⠀⢰⣿⡟⢡⣶⡌⢿⠀⣿⡟⣠⣶⡌⣿⡇⢸⡏⢠⣶⡌⣿⣷⡄⠀⠀
        ⠀⠀⠀⠀⠀⠘⢿⣷⣌⣛⣡⣿⠀⣿⣷⣌⣋⣠⣿⡇⢸⣧⣈⣋⣡⣿⡟⠀⠀⠀
        ⠀⠀⠀⠀⠀⣠⣿⡟⢋⣍⠹⣿⠀⣿⡿⢋⣍⠙⣿⡇⢸⡿⢋⣩⡙⢿⣷⡄⠀⠀
        ⠀⠀⠀⠀⠀⢻⣿⣇⠹⠿⢁⣿⠀⣿⣧⠙⠿⢃⣿⡇⢸⣧⡘⠿⢃⣼⣿⠇⠀⠀
        ⠀⠀⠀⠀⠀⠘⠛⠛⠛⠛⠛⠛⠀⠛⠛⠛⠛⠛⠛⠃⠘⠛⠻⠿⠿⠛⠛⠀⠀⠀
        ⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦
        ⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟
{Style.RESET_ALL}
"""


def intro():
    max_x = os.get_terminal_size().columns
    max_y = os.get_terminal_size().lines
    cls()
    if max_y > 20:
        print(dalek)
        count = 0
        while count < 20:
            max_x = os.get_terminal_size().columns
            max_y = os.get_terminal_size().lines
            if max_x > 0 and max_y > 0:
                random_x = random.randrange(10, 40)
                random_y = random.randrange(2, 20)
                print_at('█', random_x, random_y, Settings.error_color)
                print_at('█', random_x, random_y + 1, Settings.error_color)
                print_at('█', random_x, random_y - 1, Settings.error_color)
                print_at('█', random_x - 1, random_y, Settings.error_color)
                print_at('█', random_x + 1, random_y, Settings.error_color)
                time.sleep(0.1)
                print_at(' ', random_x, random_y, Settings.error_color)
                print_at(' ', random_x, random_y + 1, Settings.error_color)
                print_at(' ', random_x, random_y - 1, Settings.error_color)
                print_at(' ', random_x - 1, random_y, Settings.error_color)
                print_at(' ', random_x + 1, random_y, Settings.error_color)

                time.sleep(random.random()/2)
                count += 1
        cls()
        print(dalek_defeted)
        time.sleep(0.5)
        for i in range(30):
            print(move_ln_up, end='\r')

        for l in dw.splitlines():
            print(Style.DIM + Fore.CYAN + l + Style.RESET_ALL)
            time.sleep(0.05)
        cls()
        print(Style.BRIGHT + Fore.CYAN + dw + Style.RESET_ALL)
        time.sleep(0.7)
        cls()
    else:
        print(f'{Settings.warning_color}--INTRO SKIPPED DUE TO SMALL SIZE OF TERMINAL. ',end='')
        print(f'MAKE TERMINAL WINDOW LONGER FOR NEXT TIME--{Settings.end_all}')