'''Class Name'''

from bot.src.classes.class_Field import Field
from bot.src.classes.exceptions import validation_tracker


class Phones(Field):
    '''Contacts phones'''
    @validation_tracker
    def __init__(self, value):
        if isinstance(value, list):
            valid_list = []
            invalid = False
            for phone in value:
                phone = self.__reformat_phone(phone)
                if self.__validate_phone(phone):
                    valid_list.append(phone)
                else:
                    invalid = True
            value = valid_list
            super().__init__(value)
            if invalid is True:
                raise ValueError('invalid_phone')

        elif isinstance(value, str):
            value = self.__reformat_phone(value)
            if self.__validate_phone(value):
                value = [value]
                super().__init__(value)
            else:
                value = []
                super().__init__(value)
                raise ValueError('invalid_phone')
        else:
            value = []
            super().__init__(value)
            raise ValueError('invalid_phone')

    def __reformat_phone(self, value):
        if isinstance(value, str):
            pattern = ('(', ')', '+', '38', '-')
            for check in pattern:
                value = value.replace(check, '')
                value = value.strip()
        else:
            value = ''
        return value

    def __validate_phone(self, value):
        if value.isdigit() and len(value) == 10:
            return True
        else:
            return False
