'''Contact change command'''

from src.tools.StorageController import StorageController
from settings import Settings

def c_change_cmd(cmd):
    '''
    Changing the contact from command (cmd)
    Where 
        cmd[0] - string 'change'
        cmd[1] - contact name
        cmd[2], cmd[3], - optional: strings 'phones:XXXXXXXXXX,XXXXXXXXXX', 'email:asd@jhg', 'birthday:12.12.2012'
    '''
    storage_controller = StorageController()
    contacts = storage_controller.load_contact_book()
    if len(cmd) < 2:
        # cmd isn't contains a name
        print(f"{Settings.warning_color}My Lord, you forget enter a name?{Settings.end_color}")
    else:
        contact = contacts.get_contact(cmd[1])
        if contact:
            if len(cmd) == 2:
                # cmd contains only name of searching contact
                value = input(f"{Settings.msg_color}What you want to change? Phones, email, address or birthday? {Settings.end_color}")
                if 'phones' in value.lower():
                    phones = input(f"{Settings.msg_color}Ok, input phone or phones by comma: {Settings.end_color}")
                    contact.phones = phones.split(',')
                    save(contacts, contact)
                    print(f"{Settings.success_color}New phone saved, my Lord!{Settings.end_color}")
                elif 'email' in value.lower():
                    email = input(f"{Settings.msg_color}Ok, input email: {Settings.end_color}")
                    contact.email = email
                    save(contacts, contact)
                    print(f"{Settings.success_color}New email saved, my Lord!{Settings.end_color}")
                elif 'birthday' in value.lower():
                    birthday = input(f"{Settings.msg_color}Ok, input birthday in next format 23-10-2005: {Settings.end_color}")
                    contact.birthday = birthday
                    save(contacts, contact)
                    print(f"{Settings.success_color}New birthday saved, my Lord!{Settings.end_color}")
                elif 'address' in value.lower():
                    address = input(f"{Settings.msg_color}Ok, input address: {Settings.end_color}")
                    contact.address = address
                    save(contacts, contact)
                    print(f"{Settings.success_color}New address saved, my Lord!{Settings.end_color}")
                else:
                    print(f"{Settings.error_color}Sorry, my Lord, I can't recognize this command...{Settings.end_color}")
            print(contact) #TODO: remove after testing?
        else:
            print(f"{Settings.error_color}Sorry, my Lord, but contact is not found..{Settings.end_color}")


def save(contacts, contact):
    '''Save contacts on disk'''
    storage_controller = StorageController()
    contacts.add_contact(contact)
    storage_controller.save_contact_book(contacts)