from src.functions.others.o_hello_cmd import o_hello_cmd
from src.functions.others.o_help_cmd import o_help_cmd
from src.functions.others.o_war_cmd import o_war_cmd
from src.functions.others.o_about_cmd import o_about_cmd
from settings import Settings
from src.tools.a_print import a_print

def process_others_command(cmd):
    match cmd[0]:
        case 'hello':
            o_hello_cmd(cmd)
        case 'war':
            o_war_cmd(cmd)
        case 'help':
            o_help_cmd(cmd)
        case 'about':
            o_about_cmd()
        case _:
            a_print('Command not recognized. Doctor, check what you are typing!',
                    prefix=Settings.TARDIS,
                    main_color=Settings.warning_color)
