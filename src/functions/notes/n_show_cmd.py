from src.tools.StorageController import StorageController
from colorama import Fore
import time

def n_show_cmd(cmd):
    storage = StorageController()
    notes = storage.load_note_book()

    if notes.data:
        intro_text = """

         Across the streams of time,
|-----|  in the vast library of the universe,
|II|II|  lie the moments captured,
|II|II|  in the whispers of these titles...
|II|II|  Each a gateway, each a story,
|II|II|  within the endless space of ideas!

"""
        for char in intro_text:
            print(char, end='', flush=True)
            time.sleep(0.01)

        for index, note in enumerate(notes.data):
            notes_titles = f"{Fore.YELLOW}{index}: {note.title}\n{Fore.RESET}\n"
            for char in notes_titles:
                print(char, end='', flush=True)
                time.sleep(0.015)

    else:
        print("No notes available.") 

