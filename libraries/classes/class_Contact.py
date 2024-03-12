from datetime import datetime
from libraries.classes.class_Field import Field


def validation_tracker(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            if str(e) == 'invalid_phone':
                print('Entry has invalid phone number(s)')
            elif str(e) == 'invalid_email':
                print('Entry has invalid e-mail address')
            elif str(e) == 'invalid_name':
                print('Entry has invalid name')
            else:
                print(e)
        except TypeError as e:
            print(e)

    return wrapper


class Name(Field):
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


class Phones(Field):
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
            if invalid == True:
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


class Email(Field):
    @validation_tracker
    def __init__(self, value):
        if isinstance(value, str) and '@' in value and '.' in value:
            super().__init__(value)
        else:
            value = ''
            super().__init__(value)
            raise ValueError("invalid_email")


class Birthday(Field):

    def __init__(self, value):
        try:
            value = datetime.strptime(value, '%d-%m-%Y')
            super().__init__(value)
        except ValueError:
            print('Entry has wrong date format')
            value = ''
            super().__init__(value)
        except TypeError:
            value = ''
            super().__init__(value)
            print('Entry has wrong date format')


class Address(Field):
    def __init__(self, value):
        super().__init__(value)


class Remark(Field):
    def __init__(self, value):
        super().__init__(value)


class Contact:
    def __init__(self, name):
        self.__name = ''
        self.name = name
        self.__phones = ''
        self.__email = ''
        self.__address = ''
        self.__birthday = ''
        self.__remark = ''

    @property
    def name(self):
        if self.__name != '':
            return self.__name.value
        else:
            return self.__name

    @name.setter
    def name(self, new_value):
        self.__name = Name(new_value)

    @property
    def phones(self):
        if self.__phones != []:
            return self.__phones.value
        else:
            return self.__phones

    @phones.setter
    def phones(self, new_value):
        check = Phones(new_value)
        if check.value != []:
            self.__phones = Phones(new_value)
        if new_value == []:
            self.__phones = []

    @property
    def email(self):
        if self.__email != '':
            return self.__email.value
        else:
            return self.__email

    @email.setter
    def email(self, new_value):
        if new_value != '':
            check = Email(new_value)
            if check.value != '':
                self.__email = Email(new_value)
        else:
            self.__email = ''

    @property
    def address(self):
        if self.__address != '':
            return self.__address.value
        else:
            return self.__address

    @address.setter
    def address(self, new_value):
        self.__address = Address(new_value)

    @property
    def birthday(self):
        if self.__birthday != '':
            return self.__birthday.value.strftime('%d-%m-%Y')
        else:
            return self.__birthday

    @birthday.setter
    def birthday(self, new_value):
        if new_value != '':
            check = Birthday(new_value)
            if check.value != '':
                self.__birthday = Birthday(new_value)
        else:
            self.__birthday = ''

    @property
    def remark(self):
        if self.__remark != '':
            return self.__remark.value
        else:
            return self.__remark

    @remark.setter
    def remark(self, new_value):
        self.__remark = Remark(new_value)

    def __str__(self):
        return f'name: {self.name} <{self.remark}>\ne-mail: {self.email}\nphones: {', '.join(self.phones)}\naddress: {self.address}\nbirthday: {self.birthday}'
