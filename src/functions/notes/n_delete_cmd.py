'''Notes delete command'''
from src.tools.StorageController import StorageController
from settings import Settings
from src.tools.a_print import a_print

'''command to check: notes delete <title>'''

def n_delete_cmd(cmd):

    storage = StorageController()
    notes = storage.load_note_book()
    title_to_delete = " ".join(cmd[1:])
    
    for note in notes:
        if note.title == title_to_delete:
            notes.remove(note)
            a_print(f"Note '{note.title}' deleted successfully!", prefix="TARDIS: ", main_color=Settings.success_color)
            storage.save_note_book(notes)
            return
    
    a_print(f"No note with title '{title_to_delete}' found!", prefix="TARDIS: ", main_color=Settings.error_color)

