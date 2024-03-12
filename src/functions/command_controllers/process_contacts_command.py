from src.functions.contacts.c_create_cmd import c_create_cmd
from src.functions.contacts.c_change_cmd import c_change_cmd
from src.functions.contacts.c_show_cmd import c_show_cmd
from src.functions.contacts.c_delete_cmd import c_delete_cmd
from src.functions.contacts.c_search_cmd import c_search_cmd


def process_contacts_command(cmd):
    cmd.pop(0)

    if len(cmd) > 0:
        cmd[0] = cmd[0].lower()
        match cmd[0]:
            case 'create':
                c_create_cmd(cmd)
            case 'change':
                c_change_cmd(cmd)
            case 'show':
                c_show_cmd(cmd)
            case 'delete':
                c_delete_cmd(cmd)
            case 'search':
                c_search_cmd(cmd)
            case _:
                print('ERROR. Wrong number of parameters')

    else:
        print('ERROR. Wrong number of parameters')
