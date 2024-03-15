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
         {'cmd': 'contacts create',
         'syntax': 'contacts create <contact name> <email:xxxx@xxxx.xx> <phones:1234567890,1234567890> <birthday:dd-mm-YYYY>',
         'description': 'This command for create a new contact',
         'examples': 'contacts create Who,Doctor email:who@doctor.com phones:0991112233'
         },
         {'cmd': 'contacts change',
         'syntax': 'contacts change <contact name> ENTER or <email:xxxx@xxxx.xx> <phones:1234567890,1234567890> <birthday:dd-mm-YYYY>',
         'description': 'This command for change a contact data',
         'examples': 'contacts change Who,Doctor email:doctor@who.com phones:0993211122'
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
