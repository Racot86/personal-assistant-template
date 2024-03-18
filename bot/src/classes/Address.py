'''Address class'''

from bot.src.classes.class_Field import Field

class Address(Field):
    '''Address of the contact'''
    def __init__(self, value):
        super().__init__(value)
