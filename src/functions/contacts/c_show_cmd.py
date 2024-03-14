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
            #print("run Show all")
            c_show_all()
        elif "birthdays" in cmd and range_days >= 0:
            #print("run birthdays" )
            get_birthdays(range_days) 
        elif cmd[0] == "show" and cmd[1]:
            #print("run birthday Name show")
            search_contact_by_name(cmd[1])
        else:
            print("Invalid command. Please check your input and try again.")
    except Exception as e:
        print(f"An error occurred: {str(e)}. Please check your input and try again.")

def output(text):
    delay = 0.01  
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  


def get_birthdays(range_of_days):
    today = datetime.today().date()
    next_birthdays = []
    #print(today)

    storage = StorageController()
    contacts = storage.load_contact_book()
    no_birthdays = True

    for contact in contacts:
        name = contact.name
        birthday = datetime.strptime(contact.birthday, '%d-%m-%Y').date()
        
        birthday_this_year = birthday.replace(year=today.year)
        #print(birthday_this_year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        delta_days = (birthday_this_year - today).days
        #print(delta_days)
        if delta_days < range_of_days:
            age = birthday_this_year.year - birthday.year
            date_of_birthday = birthday.strftime("%d.%m")

            birthday_text = f"{Fore.YELLOW}{name} will be {age} years old on {date_of_birthday}{Style.RESET_ALL}"
            output(birthday_text)
            no_birthdays = False

    if no_birthdays:
        output(f"{Fore.RED}I'm sorry, my Lord. We don't have birthdays next {range_of_days} days{Style.RESET_ALL}")

    return next_birthdays


def c_show_all():
    storage = StorageController()
    contacts = storage.load_contact_book()
    output(Fore.GREEN + "Name             Phones           Remark")
    output("-" * 44)

    for contact in contacts:
        name = contact.name
        phones = ', '.join(contact.phones) if contact.phones else ""
        remark = contact.remark if contact.remark else ""
        row = "{:<16} {:<16} {:<16}".format(name, phones, remark)
        output(row)
        
    print(Style.RESET_ALL)


def search_contact_by_name(name):
    storage = StorageController()
    contacts = storage.load_contact_book()

    found_contacts = []
    for contact in contacts:
        if contact.name.lower() == name.lower():
            found_contacts.append(contact)

    if found_contacts:
        output(f"{Fore.GREEN}Found contact(s) with name '{name}':{Style.RESET_ALL}")

        for contact in found_contacts:
            #contact_info = f"Name: {contact.name}, Phones: {', '.join(contact.phones)}, E-mail: {contact.email}, Address: {contact.address}, Birthday: {contact.birthday}, Remark: {contact.remark}"
            #output(contact_info)
            contact_info = str(contact)
            for line in contact_info.splitlines():
                output(line)
    else:
        output(f"{Fore.RED}I'm sorry, my Lord. We don't have info about '{name}' in our contacts{Style.RESET_ALL}")
