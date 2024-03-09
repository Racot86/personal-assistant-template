from collections import UserList


class Note:
    def __init__(self, name):
        self.__name = ''
        self.name = name
        self.__data = ''
        self.__tags = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_value):
        self.__name = new_value

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, new_value):
        self.__data = new_value

    @property
    def tags(self):
        return self.__tags

    @tags.setter
    def tags(self, new_value: list):
        self.__tags = new_value

    def __find_tags(self):
        pass


class NoteBook(UserList):
    def add_note(self, note: Note):
        self.data.append(note)