'''Email Name'''

from src.classes.class_Field import Field
from src.classes.exceptions import validation_tracker


class Email(Field):
    '''Email of contact'''
    @validation_tracker
    def __init__(self, value):
        if isinstance(value, str) and '@' in value and '.' in value:
            super().__init__(value)
        else:
            value = ''
            super().__init__(value)
            raise ValueError("invalid_email")
