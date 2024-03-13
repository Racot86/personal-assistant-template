from src.tools.load_contacts import load_contacts
from src.tools.save_contacts import save_contacts
from src.classes.class_ContactBook import ContactBook
from src.classes.class_Contact import Contact

def c_delete_cmd(cmd):
    contacts = ContactBook(load_contacts())
    contact = Contact('Dmytro')
    contact.birthday = '04-06-1986'
    contacts.add_contact(contact)
    contacts.delete_contact(contact)
    print(contacts[0])

    save_contacts(contacts)