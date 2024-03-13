from src.tools.StorageController import StorageController 

def c_search_cmd(cmd):

    if len(cmd) != 2:
        print('My lord, I need to see the command and one thing about enemy... Write it down for me.')
        return
    
    storage = StorageController()
    contacts = storage.load_contact_book()

    search_param = cmd[1]
       
    if search_param:
        found_contact = None

        
        for contact in contacts:
            if contact.name.lower() == search_param.lower():
                found_contact = contact
                break

        
        if not found_contact:
            for contact in contacts:
                if search_param in contact.phones:
                    found_contact = contact
                    break

        
        if not found_contact:
            for contact in contacts:
                if search_param.lower() == contact.email.lower():
                    found_contact = contact
                    break
        
        if not found_contact:
            for contact in contacts:
                if search_param == contact.birthday:
                    found_contact = contact
                    break
                
        if found_contact:
            print(f"Contact found:\n{found_contact}")
        else:
            print(f"No contact found with '{search_param}'")
    