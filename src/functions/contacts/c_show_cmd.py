#  import classes
from src.classes.class_Contact import Contact
from src.classes.class_ContactBook import ContactBook
from src.tools.StorageController import StorageController
from datetime import datetime
from colorama import Fore, Back, Style
import time
import sys


def c_show_cmd(cmd):
    #print(cmd)
    range_days = None
    if not cmd:
        print("Empty command. Please enter a command.")
        return
    
    try:  

        for item in cmd:
            try:
                range_days = int(item)
            except ValueError:
                pass

        if "all" in cmd and "show" in cmd:
            print("run Show all")
            c_show_all()
        elif "birthdays" in cmd and range_days:
            print("run birthdays" )
            get_birthdays_per_week(range_days) ## первым аргументом надо добавить наш справочник Notebook
        elif cmd[0] == "show" and cmd[1]:
            print("run birthday Name show")
        else:
            print("Invalid command. Please check your input and try again.")
    except Exception as e:
        print(f"An error occurred: {str(e)}. Please check your input and try again.")

def get_birthdays_per_week(range_of_days):
    today = datetime.today().date()
    next_birthdays = []

    storage = StorageController()
    contacts = storage.load_contact_book()

    for contact in contacts:
        name = contact.name
        #print(contact.birthday)
        birthday = datetime.strptime(contact.birthday, '%d-%m-%Y').date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        delta_days = (birthday_this_year - today).days
        if delta_days < range_of_days:
            age = birthday_this_year.year - birthday.year
            date_of_birthday = birthday.strftime("%d.%m")
            next_birthdays.append(f"{name} will be {age} years old on {date_of_birthday}")

    for birthday in next_birthdays:
        print(birthday)

    return next_birthdays


def c_show_all():

    storage = StorageController()
    contacts = storage.load_contact_book()

    headers = ["Name", "Phones", "E-mail", "Address", "Birthday", "Remark"]
    row_format = "{:<20} {:<12} {:<30} {:<30} {:<12} {:<25}"
    print(row_format.format(*headers))  # Выводим заголовки таблицы
    print("-" * 129)  # Выводим разделительную линию

    for contact in contacts:
        # Собираем данные из каждого контакта
        name = contact.name
        phones = ', '.join(contact.phones) if contact.phones else ""
        email = contact.email if contact.email else ""
        address = contact.address if contact.address else ""
        birthday = contact.birthday if contact.birthday else ""
        remark = contact.remark if contact.remark else ""
        
        # Выводим данные контакта, форматируя в строку в соответствии с заданным форматом
        print(row_format.format(name, phones, email, address, birthday, remark))

        