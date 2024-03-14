from src.tools.StorageController import StorageController
from src.classes.class_Note import Note
from src.classes.class_NoteBook import NoteBook
from prompt_toolkit import prompt


def print_list(match, search_criteria):
    if len(match) > 0:
        n = 1
        print(f"    Tardis: Look, where I found tag(s) {' '.join(search_criteria)}")
        for note in match:
            print(f'            {n} {note.title}')
            n += 1
    else:
        print(f'    Sir, I did not find any notes with {" ".join(search_criteria)}')


def n_filter_cmd(cmd):
    if len(cmd) > 3 and cmd[1].lower() == 'by' and cmd[2].lower() == 'tag':
        storage = StorageController()
        notes = storage.load_note_book()
        cmd.pop(0)
        cmd.pop(0)
        cmd.pop(0)
        match_list = []
        for note in notes:
            if len(note.tags) > 0:
                for tag in note.tags:
                    for search_tag in cmd:
                        if tag.lower() == search_tag.lower():
                            match_list.append(note)
                            continue

            else:
                continue

        print_list(match_list, cmd)


    else:
        print('     Tardis: Doctor, are you Ok? Check what you are typing!')

