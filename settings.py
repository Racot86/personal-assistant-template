from colorama import Fore, Back, Style


class Settings:

#TODO: remove next variables before prod
    time_color = Fore.CYAN
    bg_color = Back.LIGHTBLACK_EX
    bg_cmd_line_color = Back.LIGHTCYAN_EX

# input_color, msg_color, warning_color, error_color
    style_bold = Style.BRIGHT # Some bolder text
    msg_color = Fore.CYAN # regular bot message
    input_color = Fore.CYAN # user input color
    warning_color = Fore.LIGHTYELLOW_EX # warning bot message
    error_color = Fore.LIGHTRED_EX # error bot message
    success_color = Fore.LIGHTGREEN_EX # success bot message
    notes_color = Fore.YELLOW # color for all user notes
    shadow_color = Style.DIM # less prominent color for the secondary information
    bg_msg_color = Back.LIGHTBLACK_EX
    end_color = Fore.RESET # end font color tag (required on each line!)
    end_all = Style.RESET_ALL # end font and background color tag
    __tardis_name_color = Fore.CYAN # color for the "TARDIS:" name

# time delays
    NOTES_INTRO_DELAY = 0.01
    NOTES_TITLE_DELAY = 0.015
    NOTES_BODY_DELAY = 0.03

# prompt colors
    PROMPT_TEXT_COLOR = 'ansiblue'
    PROMPT_INPUT_COLOR = 'ansigray'
    PROMPT_NOTE_COLOR = 'ansiyellow'
    PROMPT_TARDIS_COLOR = 'ansiwhite'

# tardis settings
    TARDIS = f"{__tardis_name_color}TARDIS: {end_color}"
