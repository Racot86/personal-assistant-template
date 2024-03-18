'''Class Contact'''

from bot.src.classes.Name import Name
from bot.src.classes.Phones import Phones
from bot.src.classes.Email import Email
from bot.src.classes.Address import Address
from bot.src.classes.Birthday import Birthday
from bot.src.classes.Remark import Remark



class Contact:
    '''Contact'''
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
        '''Getting a name of contact'''
        if self.__name != '':
            return self.__name.value
        else:
            return self.__name

    @name.setter
    def name(self, new_value):
        self.__name = Name(new_value)

    @property
    def phones(self):
        '''Getting a phones of contact'''
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
        '''Getting a email of contact'''
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
        '''Getting a address of contact'''
        if self.__address != '':
            return self.__address.value
        else:
            return self.__address

    @address.setter
    def address(self, new_value):
        self.__address = Address(new_value)

    @property
    def birthday(self):
        '''Getting abirthday of contact'''
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
        '''Getting a remark of contact'''
        if self.__remark != '':
            return self.__remark.value
        else:
            return self.__remark

    @remark.setter
    def remark(self, new_value):
        self.__remark = Remark(new_value)

    def __str__(self):
        return f"name: {self.name} <{self.remark}>\ne-mail: {self.email}\nphones: {', '.join(self.phones)}\naddress: {self.address}\nbirthday: {self.birthday}"
