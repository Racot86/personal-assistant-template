# importing standard & custom modules
from prompt_toolkit import prompt
from datetime import datetime

from prompt_toolkit.completion import WordCompleter

from settings import Settings
from colorama import Fore
import os

#  import classes
from src.classes.class_Note import Note
from src.classes.class_NoteBook import NoteBook
from src.classes.class_Contact import Contact
from src.classes.class_ContactBook import ContactBook
# importing contacts controller function
from src.functions.command_controllers.process_contacts_command import process_contacts_command
# importing notes controller function
from src.functions.command_controllers.process_notes_command import process_notes_command
# importing others controller function
from src.functions.command_controllers.process_others_commans import process_others_command
# importing tools
from src.tools.StorageController import StorageController
from src.tools.a_print import a_print
from prompt_toolkit.styles import Style
from src.tools.completer_dict import completer

# defining variables
move_ln_up = '\033[F'

style = Style.from_dict({'': Settings.PROMPT_INPUT_COLOR, 'prompt': Settings.PROMPT_TEXT_COLOR})


def parse_cmd(cmd):
    cmd = cmd.strip()
    cmd = cmd.split(' ')
    cmd[0] = cmd[0].lower()
    return cmd


a_print(f'If you forget something, ask me using help command.',
        used_colors=[Settings.msg_color],
        prefix='TARDIS: ',
        main_color=Settings.msg_color,
        )


def main():
    while True:
        term_width = os.get_terminal_size().columns
        term_height = os.get_terminal_size().lines
        # print(f"terminal window size: {term_width}x{term_height}")
        cmd = parse_cmd(prompt('Enter your command: ', style=style, completer=completer()))
        print(move_ln_up, end='')
        print(" " * term_width, end='\r')
        print(
            f"  Doctor: {' '.join(cmd)}")
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
