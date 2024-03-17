'''Change notes function'''
from src.tools.StorageController import StorageController
from prompt_toolkit.styles import Style
from settings import Settings
from prompt_toolkit import prompt
from src.tools.a_print import a_print

style = Style.from_dict({'': Settings.PROMPT_INPUT_COLOR, 'prompt': Settings.PROMPT_TEXT_COLOR })

'''Commands for checking: notes change apple'''

def n_change_cmd(cmd):
    storage = StorageController()
    notes = storage.load_note_book()
    title = " ".join(cmd[1:])
    if not notes.note_exists(title): 
        a_print("Note with provided title not found", prefix = Settings.TARDIS, main_color=Settings.error_color)
    else:
        print(f"{Settings.warning_color}Finish text editing press: opt+ent or esc+ent (mac) meta+ent (win){Settings.end_all}")
        print(Settings.TARDIS)
        new_title = prompt("   Enter new title> ", default=title, style=style)

        note = [note for note in notes if note.title == title][0]
        note.title = new_title
        print(f"{Settings.shadow_color}Time: {Settings.end_all}{note.time}")
        print(f"{Settings.shadow_color}Title: {Settings.end_all}{new_title}")
        print(f"{Settings.shadow_color}Body:{Settings.end_all}\n{Settings.notes_color}\n{note.body}\n{Settings.end_color}\n")
        a_print("Title updated successfully!", prefix = Settings.TARDIS, main_color=Settings.success_color)
        storage.save_note_book(notes)

        current_body = note.body

        print(Settings.TARDIS)
        new_text = prompt("   Enter new body>", multiline=True, default=current_body,style=style)
        note.body = new_text
        print(f"{Settings.shadow_color}Time: {Settings.end_all}{note.time}")
        print(f"{Settings.shadow_color}Title: {Settings.end_all}{note.title}")
        print(f"{Settings.shadow_color}Body:{Settings.end_all}\n{Settings.notes_color}\n{new_text}\n{Settings.end_color}\n")
        a_print("Note updated successfully!!", prefix = Settings.TARDIS, main_color=Settings.success_color)
        storage.save_note_book(notes)
        

