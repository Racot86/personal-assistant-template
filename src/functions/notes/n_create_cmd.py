'''Notes create command'''
from src.classes.class_Note import Note
from src.tools.StorageController import StorageController
from prompt_toolkit import prompt

'''commands to check: notes create <title>'''


def n_create_cmd(cmd):
    storage = StorageController()
    notes = storage.load_note_book()
    title = " ".join(cmd[1:])
    print("end")
    for note in notes:
        if note.title == title:
            print("Note with this title already exists. Cannot create a duplicate note.")
            return
    
    text = prompt("Your note, my Lord>", multiline=True)

    note = Note(title)
    note.body = text
    notes.add_note(note)
    
    print(f"title: {note.title}\nbody: {note.body}\ntime: {note.time}\nNote added successfully!")
    
    storage.save_note_book(notes)







