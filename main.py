# importing standard & custom modules
from prompt_toolkit import prompt
from datetime import datetime
from settings import Settings
from colorama import Fore
import os

#  import classes
from libraries.classes.class_Contact import Contact
from libraries.classes.class_ContactBook import ContactBook
# importing contacts functions
from libraries.functions.contacts.c_create_cmd import c_create_cmd
from libraries.functions.contacts.c_change_cmd import c_change_cmd
from libraries.functions.contacts.c_show_cmd import c_show_cmd
from libraries.functions.contacts.c_delete_cmd import c_delete_cmd
from libraries.functions.contacts.c_search_cmd import c_search_cmd
# importing notes functions
from libraries.functions.notes.n_create_cmd import n_create_cmd
from libraries.functions.notes.n_change_cmd import n_change_cmd
from libraries.functions.notes.n_show_cmd import n_show_cmd
from libraries.functions.notes.n_delete_cmd import n_delete_cmd
from libraries.functions.notes.n_search_cmd import n_search_cmd
from libraries.functions.notes.n_filter_cmd import n_filter_cmd
# importing others functions
from libraries.functions.others.o_hello_cmd import o_hello_cmd
from libraries.functions.others.o_help_cmd import o_help_cmd
from libraries.functions.others.o_war_cmd import o_war_cmd
from libraries.functions.others.o_about_cmd import o_about_cmd
# import tools
from libraries.tools.save_contacts import save_contacts
from libraries.tools.load_contacts import load_contacts

# defining variables
move_ln_up = '\033[F'


def parse_cmd(cmd):
    cmd = cmd.strip()
    cmd = cmd.split(' ')
    cmd[0] = cmd[0].lower()
    return cmd


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


def main():
    while True:
        term_width = os.get_terminal_size().columns
        term_height = os.get_terminal_size().lines
        contacts = ContactBook(load_contacts())
        print(f'terminal dimensions: {term_width}x{term_height}')
        cmd = parse_cmd(prompt('Command, my Lord> '))
        print(move_ln_up, end='')  # moves cursor to beginning of prev line
        print(Settings.bg_color + ' ' * term_width, end='\r')  # clears line and paints it with background color
        print(
            f'  {Settings.bg_color}{Settings.time_color}{datetime.now().strftime('%d/%m %H:%M')}{Settings.end_color}    {' '.join(cmd)}')
        print(Settings.end_all, end='')
        match cmd[0]:
            case 'contacts':
                process_contacts_command(cmd)
            case 'notes':
                process_notes_command(cmd)
            case _:
                if cmd[0] in ['exit', 'end', 'quit']:
                    break
                else:
                    process_others_command(cmd)


if __name__ == '__main__':
    main()
