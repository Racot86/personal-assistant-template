from src.classes.class_Field import Field


class Title(Field):
    def __init__(self, value):
        super().__init__(value)


class Body(Field):
    def __init__(self, value):
        super().__init__(value)


class Note:
    def __init__(self, name):
        self.__title = ''
        self.name = name
        self.__body = ''
        self.__tags = []
        self.__time = ''

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_value):
        self.__name = new_value

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, new_value):
        self.__body = new_value

    @property
    def tags(self):
        return self.__tags

    @tags.setter
    def tags(self, new_value: list):
        self.__tags = new_value

    def __find_tags(self):
        pass

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, new_value):
        self.__time = new_value
