from collections import UserList
from src.classes.class_Note import Note



class NoteBook(UserList):

    def note_exists(self,note_title):
        for note in self.data:
            if note.title == note_title:
                return True
        return False

    def add_note(self, note: Note):
        if not self.note_exists(note.title):
            self.data.append(note)
            return True
        else:
            return False

    def get_note(self, note_name: str):
        for note in self.data:
            if note.name == note_name:
                return note
        return False

    def delete_note(self, note: Note):
        self.data.remove(note)
