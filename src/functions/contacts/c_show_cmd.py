#  import classes
from src.classes.class_Contact import Contact
from src.classes.class_ContactBook import ContactBook
from src.tools.StorageController import StorageController
from datetime import datetime
import time
from settings import Settings
from src.tools.a_print import a_print


def c_show_cmd(cmd):

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
            c_show_all()
        elif "birthdays" in cmd and range_days >= 0:
            get_birthdays(range_days) 
        elif cmd[0] == "show" and cmd[1]:
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

    storage = StorageController()
    contacts = storage.load_contact_book()
    no_birthdays = True

    quantity_birthdays = 0
    for contact in contacts:
        if len(contact.birthday)<5:
            continue
        quantity_birthdays += 1
        name = contact.name
        birthday = datetime.strptime(contact.birthday, '%d-%m-%Y').date()
        # TODO: uncomment and resolve empty birthday problem
        # output(f"TARDIS: {Settings.success_color}Founded:{Settings.end_all}")
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        delta_days = (birthday_this_year - today).days
        
        if delta_days < range_of_days:
            age = birthday_this_year.year - birthday.year
            date_of_birthday = birthday.strftime("%d.%m")

            birthday_text = f"{Settings.msg_color}{name} will be {age} years old on {date_of_birthday}{Settings.end_all}"
            a_print(birthday_text, used_colors=[Settings.msg_color,Settings.end_all])
            no_birthdays = False

    if quantity_birthdays==0:
        output(f"TARDIS: {Settings.warning_color}No contacts match this period'{Settings.end_all}")
    if no_birthdays:
        output(f"TARDIS: {Settings.error_color}I'm sorry, my Lord. We don't have birthdays next {range_of_days} days{Settings.end_all}")

    return next_birthdays


def c_show_all():
    storage = StorageController()
    contacts = storage.load_contact_book()
    output(Settings.msg_color + "Name             Phones           Remark")
    output("-" * 44)

    for contact in contacts:
        name = contact.name
        phones = ', '.join(contact.phones) if contact.phones else ""
        remark = contact.remark if contact.remark else ""
        row = "{:<16} {:<16} {:<16}".format(name, phones, remark)
        output(row)
        
    print(Settings.end_all)


def search_contact_by_name(name):
    storage = StorageController()
    contacts = storage.load_contact_book()

    contact = contacts.get_contact(name)
    if contact:
        output(f"TARDIS: {Settings.success_color}Look which data I found for '{name}':{Settings.end_all}")
        if contact.remark:
            print(f"{Settings.shadow_color}  Name: {Settings.end_all}{contact.name} ({contact.remark})")
        else:
            print(f"{Settings.shadow_color}  Name: {Settings.end_all}{contact.name}")
        if len(contact.phones):
            print(f"{Settings.shadow_color}  Phones: {Settings.end_all}{', '.join(contact.phones)}")
        if contact.email:
            print(f"{Settings.shadow_color}  E-mail: {Settings.end_all}{contact.email}")
        if contact.address:
            print(f"{Settings.shadow_color}  Address: {Settings.end_all}{contact.address}")
        if contact.birthday:
            print(f"{Settings.shadow_color}  Birthday: {Settings.end_all}{contact.birthday}")
    else:
        output(f"{Settings.error_color}I'm sorry, my Lord. We don't have info about '{name}' in our contacts{Settings.end_all}")
