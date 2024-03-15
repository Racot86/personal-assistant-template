'''Notes create command'''
from src.classes.class_Note import Note
from src.tools.StorageController import StorageController
from prompt_toolkit import prompt
from settings import Settings
from prompt_toolkit.styles import Style

'''commands to check: notes create <title>'''

style = Style.from_dict({'': Settings.PROMPT_INPUT_COLOR, 'prompt': Settings.PROMPT_TEXT_COLOR, 'note':Settings.PROMPT_NOTE_COLOR})

def n_create_cmd(cmd):
    storage = StorageController()
    notes = storage.load_note_book()
    title = " ".join(cmd[1:])
    for note in notes:
        if note.title == title:
            print(f"{Settings.error_color}Note with this title already exists. Cannot create a duplicate note.{Settings.end_all}")
            return
    
    text = prompt("Your note, my Lord>", multiline=True, style=style)

    note = Note(title)
    note.body = text
    notes.add_note(note)
    
    print(f"{Settings.shadow_color}Time:{Settings.end_all} {note.time}")
    print(f"{Settings.shadow_color}Title:{Settings.end_all} {note.title}")
    print(f"{Settings.shadow_color}Body:{Settings.end_all}\n{Settings.notes_color}\n{note.body}\n{Settings.end_color}\n")
    print(f"{Settings.success_color}Note added successfully!")
    
    storage.save_note_book(notes)







