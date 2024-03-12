from collections import UserList
from src.classes.class_Contact import Contact


class ContactBook(UserList):

    def contact_exists(self, name: str):
        match = 0
        for contact in self.data:
            if contact.name == name:
                match = 1
        if match == 0:
            return False
        else:
            return True

    def add_contact(self, value: Contact):
        if isinstance(value, Contact) and not self.contact_exists(value.name):
            self.data.append(value)
            return True
        else:
            return False

    def __str__(self):
        names_list = []
        for contact in self.data:
            names_list.append(contact.name)
        return str(names_list)

    def delete_contact(self, value: Contact):
        self.data.remove(value)

    def get_contact(self, name: str):
        for contact in self.data:
            if contact.name == name:
                return contact
        return False

    def size(self):
        return len(self.data)
