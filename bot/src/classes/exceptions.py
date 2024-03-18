'''Exceptions handler'''

from bot.settings import Settings

def validation_tracker(func):
    '''Handling exceptions'''
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            if str(e) == 'invalid_phone':
                print(f"{Settings.error_color}Entry has invalid phone number(s), my Lord!{Settings.end_color}")
            elif str(e) == 'invalid_email':
                print(f"{Settings.error_color}Entry has invalid e-mail address, my Lord!{Settings.end_color}")
            elif str(e) == 'invalid_name':
                print(f"{Settings.error_color}Entry has invalid name, my Lord!{Settings.end_color}")
            else:
                print(e)
        except TypeError as e:
            print(e)

    return wrapper
