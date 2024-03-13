from src.classes.class_NoteBook import NoteBook
from src.classes.class_Note import Note
from src.tools.load_notes import load_notes
from src.tools.save_notes import save_notes
from prompt_toolkit import prompt

def n_change_cmd(cmd):
    notes = NoteBook(load_notes())
    title = " ".join(cmd[1:])
    for note in notes:
        if note.title == title:

            new_title = prompt("Enter new title>", multiline=True)
            note.title = new_title
            print(f"title: {new_title}\nbody: {note.body}\ntime: {note.time}\nTitle updated successfully!")
            save_notes(notes)

    # new_text = prompt("Enter new body>", multiline=True)
    # note.body = new_text
    # print(f"title: {note.title}\nbody: {new_text}\ntime: {note.time}\nNote updated successfully!")
    # save_notes(notes)
    



