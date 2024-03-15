from prompt_toolkit.completion import NestedCompleter


def completer():
    data = NestedCompleter.from_nested_dict({
        'contacts': {'create': None,
                     'change': None,
                     'delete': None,
                     'show': {'all': None,
                              'birthdays': None
                              }
                     },
        'notes': {'create': None,
                  'change': None,
                  'delete': None,
                  'show': None,
                  'search': None,
                  'filter by tag': None
                  },

        'hello': None,
        'war statistics today': None,
        'war statistics dd-mm-yyyy': None,
        'exit': None,
        'quit': None,
        'end': None,
        'about': None,
        'help': None
    })
    return data
