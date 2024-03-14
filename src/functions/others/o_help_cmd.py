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
        # add other command below:)
    ]

    if len(cmd) == 1:
        for itm in help_list:
            print('Command name: ' + itm['cmd'])
            print('Syntax: ' + itm['syntax'])
            print('Description: ' + itm['description'])
            print('Examples: ' + itm['examples'])
            print()
