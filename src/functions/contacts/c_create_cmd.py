
'''Contact create command'''

from src.tools.StorageController import StorageController
from src.classes.class_Contact import Contact
from settings import Settings

def c_create_cmd(cmd):
    '''
    Creating a contact from command (cmd)
    Where 
        cmd[0] - string 'create'
        cmd[1] - contact name
        cmd[2], cmd[3], - optional: strings 'phones:XXXXXXXXXX,XXXXXXXXXX', 'email:some@dot.com', 'birthday:12.12.2012'
    '''

    storage_controller = StorageController()
    contacts = storage_controller.load_contact_book()

    if len(cmd)<2:
        print(f"{Settings.msg_color}My Lord, you forget enter a name?{Settings.end_color}")
    else:
        if contacts.contact_exists(cmd[1]):
            print(f"{Settings.error_color}Entry already exists, my Lord!{Settings.end_color}")
        else:
            contact = Contact(cmd[1])
            items = cmd[2:]
            for item in items:
                if 'phones' in item:
                    add_contact_phones(contact, item)
                elif 'email' in item:
                    add_contact_email(contact, item)
                elif 'birthday' in item:
                    add_contact_birthday(contact, item)

            answer = input(f"{Settings.msg_color}Add some address? (yes/no) {Settings.end_color}").lower()
            if answer in ["y", "yes"]:
                address = input(f"{Settings.msg_color}Type some address >> {Settings.end_color}")
                contact.address = address

            print(f"{Settings.success_color}Contact added successfuly!{Settings.end_color}")
            contacts.add_contact(contact)
            storage_controller.save_contact_book(contacts)
            print(contact) #TODO: remove after testing?



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
