import pickle, os


def save_contacts(data):
    if len(data) > 0:
        with open('contacts.bin', 'wb') as fh:
            pickle.dump(data, fh)
    else:
        if os.path.exists("contacts.bin"):
            os.remove("contacts.bin")
