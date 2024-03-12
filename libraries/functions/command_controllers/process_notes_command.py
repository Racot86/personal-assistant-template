from libraries.functions.notes.n_create_cmd import n_create_cmd
from libraries.functions.notes.n_change_cmd import n_change_cmd
from libraries.functions.notes.n_show_cmd import n_show_cmd
from libraries.functions.notes.n_delete_cmd import n_delete_cmd
from libraries.functions.notes.n_search_cmd import n_search_cmd
from libraries.functions.notes.n_filter_cmd import n_filter_cmd


def process_notes_command(cmd):
    cmd.pop(0)
    if len(cmd) > 0:
        cmd[0] = cmd[0].lower()
        match cmd[0]:
            case 'create':
                n_create_cmd(cmd)
            case 'change':
                n_change_cmd(cmd)
            case 'show':
                n_show_cmd(cmd)
            case 'delete':
                n_delete_cmd(cmd)
            case 'search':
                n_search_cmd(cmd)
            case 'filter':
                n_filter_cmd(cmd)
            case _:
                print('ERROR. Wrong number of parameters')
    else:
        print('ERROR. Wrong number of parameters')
