from src.classes.class_Field import Field
from datetime import datetime
from src.tools.find_all import find_all

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
        self.__find_tags(self.__body.value)

    @property
    def time(self):
        if self.__time != '':
            return self.__time.strftime("%d-%m-%Y %H:%M:%S")

    def __find_tags(self, value: str):
        matches = find_all(value,'#')
        matches = list(matches)
        if len(matches) > 0:
            value = value.replace('\n',' ') + ' '
            tag_list = []
            for match in matches:
                start = match
                end = 0
                if start + 20 > len(value):
                    end = len(value)
                else:
                    end = start + 20
                for i in range(start, end):
                    if value[i] == ' ' or i == len(value):
                        tag_list.append(value[start:i])
                        break

            self.__tags = tag_list



    def __str__(self):
        return f'title: {self.title}\nbody: {self.body}\ntime: {self.__time.strftime("%d-%m-%Y %H:%M:%S")}\ntags: {self.__tags}'
