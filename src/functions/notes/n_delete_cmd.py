'''Notes delete command'''
from src.tools.StorageController import StorageController
from settings import Settings

'''command to check: notes delete <title>'''

def n_delete_cmd(cmd):

    storage = StorageController()
    notes = storage.load_note_book()
    title_to_delete = " ".join(cmd[1:])
    
    for note in notes:
        if note.title == title_to_delete:
            notes.remove(note)
            print(f"{Settings.success_color}Note '{note.title}' deleted successfully!{Settings.end_all}")
            storage.save_note_book(notes)
            return
    
    print(f"{Settings.error_color}No note with title '{title_to_delete}' found!{Settings.end_all}")

