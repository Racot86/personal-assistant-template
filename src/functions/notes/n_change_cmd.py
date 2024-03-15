'''Change notes function'''
from src.tools.StorageController import StorageController
from prompt_toolkit.styles import Style
from settings import Settings
from prompt_toolkit import prompt

style = Style.from_dict({'': Settings.PROMPT_INPUT_COLOR, 'prompt': Settings.PROMPT_TEXT_COLOR })

'''Commands for checking: notes change apple'''

def n_change_cmd(cmd):
    storage = StorageController()
    notes = storage.load_note_book()
    title = " ".join(cmd[1:])
    if not notes.note_exists(title): 
        print(f"{Settings.error_color}Note with provided title not found{Settings.end_color}")
    else:
        new_title = prompt("Enter new title>", multiline=True, style=style)

        note = [note for note in notes if note.title == title][0]
        note.title = new_title
        print(f"{Settings.shadow_color}Time: {Settings.end_all}{note.time}")
        print(f"{Settings.shadow_color}Title: {Settings.end_all}{new_title}")
        print(f"{Settings.shadow_color}Body:{Settings.end_all}\n{Settings.notes_color}\n{note.body}\n{Settings.end_color}\n")
        print(f"{Settings.success_color}Title updated successfully!{Settings.end_color}")
        storage.save_note_book(notes)

        current_body = note.body

        new_text = prompt("Enter new body>", multiline=True, default=current_body,style=style)
        note.body = new_text
        print(f"{Settings.shadow_color}Time: {Settings.end_all}{note.time}")
        print(f"{Settings.shadow_color}Title: {Settings.end_all}{note.title}")
        print(f"{Settings.shadow_color}Body:{Settings.end_all}\n{Settings.notes_color}\n{new_text}\n{Settings.end_color}\n")
        print(f"{Settings.success_color}Note updated successfully!!{Settings.end_color}")
        storage.save_note_book(notes)
        

