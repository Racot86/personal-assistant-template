from src.classes.class_NoteBook import NoteBook
from src.classes.class_Note import Note
from src.tools.load_notes import load_notes
from src.tools.save_notes import save_notes
from prompt_toolkit import prompt


def n_create_cmd(cmd):
    notes = NoteBook(load_notes()) 
    note = Note(" ".join(cmd[1:]))
    text = prompt("Your note, my Lord>", multiline=True)
    note.body = text
    # tags = []
    notes.add_note(note)
    print(f"title: {note.title}\nbody: {note.body}\ntime: {note.time}\nNote added successfully!")
    save_notes(notes)



