'''Notes create command'''
from src.classes.class_Note import Note
from src.tools.StorageController import StorageController
from prompt_toolkit import prompt
from settings import Settings
from prompt_toolkit.styles import Style
from src.tools.a_print import a_print

'''commands to check: notes create <title>'''

style = Style.from_dict({'': Settings.PROMPT_INPUT_COLOR, 'prompt': Settings.PROMPT_TEXT_COLOR, 'note':Settings.PROMPT_NOTE_COLOR})


def n_create_cmd(cmd):
    storage = StorageController()
    notes = storage.load_note_book()
    title = " ".join(cmd[1:])
    
    if not title:
        a_print("Oops...give me the title please", prefix="TARDIS: ", main_color=Settings.warning_color)
        return

    for note in notes:
        if note.title == title:
            a_print("Note with this title already exists. Cannot create a duplicate note", prefix="TARDIS: ",  main_color=Settings.warning_color)
            return

    text = prompt("Your note, my Lord>", multiline=True, style=style)
    note = Note(title)
    note.body = text
    notes.add_note(note)

    print(f"{Settings.shadow_color}Time:{Settings.end_all} {note.time}")
    print(f"{Settings.shadow_color}Title:{Settings.end_all} {note.title}")
    print(f"{Settings.shadow_color}Body:{Settings.end_all}\n{Settings.notes_color}\n{note.body}\n{Settings.end_color}\n")
    a_print("Note added successfully!", prefix="TARDIS: ",  main_color=Settings.success_color)

    storage.save_note_book(notes)









