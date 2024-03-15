
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
        print(f"TARDIS: {Settings.msg_color}My Lord, you forget enter a name?{Settings.end_color}")
    else:
        if contacts.contact_exists(cmd[1]):
            print(f"TARDIS: {Settings.error_color}Entry already exists, my Lord!{Settings.end_color}")
        else:
            contact = Contact(cmd[1])
            items = cmd[2:]
            errors = []
            for item in items:
                if 'phones' in item:
                    response = add_contact_phones(contact, item)
                    if len(response)>0:
                        errors.append(response)
                elif 'email' in item:
                    response = add_contact_email(contact, item)
                    if len(response)>0:
                        errors.append(response)
                elif 'birthday' in item:
                    response = add_contact_birthday(contact, item)
                    if len(response)>0:
                        errors.append(response)

            if len(errors)>0:
                errors_str = ", ".join(errors)
            #     print(f"TARDIS: {Settings.error_color}Wrong format in next fields: {errors_str}, see help, my Lord!{Settings.end_color}")
            else:
                answer = input(f"TARDIS: {Settings.msg_color}Add some address? (yes/no) {Settings.end_color}").lower()
                if answer in ["y", "yes"]:
                    address = input(f"TARDIS: {Settings.msg_color}Type some address: {Settings.end_color}")
                    contact.address = address

                print(f"TARDIS: {Settings.success_color}Contact added successfuly!{Settings.end_color}")
                contacts.add_contact(contact)
                storage_controller.save_contact_book(contacts)



def add_contact_phones(contact, string_phones:str):
    '''Add phones to contact'''
    phones = string_phones[7:]
    contact.phones = phones.split(',')
    error = ''
    if len(contact.phones)==0:
        error = 'phones'
    return error


def add_contact_email(contact, string_email:str):
    '''Add email to contact'''
    email = string_email[6:]
    contact.email = email
    error = ''
    if contact.email=='':
        error = 'email'
    return error


def add_contact_birthday(contact, string_birthday:str):
    '''Add birthday to contact'''
    birthday = string_birthday[9:]
    contact.birthday = birthday
    error = ''
    if contact.birthday=='':
        error = 'birthday'
    return error
