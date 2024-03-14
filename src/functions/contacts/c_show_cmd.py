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
            print("run birthday Name show")
            search_contact_by_name(cmd[1])
        else:
            print("Invalid command. Please check your input and try again.")
    except Exception as e:
        print(f"An error occurred: {str(e)}. Please check your input and try again.")

def get_birthdays(range_of_days):
    today = datetime.today().date()
    next_birthdays = []

    storage = StorageController()
    contacts = storage.load_contact_book()

    no_birthdays = True

    for contact in contacts:
        name = contact.name
        birthday = datetime.strptime(contact.birthday, '%d-%m-%Y').date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        delta_days = (birthday_this_year - today).days
        if delta_days < range_of_days:
            age = birthday_this_year.year - birthday.year
            date_of_birthday = birthday.strftime("%d.%m")
            
            birthday_text = f"{Fore.YELLOW}{name} will be {age} years old on {date_of_birthday}{Style.RESET_ALL}"
            #print(birthday_text)
            for char in birthday_text:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)  
            print()  
            no_birthdays = False  



    if no_birthdays:
        birthday_text = f"{Fore.RED}I'm sorry, my Lord. We don't have birthdays next {range_of_days} days{Style.RESET_ALL}"
        for char in birthday_text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)  
        print()
            
    return next_birthdays



def c_show_all():
    storage = StorageController()
    contacts = storage.load_contact_book()

    headers = ["Name", "Phones", "E-mail", "Address", "Birthday", "Remark"]
    row_format = "{:<16} {:<12} {:<25} {:<20} {:<12} {:<25}"
    header_row = row_format.format(*headers)
    print(Fore.GREEN + header_row)
    print("-" * 110)

    for contact in contacts:
      
        name = contact.name
        phones = ', '.join(contact.phones) if contact.phones else ""
        email = contact.email if contact.email else ""
        address = contact.address if contact.address else ""
        birthday = contact.birthday if contact.birthday else ""
        remark = contact.remark if contact.remark else ""
        
        row = row_format.format(name, phones, email, address, birthday, remark)
        
        for char in row:
            print(Fore.YELLOW + char, end="", flush=True)  
            time.sleep(0.02)  
        print()  
        sys.stdout.write(Style.RESET_ALL) 

def search_contact_by_name(name):
    storage = StorageController()
    contacts = storage.load_contact_book()
  
    found_contacts = []
    for contact in contacts:
        if contact.name.lower() == name.lower():
            found_contacts.append(contact)

    if found_contacts:

        print(f"{Fore.GREEN}Found contact(s) with name '{name}':{Style.RESET_ALL}")

        for contact in found_contacts:
            contact_info = f"Name: {contact.name}, Phones: {', '.join(contact.phones)}, E-mail: {contact.email}, Address: {contact.address}, Birthday: {contact.birthday}, Remark: {contact.remark}"
            for char in contact_info:
                print(Fore.YELLOW + char, end="", flush=True)
                time.sleep(0.02)
            print(Style.RESET_ALL) 
            time.sleep(0.2) 
    else:
        print(f"{Fore.RED}I'm sorry, my Lord. We don't have info about '{name}' in our contacts{Style.RESET_ALL}")
   
        