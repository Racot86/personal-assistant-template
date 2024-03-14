import re
from src.tools.StorageController import StorageController
from colorama import Fore, Style
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
        tardis_text = """
         Decode the notes,
|-----|  Doctor, I
|II|II|  hear the echoes
|II|II|  of distant galaxies...
|II|II|  It seems to be her,
|II|II|  ... the TARDIS!



"""
        for char in tardis_text:
                print(char, end='', flush=True)
                time.sleep(0.015)

        for idx, note in found_notes:
            id = f"{Style.BRIGHT}ID:{Style.RESET_ALL} {idx}\n"
            for char in id:
                print(char, end='', flush=True)
                time.sleep(0.01)
            
            note_title = f"{Style.BRIGHT}Title:{Style.RESET_ALL} {note.title}\n"
            for char in note_title:
                print(char, end='', flush=True)
                time.sleep(0.01)

            note_body = f"{Style.BRIGHT}Body:{Style.RESET_ALL}\n{Fore.YELLOW}\n{note.body}\n{Fore.RESET}\n"
            for char in note_body:
                print(char, end='', flush=True)
                time.sleep(0.03)

    else:
        print("No notes found.")

if __name__ == "__main__":
    pass
