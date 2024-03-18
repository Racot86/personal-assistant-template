from bot.src.tools.StorageController import StorageController
import random
from bot.settings import Settings
def tool_bar():
    storage = StorageController()
    qty_contacts = storage.load_contact_book().size()
    qty_notes = len(storage.load_note_book())
    print()
    print(f"{Settings.shadow_color + Settings.msg_color}         TARDIS Personal Assistant{Settings.end_color} v1.0{Settings.end_all}")
    print(f'  {Settings.msg_color}CONTACT BOOK {Settings.end_all}' + Settings.shadow_color + '.' * 25 + Settings.end_all + f' {qty_contacts} {Settings.shadow_color}entries{Settings.end_all}')
    print(f'  {Settings.notes_color}NOTE BOOK {Settings.end_all}' + Settings.shadow_color + '.' * 28 + Settings.end_all + f' {qty_notes} {Settings.shadow_color}entries{Settings.end_all}')
    print(f'  {Settings.error_color}DALEKS EXTERMINATED {Settings.end_all}' + Settings.shadow_color + '.' * 18 + Settings.end_all + f' {random.randrange(1000000,2000000)} {Settings.shadow_color}pcs{Settings.end_all}')
    print()