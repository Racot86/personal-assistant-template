from src.tools.StorageController import StorageController 
# from src.classes.class_Contact import Contact







def c_delete_cmd(cmd):
    if len(cmd) != 2:
        print('My lord, I need to see the command and one enemy... Write it down for me.')
        return
    
    storage = StorageController()
    contacts = storage.load_contact_book()

    # contact = Contact('Dmytro')
    # contact.birthday = '04-06-1986'
    # contacts.add_contact(contact)

    contact_name = cmd[1]
    contact = contacts.get_contact(contact_name)
    if contact:
        contacts.delete_contact(contact)
        storage.save_contact_book(contacts)
        print(f"Enemy '{contact_name}' is defeated by being destroyed.")        
    else:
        print(f"Enemy '{contact_name}' was early defeated. Write me new name.")


