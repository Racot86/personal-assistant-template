from libraries.functions.others.o_hello_cmd import o_hello_cmd
from libraries.functions.others.o_help_cmd import o_help_cmd
from libraries.functions.others.o_war_cmd import o_war_cmd
from libraries.functions.others.o_about_cmd import o_about_cmd


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
            print('Command not recognized')
