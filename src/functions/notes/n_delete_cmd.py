'''Notes delete command'''
from src.tools.StorageController import StorageController

'''command to check: notes delete <title>'''

def n_delete_cmd(cmd):

    storage = StorageController()
    notes = storage.load_note_book()
    title_to_delete = " ".join(cmd[1:])
    
    for note in notes:
        if note.title == title_to_delete:
            notes.remove(note)
            print(f"Note '{note.title}' deleted successfully!")
            storage.save_note_book(notes)
            return
    
    print(f"No note with title '{title_to_delete}' found.")

