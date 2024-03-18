import os
import pickle


def save_notes(data):
    if len(data) > 0:
        with open('notes.bin', 'wb') as fh:
            pickle.dump(data, fh)
    else:
        if os.path.exists("notes.bin"):
            os.remove("notes.bin")
