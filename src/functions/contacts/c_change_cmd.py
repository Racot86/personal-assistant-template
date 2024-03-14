'''Contact change command'''

from src.tools.StorageController import StorageController

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
    print(len(cmd))
    if len(cmd) < 2:
        # cmd isn't contains a name
        print("My Lord, you forget enter a name?")
    else:
        print(contacts)
        contact = contacts.get_contact(cmd[1])
        if contact:
            if len(cmd) == 2:
                # cmd contains only name of searching contact
                value = input("What you want to change? Phones, email, address or birthday? ")
                if 'phones' in value.lower():
                    phones = input("Ok, input phone or phones by comma: ")
                    contact.phones = phones.split(',')
                    print("New phone saved, my Lord!")
                elif 'email' in value.lower():
                    email = input("Ok, input email: ")
                    contact.email = email
                    print("New email saved, my Lord!")
                elif 'birthday' in value.lower():
                    birthday = input("Ok, input birthday in next format 23-10-2005: ")
                    contact.birthday = birthday
                    print("New birthday saved, my Lord!")
                elif 'address' in value.lower():
                    address = input("Ok, input address: ")
                    contact.address = address
                    print("New address saved, my Lord!")
                else:
                    print("Sorry, my Lord, I can't recognize this command...")
            else:
                print("Sorry, my Lord, but contact is not found..")
            print(contact) #TODO: remove after testing?
        else:
            print("Sorry, my Lord, but contact not found..")
