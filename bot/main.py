# importing standard & custom modules
from prompt_toolkit import prompt
from bot.settings import Settings
import sys
import os
# importing contacts controller function
from bot.src.functions.command_controllers.process_contacts_command import process_contacts_command
# importing notes controller function
from bot.src.functions.command_controllers.process_notes_command import process_notes_command
# importing others controller function
from bot.src.functions.command_controllers.process_others_commans import process_others_command
# importing tools
from bot.src.functions.others.intro import intro
from bot.src.tools.a_print import a_print
from prompt_toolkit.styles import Style
from bot.src.tools.completer_dict import completer
from bot.src.tools.cls import cls
from bot.src.tools.tool_bar import tool_bar

# defining variables
move_ln_up = '\033[F'
defstyle = sys.modules['prompt_toolkit.styles.defaults']
defstyle.PROMPT_TOOLKIT_STYLE.append(('completion-menu', 'bg:white fg:#146C94 reverse'))
defstyle.PROMPT_TOOLKIT_STYLE.append(("completion-menu.completion.current", 'bg:white fg:#146C94'))
defstyle.PROMPT_TOOLKIT_STYLE.append(('completion-menu.completion', 'bg:#146C94 fg:#F6F1F1'))
style = Style.from_dict({'prompt': Settings.PROMPT_TEXT_COLOR})


def parse_cmd(cmd):
    cmd = cmd.strip()
    cmd = cmd.split(' ')
    cmd[0] = cmd[0].lower()
    return cmd


intro()
tool_bar()
a_print(f'Doctor, Hi! I am at your service.',
        used_colors=[Settings.msg_color],
        prefix=Settings.TARDIS,
        main_color=Settings.msg_color,
        )
a_print(f'If you forget something, ask me using help command.',
        used_colors=[Settings.msg_color],
        prefix='        ',
        main_color=Settings.msg_color,
        )


def main():
    while True:
        term_width = os.get_terminal_size().columns
        term_height = os.get_terminal_size().lines
        if term_width > 80:
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
                        exit()
                    else:
                        process_others_command(cmd)
        else:
            cls()
            print(Settings.error_color + ' WARNING! WARNING! WARNING!' + Settings.end_all)
            print('      POOR CONNECTION')
            print('URGENTLY CHANGE TERMINAL SIZE')

if __name__ == '__main__':
    main()

