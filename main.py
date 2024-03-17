# importing standard & custom modules
from prompt_toolkit import prompt
from settings import Settings

import os
# importing contacts controller function
from src.functions.command_controllers.process_contacts_command import process_contacts_command
# importing notes controller function
from src.functions.command_controllers.process_notes_command import process_notes_command
# importing others controller function
from src.functions.command_controllers.process_others_commans import process_others_command
from src.functions.others.intro import intro
# importing tools
from src.tools.StorageController import StorageController
from src.tools.a_print import a_print
from prompt_toolkit.styles import Style
from src.tools.completer_dict import completer
from src.tools.cls import cls
from src.tools.print_at import print_at

# defining variables
move_ln_up = '\033[F'

style = Style.from_dict({'': Settings.PROMPT_TEXT_COLOR, 'prompt': Settings.PROMPT_TEXT_COLOR})


def parse_cmd(cmd):
    cmd = cmd.strip()
    cmd = cmd.split(' ')
    cmd[0] = cmd[0].lower()
    return cmd


intro()


a_print(f'If you forget something, ask me using help command.',
        used_colors=[Settings.msg_color],
        prefix=Settings.TARDIS,
        main_color=Settings.msg_color,
        )


def main():
    while True:
        term_width = os.get_terminal_size().columns
        term_height = os.get_terminal_size().lines
        if term_width > 80:
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
        else:
            cls()
            print(Settings.error_color + ' WARNING! WARNING! WARNING!' + Settings.end_all)
            print('      POOR CONNECTION')
            print('URGENTLY CHANGE TERMINAL SIZE')


if __name__ == '__main__':
    main()
