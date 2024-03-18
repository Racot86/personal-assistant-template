from bot.src.tools.StorageController import StorageController 
from bot.settings import Settings

def c_delete_cmd(cmd):
    if len(cmd) != 2:
        print(f"{Settings.warning_color}My lord, I need to see the command and one enemy... Write it down for me.")
        return
    
    storage = StorageController()
    contacts = storage.load_contact_book()

    contact_name = cmd[1]
    contact = contacts.get_contact(contact_name)
    if contact is not False:
        contacts.delete_contact(contact)
        storage.save_contact_book(contacts)
        print(f"{Settings.success_color}Enemy '{contact_name}' is defeated by being destroyed.")        
    else:
        print(f"{Settings.warning_color}Enemy '{contact_name}' was early defeated. Write me new name.")
