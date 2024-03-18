'''Class Name'''

from bot.src.classes.class_Field import Field
from bot.src.classes.exceptions import validation_tracker

class Name(Field):
    '''Name of contact'''
    @validation_tracker
    def __init__(self, value):
        if isinstance(value, str):
            super().__init__(value)
        else:
            value = str(value)
            super().__init__(value)
            raise ValueError('invalid_name')

    def __str__(self):
        return self.value
