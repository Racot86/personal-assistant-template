def o_help_cmd(cmd):

    help_list = [
        {'cmd': 'notes filter by tag',
         'syntax': 'notes filter by tag <insert any number of tags with # and space between>',
         'description': 'This command searches and displays notes filtered by given tags',
         'examples': 'notes filter by tag #test'
         },
        {'cmd': '',  # name of command. I will use this field for search
         'syntax': '',  # how to call command properly
         'description': '',  # Explanation what this command does
         'examples': ''  # examples of command usage
         },
         {'cmd': "contacts show all",
         'syntax': "command does not require any additional parameters, it is used as is",
         'description': "this command shows the content of the contact book (fields name, phone number, remark)",
         'examples': "contacts show all"
         },
         {'cmd': "contacts show <name>",
         'syntax': "contacts filter by tag <name>, useы only one name, shows all the matches",
         'description': "This command searches and displays contacts filtered by birthdays in the next few days",
         'examples': "contacts show Dmitry"
         },
         {'cmd': "contacts show birthdays <range>",
         'syntax': "filters the contact book by birthdays in the next <range> days",
         'description': "filters the contact book by birthdays in the next few days",
         'examples': "contacts show Dmitry"
         },
         {'cmd': 'contacts delete',  
         'syntax': 'contacts delete <name>', 
         'description': 'This command deletes the specified contact',  
         'examples': 'contacts delete name'  
         },
         {'cmd': 'contacts search',  
         'syntax': 'contacts search <name> / contacts search <phone> / contacts search <email>', 
         'description': 'This command searches for a contact by name, phone number or email',  
         'examples': 'contacts search name / contacts search 0630004400 / contacts search test@email.com'  
         },
          {'cmd': 'create',
         'syntax': 'notes create <title> / <body>',
         'description': 'add note to note book',
         'examples': 'notes create <title: borscht> / <body:Ukrainian Borscht everyone knows'
         },
           {'cmd': 'change',
         'syntax': 'notes change <title> / <body>',
         'description': 'changes note',
         'examples': 'notes change <title: borscht>  enter new title:<new_title>  enter new body:<new_body>'  # examples of command usage
         },
           {'cmd': 'delete',
         'syntax': 'notes delete <title>',
         'description': 'delete note from note book',
         'examples': 'notes delete <title:borscht>'
         },

        # add other command below:)
    ]

    if len(cmd) == 1:
        for itm in help_list:
            print('Command name: ' + itm['cmd'])
            print('Syntax: ' + itm['syntax'])
            print('Description: ' + itm['description'])
            print('Examples: ' + itm['examples'])
            print()
