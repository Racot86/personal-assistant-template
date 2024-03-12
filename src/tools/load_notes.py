import pickle
from pathlib import Path


def load_notes():
    if Path.is_file(Path('notes.bin')):
        with open('notes.bin', 'rb') as fh:
            return pickle.load(fh)
    else:
        print('no contacts')
        return []
