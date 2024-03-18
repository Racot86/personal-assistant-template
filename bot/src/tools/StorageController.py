from bot.src.classes.class_ContactBook import ContactBook
from bot.src.classes.class_Note import Note
from bot.src.classes.class_NoteBook import NoteBook
from bot.src.classes.class_Contact import Contact
from datetime import datetime
import os
import json
from pathlib import Path


class StorageController:
    def __init__(self):
        self.contact_book = ContactBook()
        self.note_book = NoteBook()

    def __serialise_contact_book(self, data):
        serialised_contact_book = []
        for contact in data:
            serialised_contact_book.append(
                {
                    'name': contact.name,
                    'birthday': contact.birthday,
                    'address': contact.address,
                    'phones': contact.phones,
                    'remark': contact.remark,
                    'email': contact.email,
                }
            )
        return serialised_contact_book

    def __save_serialised_book(self, contact_book, file_name):
        if len(contact_book) >= 0:
            with open(file_name, 'w') as fh:
                fh.write(json.dumps(contact_book))
        else:
            if os.path.exists(file_name):
                os.remove(file_name)

    def save_contact_book(self, contact_book: ContactBook):
        if contact_book.size() >= 0:
            self.__save_serialised_book(self.__serialise_contact_book(contact_book.data), 'contacts.dat')

    def __load_serialised_book(self, file_name):
        if Path.is_file(Path(file_name)):
            with open(file_name, 'r') as fh:
                data = fh.read()
                if data != '':
                    return json.loads(data)
                else:
                    return []
        else:
            return []

    def __deserialise_contact_book(self, book):
        self.contact_book = ContactBook()
        if len(book) > 0:
            for itm in book:
                contact = Contact(itm['name'])
                contact.remark = itm['remark']
                contact.address = itm['address']
                contact.phones = itm['phones']
                contact.email = itm['email']
                contact.birthday = itm['birthday']
                self.contact_book.add_contact(contact)
        return self.contact_book

    def load_contact_book(self):
        self.__deserialise_contact_book(list(self.__load_serialised_book('contacts.dat')))
        return self.contact_book

    def __serialize_note_book(self, note_book):
        if len(note_book) > 0:
            deserialised_list = []
            for itm in note_book:
                deserialised_list.append(
                    {
                        'title': itm.title,
                        'body': itm.body,
                        'time': itm.time,
                        'tags': itm.tags,
                    }
                )
            return deserialised_list
        else:
            return []

    def save_note_book(self, note_book):
        self.__save_serialised_book(self.__serialize_note_book(note_book),'notes.dat')

    def __deserialise_note_book(self, book):
        self.note_book = NoteBook()
        if len(book) > 0:
            for itm in book:
                note = Note(itm['title'])
                note.body = itm['body']
                note.time = datetime.strptime(itm['time'], '%d-%m-%Y %H:%M:%S')
                note.tags = itm['tags']
                self.note_book.append(note)
        return self.note_book

    def load_note_book(self):
        return self.__deserialise_note_book(self.__load_serialised_book('notes.dat'))
