import re
from src.classes.class_Note import Note
from src.classes.class_NoteBook import NoteBook
from src.tools.load_notes import load_notes

def n_search_cmd(cmd):
    pattern = " ".join(cmd[1:])
    notes = NoteBook(load_notes())
    found_notes = []
    for index, note in enumerate(notes.data):
        if (re.search(pattern, note.title, re.IGNORECASE) or re.search(pattern, note.body, re.IGNORECASE)):
            found_notes.append((index, note))
    
    if found_notes:
        for idx, note in found_notes:
            print(f"Index: {idx}, Title: '{note.title}', Body: '{note.body}'")
    else:
        print("No notes found.")

if __name__ == "__main__":
    pass
