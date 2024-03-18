from datetime import datetime
from src.tools.a_print import a_print
from settings import Settings

def o_hello_cmd(cmd):
    time_of_day = ''
    time = datetime.now()
    if 0 <= time.hour < 12: time_of_day = 'morning'
    if 12 <= time.hour < 18: time_of_day = 'day'
    if 18 <= time.hour <= 23: time_of_day = 'evening'

    a_print(f"Good {time_of_day}, Doctor! How are you doing today?",
            prefix=Settings.TARDIS,
            main_color=Settings.msg_color,
            )