'''Contact change command'''

from src.tools.StorageController import StorageController
from settings import Settings

def c_change_cmd(cmd):
    '''
    Changing the contact from command (cmd)
    Where 
        cmd[0] - string 'change'
        cmd[1] - contact name
        cmd[2], cmd[3], - optional: strings 'phones:XXXXXXXXXX,XXXXXXXXXX', 'email:asd@jhg', 'birthday:12.12.2012, remark:some remark'
    '''
    storage_controller = StorageController()
    contacts = storage_controller.load_contact_book()
    if len(cmd) < 2:
        # cmd isn't contains a name
        print(f"TARDIS: {Settings.warning_color}My Lord, you forget enter a name?{Settings.end_color}")
    else:
        contact = contacts.get_contact(cmd[1])
        is_contact_change = False
        if contact is not False:
            if len(cmd) == 2:
                # cmd contains only name of searching contact
                value = input(f"TARDIS: {Settings.msg_color}What you want to change? Phones, email, address, birthday or remark? {Settings.end_color}")
                if 'phones' in value.lower():
                    phones = input(f"TARDIS: {Settings.msg_color}Ok, input phone or phones by comma: {Settings.end_color}")
                    contact.phones = phones.split(',')
                    is_contact_change = True
                    print(f"TARDIS: {Settings.success_color}New phone saved, my Lord!{Settings.end_color}")
                elif 'email' in value.lower():
                    email = input(f"TARDIS: {Settings.msg_color}Ok, input email: {Settings.end_color}")
                    contact.email = email
                    is_contact_change = True
                    print(f"TARDIS: {Settings.success_color}New email saved, my Lord!{Settings.end_color}")
                elif 'birthday' in value.lower():
                    birthday = input(f"TARDIS: {Settings.msg_color}Ok, input birthday in next format 23-10-2005: {Settings.end_color}")
                    contact.birthday = birthday
                    is_contact_change = True
                    print(f"TARDIS: {Settings.success_color}New birthday saved, my Lord!{Settings.end_color}")
                elif 'address' in value.lower():
                    address = input(f"TARDIS: {Settings.msg_color}Ok, input address: {Settings.end_color}")
                    contact.address = address
                    is_contact_change = True
                    print(f"TARDIS: {Settings.success_color}New address saved, my Lord!{Settings.end_color}")
                elif 'remark' in value.lower():
                    remark = input(f"TARDIS: {Settings.msg_color}Ok, input remark: {Settings.end_color}")
                    contact.remark = remark
                    is_contact_change = True
                    print(f"TARDIS: {Settings.success_color}New remark saved, my Lord!{Settings.end_color}")
                else:
                    print(f"TARDIS: {Settings.error_color}Sorry, my Lord, I can't recognize this command...{Settings.end_color}")
            if is_contact_change:
                storage_controller = StorageController()
                storage_controller.save_contact_book(contacts)
        else:
            print(f"TARDIS: {Settings.error_color}Sorry, my Lord, but contact is not found..{Settings.end_color}")
