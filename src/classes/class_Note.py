from src.classes.class_Field import Field
from datetime import datetime

class Title(Field):
    def __init__(self, value):
        super().__init__(value)


class Body(Field):
    def __init__(self, value):
        super().__init__(value)


class Note:
    def __init__(self, title):
        self.__title = Title(title)
        self.__body = ''
        self.__tags = []
        self.__time = ''

    @property
    def title(self):
        if self.__title != '':
            return self.__title.value
        else:
            return self.__title

    @title.setter
    def title(self, new_value):
        self.__time = datetime.now()
        self.__title = Title(new_value)

    @property
    def body(self):
        if self.__body != '':
            return self.__body.value
        else:
            return self.__body

    @body.setter
    def body(self, new_value):
        self.__time = datetime.now()
        self.__body = Body(new_value)

    def __find_tags(self):
        pass

    def __str__(self):
        return f'title: {self.title}\nbody: {self.body}\ntime: {self.__time}\ntags: {self.__tags}'
