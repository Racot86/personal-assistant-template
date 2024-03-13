from src.classes.class_NoteBook import NoteBook
from src.tools.load_notes import load_notes
from src.tools.save_notes import save_notes

def n_delete_cmd(cmd):
    notes = NoteBook(load_notes())
    title_to_delete = " ".join(cmd[1:])
    
    for note in notes:
        if note.title == title_to_delete:
            notes.remove(note)
            print(f"Note '{note.title}' deleted successfully!")
            save_notes(notes)
            return
    
    print(f"No note with title '{title_to_delete}' found.")
  