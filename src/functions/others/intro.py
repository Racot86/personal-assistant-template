import time
from src.tools.cls import cls
from settings import Settings
import os
from src.tools.print_at import print_at

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

dalek = """
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

"""


def intro():
    cls()
    print(dalek)
    max_x = os.get_terminal_size().columns
    max_y = os.get_terminal_size().lines
    print()
