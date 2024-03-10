from collections import UserList
from libraries.classes.class_Contact import Contact


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

    def add_contact(self, value: Contact):
        if isinstance(value, Contact) and not self.contact_exists(value):
            self.data.append(value)
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
