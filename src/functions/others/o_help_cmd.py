from settings import Settings
from src.tools.a_print import a_print


def o_help_cmd(cmd):
    help_list = [
        {"cmd": "contacts create",
         "syntax": "`contacts create` `name*` [`phones:phone,phone`] [`email:email`] [`birthday:dd-mm-YYYY`]",
         "description": "name - is required, all the rest parameters are optional and can be one or can be any number of it",
         "examples": "contacts create Luck 0500000000"
         },
        {"cmd": "contacts change",
         "syntax": "contacts change` `name*`  [`phones:phone,phone`] [`email:email`] [`birthday:dd-mm-YYYY`]",
         "description": "same idea as create - name is required and others are the parameters you want to change",
         "examples": "contacts change Luck 0501111111 luck@skywalker.com"
         },
        {"cmd": "contacts delete",
         "syntax": "contacts delete <name>",
         'description': 'This command deletes the specified contact',
         'examples': 'contacts delete name'
         },
        {'cmd': 'contacts search',
         'syntax': 'contacts search <name> / contacts search <phone> / contacts search <email>',
         'description': 'This command searches for a contact by name, phone number or email',
         'examples': 'contacts search name / contacts search 0630004400 / contacts search test@email.com'
         },
        {'cmd': "contacts show all",
         'syntax': "command does not require any additional parameters, it is used as is",
         'description': "this command shows the content of the contact book (fields name, phone number, remark)",
         'examples': "contacts show all"
         },
        {"cmd": "contacts show",
         "syntax": "contacts filter by tag <name>, use only one name, shows all the matches",
         "description": "This command searches and displays contacts filtered by birthdays in the next few days",
         "examples": "contacts show Dmitry"
         },
        {"cmd": "contacts show birthdays",
         "syntax": "contacts show birthdays <range> days",
         "description": "filters the contact book by birthdays in the next few days",
         "examples": "contacts show birthdays 7 days"
         },
        {'cmd': 'notes create',
         'syntax': 'notes create <title> / <body>',
         'description': 'add note to note book',
         'examples': 'notes create <title: borscht> / <body:Ukrainian Borscht everyone knows'
         },
        {'cmd': 'notes change',
         'syntax': 'notes change <title> / <body>',
         'description': 'changes note',
         'examples': 'notes change <title: borscht>  enter new title:<new_title>  enter new body:<new_body>'
         },
        {'cmd': 'notes delete',
         'syntax': 'notes delete <title>',
         'description': 'delete note from note book',
         'examples': 'notes delete <title:borscht>'
         },
        {'cmd': 'notes search',
         'syntax': 'notes search, notes search <title>, notes search <body>',
         'description': 'search note in note book',
         'examples': 'notes search, notes search <egg>'
         },
        {'cmd': 'notes show',
         'syntax': 'notes show, notes show <title>',
         'description': 'show note from note book',
         'examples': 'notes show, notes show cooking instruction'
         },
         {'cmd': 'notes filter by tag',
         'syntax': 'notes filter by tag <insert any number of tags with # and space between>',
         'description': 'This command searches and displays notes filtered by given tags',
         'examples': 'notes filter by tag #test, notes filter by tag #test #dummy'
         },
        {'cmd': 'about',  # name of command. I will use this field for search
         'syntax': 'about',  # how to call command properly
         'description': 'Information about app',  # Explanation what this command does
         'examples': 'about'  # examples of command usage
         },
        {"cmd": "hello",
         "syntax": "command does not require any additional parameters, it is used as is",
         "description": "some funny greating",
         "examples": "hello"
         },
        {"cmd": "help",
         "syntax": "command does not require any additional parameters, it is used as is",
         "description": "description of all bot commands functioning in the program",
         "examples": "help"
         },
        {'cmd': 'war statistics',  # name of command. I will use this field for search
         'syntax': 'war statistics today/war statistics mm-dd-yyyy',  # how to call command properly
         'description': 'Get statistics about war in Ukraine',  # Explanation what this command does
         'examples': 'war statistics today, war statistics 14-03-2022'  # examples of command usage
         }
    ]

    if len(cmd) == 1:
        a_print('Doctor, please find below list of commands which I currently know', prefix='TARDIS: ',
                main_color=Settings.msg_color)
        for itm in help_list:
            print(f'  {Settings.notes_color}Command name: {Settings.end_all}' + itm['cmd'])
            print(f'  {Settings.notes_color}Syntax: {Settings.end_all}' + itm['syntax'])
            print(f'  {Settings.notes_color}Description: {Settings.end_all}' + itm['description'])
            print(f'  {Settings.notes_color}Examples: {Settings.end_all}' + itm['examples'])
            print()
