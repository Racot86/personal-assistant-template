from datetime import datetime
from collections import UserList


def validation_tracker(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            if func.__name__ == 'phones':
                print('Entry has invalid phone number(s)')
            if func.__name__ == 'email':
                print('Entry has invalid e-mail')
            if func.__name__ == 'birthday':
                print('Entry has invalid birthday date')

    return wrapper


class Contact:
    def __init__(self, name):
        self.__name = ''
        self.name = name
        self.__phones = []
        self.__email = ''
        self.__address = ''
        self.__birthday = ''
        self.__remark = ''

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_value):
        self.__name = new_value

    @property
    def phones(self):
        return self.__phones

    @phones.setter
    @validation_tracker
    def phones(self, new_value):
        def reformat_phone(value):
            pattern = ('(', ')', '+', '38', '-')
            for check in pattern:
                value = value.replace(check, '')
                value = value.strip()
            return value

        def validate_phone(value):
            if value.isdigit() and len(value) == 10:
                return True
            else:
                return False

        if isinstance(new_value, list):
            count = 0
            valid_list = []
            invalid = False
            for phone in new_value:
                count += 1
                phone = reformat_phone(phone)
                if validate_phone(phone):
                    valid_list.append(phone)
                else:
                    invalid = True
                    # print(f'phone no {count} - not valid')
            if len(valid_list) > 0:
                self.__phones = valid_list
            if invalid == 1:
                raise ValueError("Invalid phone number")
        elif isinstance(new_value, str):
            new_value = reformat_phone(new_value)
            if validate_phone(new_value):
                self.__phones = [new_value]
            else:
                raise ValueError("Invalid phone number")
                # print('invalid phone')
        else:
            raise ValueError("Invalid phone number")
            # print('invalid phone')

    @property
    def email(self):
        return self.__email

    @email.setter
    @validation_tracker
    def email(self, new_value):
        if isinstance(new_value, str) and '@' in new_value and '.' in new_value:
            self.__email = new_value
        else:
            raise ValueError("Invalid email address")
            # print('invalid e-mail')

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, new_value):
        self.__address = new_value

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    @validation_tracker
    def birthday(self, new_value):
        self.__birthday = datetime.strptime(new_value, '%d-%m-%Y')

    @property
    def remark(self):
        return self.__remark

    @remark.setter
    def remark(self, new_value):
        self.__remark = new_value

    def __str__(self):
        return f'name: {self.name} <{self.remark}>\ne-mail: {self.email}\nphones: {', '.join(self.phones)}\naddress: {self.address}\nbirthday: {self.birthday}'


class ContactBook(UserList):

    def contact_exists(self, new_value: Contact):
        match = 0
        for contact in self.data:
            if contact.name == new_value.name:
                match = 1
        if match == 0:
            return False
        else:
            return True

    def add_contact(self, new_value: Contact):
        if isinstance(new_value, Contact) and not self.contact_exists(new_value):
            self.data.append(new_value)
            return True
        else:
            return False

    def __str__(self):
        names_list = []
        for contact in self.data:
            names_list.append(contact.name)
        return str(names_list)

    def delete_contact(self, new_value: Contact):
        self.data.remove(new_value)

    def change_contact(self, old_value: Contact, new_value: Contact):
        for contact in self.data:
            if contact.name == old_value.name:
                contact.name = new_value.name
                contact.phones = new_value.phones
                contact.email = new_value.email
                contact.birthday = new_value.birthday
                contact.address = new_value.address
                contact.remark = new_value.remark
                return True
        return False

    def get_contact(self, name: str):
        for contact in self.data:
            if contact.name == name:
                return contact
        return False
