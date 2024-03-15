from collections import UserList
from src.classes.class_Contact import Contact


class ContactBook(UserList):

    def contact_exists(self, name: str):
        for contact in self.data:
            if contact.name == name:
                return True
        return False

    def add_contact(self, value: Contact):
        self.data.append(value)


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
