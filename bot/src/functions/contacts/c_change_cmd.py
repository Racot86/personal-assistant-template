'''Contact change command'''

from bot.src.tools.StorageController import StorageController
from bot.settings import Settings
from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit import prompt
from bot.src.tools.a_print import a_print
from prompt_toolkit.styles import Style

completer = NestedCompleter.from_nested_dict({
    'phones': None,
    'emails': None,
    'address': None,
    'remark': None,
    'birthday': None
})


style = Style.from_dict({
    '': Settings.PROMPT_INPUT_COLOR,
    'prompt': Settings.PROMPT_TEXT_COLOR
})


def c_change_cmd(cmd):
    '''
    Changing the contact from command (cmd)
    Where 
        cmd[0] - string 'change'
        cmd[1] - contact name
        cmd[2], cmd[3], - optional: strings 'phones:XXXXXXXXXX,XXXXXXXXXX', 'email:asd@jhg', 'birthday:12.12.2012, remark:some remark'
    '''
    storage_controller = StorageController()
    contacts = storage_controller.load_contact_book()
    if len(cmd) < 2:
        # cmd isn't contains a name
        a_print(f"My Lord, you forget enter a name?", prefix = Settings.TARDIS, main_color=Settings.warning_color)
    else:
        contact = contacts.get_contact(cmd[1])
        is_contact_change = False
        if contact is not False:
            if len(cmd) == 2:
                # cmd contains only name of searching contact
                print(f"TARDIS:")
                value = prompt(f"  What you want to change? phones, email, address, birthday or remark? ", complete_while_typing=True, completer=completer, style=style)
                if 'phones' in value.lower():
                    phones = input(
                        f"TARDIS: {Settings.msg_color}Ok, input phone or phones by comma: {Settings.end_color}")
                    contact.phones = phones.split(',')
                    is_contact_change = contact.phones == phones.split(',')
                elif 'email' in value.lower():
                    email = input(f"TARDIS: {Settings.msg_color}Ok, input email: {Settings.end_color}")
                    contact.email = email
                    is_contact_change = contact.email == email
                elif 'birthday' in value.lower():
                    birthday = input(
                        f"TARDIS: {Settings.msg_color}Ok, input birthday in next format 23-10-2005: {Settings.end_color}")
                    contact.birthday = birthday
                    is_contact_change = contact.birthday == birthday
                elif 'address' in value.lower():
                    address = input(f"TARDIS: {Settings.msg_color}Ok, input address: {Settings.end_color}")
                    contact.address = address
                    is_contact_change = contact.address == address
                elif 'remark' in value.lower():
                    remark = input(f"TARDIS: {Settings.msg_color}Ok, input remark: {Settings.end_color}")
                    contact.remark = remark
                    is_contact_change = contact.remark == remark
                else:
                    a_print(f"Sorry, my Lord, I can't recognize this command...", prefix = Settings.TARDIS, main_color=Settings.error_color)
            if is_contact_change:
                storage_controller = StorageController()
                storage_controller.save_contact_book(contacts)
                a_print(f"Your's changes is currently added, my Lord!", prefix = Settings.TARDIS, main_color=Settings.success_color)
        else:
            a_print(f"Sorry, my Lord, but contact is not found..", prefix = Settings.TARDIS, main_color=Settings.error_color)
