'''Notes create command'''
from src.classes.class_Note import Note
from src.tools.StorageController import StorageController
from prompt_toolkit import prompt
from settings import Settings
from src.tools.a_print import a_print

'''commands to check: notes create <title>'''


def n_create_cmd(cmd):
    storage = StorageController()
    notes = storage.load_note_book()
    title = " ".join(cmd[1:])
    print(f"{Settings.warning_color}finish editing text, press for mac: opt+end or esc+ent win: meta+end{Settings.end_color}")
    for note in notes:
        if note.title == title:
            print(f"{Settings.error_color}Note with this title already exists. Cannot create a duplicate note.{Settings.end_color}")
            return
    
    text = prompt("Your note, my Lord>", multiline=True)

    note = Note(title)
    note.body = text
    notes.add_note(note)
    
    print(f"{Settings.style_bold}title: {note.title}\nbody: {note.body}\ntime: {note.time}{Settings.end_color} ")
    print(f"{Settings.success_color}Note added successfully!{Settings.end_color}")
    
    storage.save_note_book(notes)







