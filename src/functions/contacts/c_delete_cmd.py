# from src.tools.load_contacts import load_contacts
# from src.tools.save_contacts import save_contacts
# from src.classes.class_ContactBook import ContactBook
# from src.classes.class_Contact import Contact
from src.tools.StorageController import StorageController 


# def c_delete_cmd(cmd):
#     contacts = ContactBook(load_contacts())
#     contact = Contact('Dmytro')
#     contact.birthday = '04-06-1986'
#     contacts.add_contact(contact)
#     contacts.delete_contact(contact)
#     print(contacts[0])

#     save_contacts(contacts)


def c_delete_cmd(cmd):
    if len(cmd) != 2:
        print('My lord, I need to see the command and one enemy... Write it down for me.')
        return
    
    storage = StorageController()
    contacts = storage.load_contact_book()
    # contacts = ContactBook(load_contacts())

    contact_name = cmd[1]
    contact = contacts.get_contact(contact_name)
    if contact:
        contacts.delete_contact(contact)
        # save_contacts(contacts)
        storage.save_contact_book(contacts)
        print(f"Enemy '{contact_name}' is defeated by being destroyed.")        
    else:
        print(f"Enemy '{contact_name}' was early defeated. Write me new name.")



