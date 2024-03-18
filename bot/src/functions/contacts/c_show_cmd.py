#  import classes
from bot.src.classes.class_Contact import Contact
from bot.src.classes.class_ContactBook import ContactBook
from bot.src.tools.StorageController import StorageController
from datetime import datetime
import time
from bot.settings import Settings
from bot.src.tools.a_print import a_print


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
            a_print("Do not disappoint me. Please check your input and try again.",
                    prefix=Settings.TARDIS, main_color=Settings.error_color)
    except Exception as e:
        a_print(f"Oops, an error occurred: {str(e)}. Please open your eyes and try again.",
                prefix=Settings.TARDIS, main_color=Settings.error_color)

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
    a_print('Let me check what I have for your request...', prefix=Settings.TARDIS, main_color=Settings.msg_color)
    for contact in contacts:
        if len(contact.birthday)<5:
            continue
        quantity_birthdays += 1
        name = contact.name
        birthday = datetime.strptime(contact.birthday, '%d-%m-%Y').date()
        #  output(f"TARDIS: {Settings.success_color}Founded:{Settings.end_all}")
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        delta_days = (birthday_this_year - today).days
        
        if delta_days < range_of_days:
            age = birthday_this_year.year - birthday.year
            date_of_birthday = birthday.strftime("%d.%m")

            birthday_text = f"  {Settings.msg_color}{name}{Settings.shadow_color} will be{Settings.end_all + Settings.msg_color} {age} {Settings.shadow_color}years old on{Settings.end_all + Settings.msg_color} {date_of_birthday}{Settings.end_all}"
            a_print(birthday_text, used_colors=[Settings.msg_color,Settings.end_all])
            no_birthdays = False

    if quantity_birthdays==0:
        output(f"{Settings.TARDIS}{Settings.warning_color}No contacts match this period'{Settings.end_all}")
    if no_birthdays:
        output(f"{Settings.TARDIS}{Settings.error_color}I'm sorry, my Lord. We don't have birthdays next {range_of_days} days{Settings.end_all}")

    return next_birthdays


def c_show_all():
    storage = StorageController()
    contacts = storage.load_contact_book()
    a_print('Following contacts are present in the contact book:',
            prefix=Settings.TARDIS, main_color=Settings.msg_color)
    output(Settings.shadow_color + "  Name             Phones           Remark" + Settings.end_all)
    #  output("-" * 44)

    for contact in contacts:
        name = contact.name
        phones = ', '.join(contact.phones) if contact.phones else ""
        remark = contact.remark if contact.remark else ""
        row = "  {:<16} {:<16} {:<16}".format(name, phones, remark)
        output(Settings.msg_color + row + Settings.end_color)
        
    print(Settings.end_all)


def search_contact_by_name(name):
    storage = StorageController()
    contacts = storage.load_contact_book()

    contact = contacts.get_contact(name)
    if contact:
        output(f"{Settings.TARDIS}{Settings.msg_color}Look which data I found for '{name}':{Settings.end_all}")
        if contact.remark:
            print(f"  {Settings.shadow_color}  Name: {Settings.end_all}{contact.name} ({contact.remark})")
        else:
            print(f"  {Settings.shadow_color}  Name: {Settings.end_all}{contact.name}")
        if len(contact.phones):
            print(f"  {Settings.shadow_color}  Phones: {Settings.end_all}{', '.join(contact.phones)}")
        if contact.email:
            print(f"  {Settings.shadow_color}  E-mail: {Settings.end_all}{contact.email}")
        if contact.address:
            print(f"  {Settings.shadow_color}  Address: {Settings.end_all}{contact.address}")
        if contact.birthday:
            print(f"  {Settings.shadow_color}  Birthday: {Settings.end_all}{contact.birthday}")
    else:
        output(f"{Settings.TARDIS}{Settings.error_color}I'm sorry, my Lord. We don't have info about '{name}' in our contacts{Settings.end_all}")
