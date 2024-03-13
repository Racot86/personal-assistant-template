#  import classes
from src.classes.class_Contact import Contact
from src.classes.class_ContactBook import ContactBook
from datetime import datetime

def c_show_cmd(cmd):
    print(cmd)
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
        elif "birthdays" in cmd and range_days:
            print("run birthdays" )
            get_birthdays_per_week(contacts, range_days) ## первым аргументом надо добавить наш справочник Notebook
        elif cmd[0] == "show" and cmd[1]:
            print("run birthday Name show")
        else:
            print("Invalid command. Please check your input and try again.")
    except Exception as e:
        print(f"An error occurred: {str(e)}. Please check your input and try again.")

def get_birthdays_per_week(contacts, range_of_days):
    today = datetime.today().date()
    next_birthdays = []

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
            next_birthdays.append(f"{name} will be {age} years old on {date_of_birthday}")

    for birthday in next_birthdays:
        print(birthday)

    return next_birthdays


# def get_birthdays_per_week(users, range_of_days):
   
#     today = datetime.today().date()
    
#     next_birthdays = []

#     #contact in contacts
#     #contact.name
#     #contact.birthday
 
#     # поиск в списке всех именинников на ближайшие x дней, включая текущий день    
#     for user in users:
#         name = user["name"] # contact.name
#         # dd-mm-yyyy
#         birthday = user["birthday"].date()
#         birthday_this_year = birthday.replace(year=today.year)
#         if birthday_this_year < today:
#             birthday_this_year = birthday_this_year.replace(year=today.year + 1)
#         delta_days = (birthday_this_year - today).days
#         if delta_days < range_of_days:
#             age = birthday_this_year.year - birthday.year
#             date_of_birthday = birthday.strftime("%d.%m")
#             next_birthdays.append(f"{name} will be {age} years old on {date_of_birthday}")

#     for birthday in next_birthdays:
#         print(birthday)

#     return next_birthdays

