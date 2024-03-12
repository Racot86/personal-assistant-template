from collections import UserList
from src.classes.class_Note import Note


class NoteBook(UserList):
    def add_note(self, note: Note):
        self.data.append(note)

    def delete_note(self, note: Note):
        self.data.remove(note)
