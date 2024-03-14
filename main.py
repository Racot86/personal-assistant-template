# importing standard & custom modules
from prompt_toolkit import prompt
from datetime import datetime
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

# defining variables
move_ln_up = '\033[F'


def parse_cmd(cmd):
    cmd = cmd.strip()
    cmd = cmd.split(' ')
    cmd[0] = cmd[0].lower()
    return cmd


a_print(f'Doctor, looks like you forget - I am Tardis!',
        used_colors=[Settings.bg_color,Settings.time_color],
        prefix='TARDIS: ',
        prefix_color=Settings.bg_color,
        main_color=Settings.time_color,
        speed=0.02,
        wait_after=0.5
        )
a_print(f'If you forget something, ask me using help command.',
        used_colors=[Settings.bg_color,Settings.time_color],
        prefix='        ',
        main_color=Settings.time_color,
        speed=0.02,
        )


def main():
    while True:
        term_width = os.get_terminal_size().columns
        term_height = os.get_terminal_size().lines
        # print(f"terminal window size: {term_width}x{term_height}")
        cmd = parse_cmd(prompt('Command, my Lord> '))
        print(move_ln_up, end='')  # moves cursor to beginning of prev line
        print(Settings.bg_color + ' ' * term_width, end='\r')  # clears line and paints it with background color
        print(
            f"  {Settings.bg_color}{Settings.time_color}{datetime.now().strftime('%d/%m %H:%M')}{Settings.end_color}  Doctor: {' '.join(cmd)}")
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
