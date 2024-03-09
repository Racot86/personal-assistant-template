import pickle
from pathlib import Path


def load_contacts():
    if Path.is_file(Path('contacts.bin')):
        with open('contacts.bin', 'rb') as fh:
            return pickle.load(fh)
    else:
        print('no contacts')
        return []
