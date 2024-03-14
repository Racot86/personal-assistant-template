from src.tools.StorageController import StorageController

from prompt_toolkit import prompt

def n_change_cmd(cmd):
    storage = StorageController()
    notes = storage.load_note_book()
    title = " ".join(cmd[1:])
    for note in notes:
        if note.title == title:

            new_title = prompt("Enter new title>", multiline=True)
            note.title = new_title
            print(f"title: {new_title}\nbody: {note.body}\ntime: {note.time}\nTitle updated successfully!")
            storage.save_note_book(notes)

            new_text = prompt("Enter new body>", multiline=True)
            note.body = new_text
            print(f"title: {note.title}\nbody: {new_text}\ntime: {note.time}\nNote updated successfully!")
            storage.save_note_book(notes)



