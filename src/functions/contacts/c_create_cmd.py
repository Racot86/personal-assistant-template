
'''Contact create command'''

from src.classes.class_ContactBook import ContactBook
from src.classes.class_Contact import Contact
from src.tools.load_contacts import load_contacts

def c_create_cmd(cmd):
    '''
    Creating a contact from command (cmd)
    Where 
        cmd[0] - string 'create'
        cmd[1] - contact name
        cmd[2], cmd[3], - optional: strings 'phones:XXXXXXXXXX,XXXXXXXXXX', 'email:asd@jhg', 'birthday:12.12.2012'
    '''
    
    book = ContactBook(load_contacts())
    
    if len(cmd)<2:
        print("Give me a name and phone!")
    else:
        contact = Contact(cmd[1])    
        book.add_contact(contact)
        items = cmd[2:]
        for item in items:
            if 'phones' in item:
                add_contact_phones(contact, item)
            elif 'email' in item:
                add_contact_email(contact, item)
            elif 'birthday' in item:
                add_contact_birthday(contact, item)

    answer = input("Add some address?").lower()
    if answer in ["y", "yes"]:
        address = input("Type some address >> ")
        contact.address = address
        print(contact)
    else:
        print("Contact just added!")
        print(contact)


def add_contact_phones(contact, string_phones:str):
    '''Add phones to contact'''
    phones = string_phones[7:]
    contact.phones = phones.split(',')


def add_contact_email(contact, string_email:str):
    '''Add email to contact'''
    email = string_email[6:]
    contact.email = email


def add_contact_birthday(contact, string_birthday:str):
    '''Add birthday to contact'''
    birthday = string_birthday[9:]
    contact.birthday = birthday
    
    