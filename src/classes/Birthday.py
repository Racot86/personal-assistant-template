'''Birthday Name'''

from datetime import datetime
from src.classes.class_Field import Field
from settings import Settings

class Birthday(Field):
    '''Birthday of the contact'''
    def __init__(self, value):
        try:
            value = datetime.strptime(value, '%d-%m-%Y')
            super().__init__(value)
        except ValueError:
            print(f"{Settings.error_color}Entry has wrong date format, my Lord!{Settings.end_color}")
            value = ''
            super().__init__(value)
        except TypeError:
            value = ''
            super().__init__(value)
            print(f"{Settings.error_color}Entry has wrong date format, my Lord!{Settings.end_color}")
