import re
from bot.src.tools.StorageController import StorageController
from bot.settings import Settings
from bot.src.tools.a_print import a_print
import time

def n_search_cmd(cmd):
    pattern = " ".join(cmd[1:])
    storage = StorageController()
    notes = storage.load_note_book()
    found_notes = []
    for index, note in enumerate(notes.data):
        if (re.search(pattern, note.title, re.IGNORECASE) or re.search(pattern, note.body, re.IGNORECASE)):
            found_notes.append((index, note))
    
    if found_notes:
        tardis_label = Settings.TARDIS
        tardis_text = """
           Decode the notes,
  |-----|  Doctor, I
  |II|II|  hear the echoes
  |II|II|  of distant galaxies...
  |II|II|  Our calculations suggest,
  |II|II|  ... the enemy's spaceship is near!

"""
        print(f"{tardis_label}", end='')
        print(f"{Settings.shadow_color}{tardis_text}{Settings.end_all}")
        time.sleep(Settings.NOTES_INTRO_DELAY)

        for idx, note in found_notes:
            print(f"  {Settings.shadow_color}ID:{Settings.end_all} {idx}")
            time.sleep(Settings.NOTES_TITLE_DELAY)
            
            print(f"  {Settings.shadow_color}Title:{Settings.end_all} {note.title}")
            time.sleep(Settings.NOTES_TITLE_DELAY)

            note_body = f"{Settings.shadow_color}Body:{Settings.end_all}\n{Settings.notes_color}\n{note.body}\n{Settings.end_color}\n"
            print('  ', end='')
            for char in note_body:
                if char == '\n':
                    char = '\n  '
                print(char, end='', flush=True)
                time.sleep(Settings.NOTES_BODY_DELAY)
            print('\r',end='')

    else:
        a_print(f"Currently adrift in silence, my archives yield no tales.", prefix = Settings.TARDIS, main_color=Settings.error_color)

if __name__ == "__main__":
    pass
