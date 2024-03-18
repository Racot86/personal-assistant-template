import os
from bot.settings import Settings
from bot.src.tools.a_print import a_print
from bot.src.tools.cls import cls
from bot.settings import Settings

move_ln_up = '\033[F'
creators = ['Roman Turas', 'Viktoriia Didenko', 'Mykhailo Martyniuk', 'Mariia Svinitska', 'Hanna Dunska', 'Dmytro Mayevsky']
packages = ['colorama', 'prompt-toolkit', 'requests']
def o_about_cmd():
    term_width = os.get_terminal_size().columns
    term_height = os.get_terminal_size().lines
    logo = f"""{Settings.warning_color}   
   ▄▄▄▄         ▄▄· ▄▄▄▄▄      ▄▄▄      ▄▄▌ ▐ ▄▌ ▄ .▄      
  ██▪ ██ ▪     ▐█ ▌▪•██  ▪     ▀▄ █·    ██· █▌▐███▪▐█▪     
  ▐█· ▐█▌ ▄█▀▄ ██ ▄▄ ▐█.▪ ▄█▀▄ ▐▀▀▄     ██▪▐█▐▐▌██▀▐█ ▄█▀▄ 
  ██. ██ ▐█▌.▐▌▐███▌ ▐█▌·▐█▌.▐▌▐█•█▌    ▐█▌██▐█▌██▌▐▀▐█▌.▐▌
  ▀▀▀▀▀•  ▀█▄▀▪·▀▀▀  ▀▀▀  ▀█▄▀▪.▀  ▀     ▀▀▀▀ ▀▪▀▀▀ · ▀█▄▀▪ {Settings.end_color}"""

    a_print(logo, clear_screen=1, speed=0.001, used_colors=[Settings.success_color])
    cls()
    print(logo)
    print()
    print(f'{Settings.success_color}     Created by TimeLords12 team:{Settings.end_color}')

    for creator in creators:
        a_print(creator,prefix='            ')
    for i in range(0,6):
        print(move_ln_up,end='')
    for creator in creators:
        a_print(creator,prefix='            ', main_color=Settings.msg_color, speed = 0.001)
    print()
    print(f'{Settings.warning_color}     Used packages:{Settings.end_color}')
    for package in packages:
        print('            ' + package)
    print()
    a_print('Special thanks to GoIT Neoversity!', prefix='     ', main_color=Settings.success_color)
    print()