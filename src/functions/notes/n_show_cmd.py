from src.tools.StorageController import StorageController
from colorama import Fore, Style
from settings import Settings
from src.tools.a_print import a_print
import time

def n_show_cmd(cmd):
    storage = StorageController()
    notes = storage.load_note_book()
    pattern = " ".join(cmd[1:])
    note_found = False

    if notes.data:
        tardis_label = Settings.TARDIS
        tardis_text = """
           Across the streams of time,
|-----|    in the vast library of the universe,
|II|II|    lie the moments captured,
|II|II|    in the whispers of these titles...
|II|II|    Each a gateway, each a story,
|II|II|    within the endless space of notes!
"""
        if len(pattern) == 0: 
            print(f"{tardis_label}", end='')
            print(f"{Settings.shadow_color}{tardis_text}{Settings.end_all}")
            for index, note in enumerate(notes.data):
                print(f"{Settings.notes_color}{index}: {note.title}{Settings.end_color}")
            print()

        elif len(pattern) > 0:
            for note in notes.data:
                if pattern == note.title:

                    note_found = True
                    print(f"{tardis_label}", end='')
                    print(f"{Settings.shadow_color}{tardis_text}{Settings.end_all}")
                    time.sleep(Settings.NOTES_INTRO_DELAY)

                    print(f"{Settings.shadow_color}Title:{Settings.end_all} {note.title}")
                    time.sleep(Settings.NOTES_TITLE_DELAY)

                    print(f"{Settings.shadow_color}Body:{Settings.end_all}\n")
                    time.sleep(Settings.NOTES_BODY_DELAY)

                    for char in note.body:
                        print(f"{Settings.notes_color}{char}{Settings.end_color}", end='', flush=True)
                        time.sleep(Settings.NOTES_BODY_DELAY)
                    print("\n")
                    break

            if not note_found:
                a_print(f"Currently adrift in silence, my archives yield no tales.", prefix = Settings.TARDIS, main_color=Settings.error_color)
    
    else:
        a_print(f"Currently adrift in silence, my archives yield no tales.", prefix = Settings.TARDIS, main_color=Settings.error_color)
