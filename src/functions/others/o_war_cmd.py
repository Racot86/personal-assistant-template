import json
import requests
from settings import Settings
from datetime import datetime, timedelta
from src.tools.a_print import a_print


def print_statistics(data):
    data = data['data']

    a_print('   date: {:12}                 day: {:<}'.format(data['date'], data['day']))
    a_print(f'{Settings.shadow_color}  ----------------------------------------------{Settings.end_all}',
            used_colors=[Settings.shadow_color, Settings.end_all])

    delta = data['increase']
    for k, v in data['stats'].items():
        if delta[k] != 0:
            print('   {:<36}: {:<}'.format(Settings.shadow_color + k.replace('_', ' ') + Settings.end_all, str(v) + '(' + Settings.success_color + str(delta[k]) + Settings.end_color + ')'))
        else:
            print('   {:<36}: {:<}'.format(Settings.shadow_color + k.replace('_', ' ') + Settings.end_all , v))

    print('  resource: {:12}'.format(data['resource']))
    print('')
    a_print('GLORY TO UKRAINE!', prefix=Settings.TARDIS,
            main_color=Settings.msg_color,
            )
    print()


def o_war_cmd(cmd):
    cmd.pop(0)
    if len(cmd) > 1:
        if cmd[0] == 'statistics' and cmd[1] == 'today':
            url = 'https://russianwarship.rip/api/v2/statistics/latest'
            x = requests.get(url)
            if x.status_code == 200:
                a_print('Look what I found to your request!',
                        prefix=Settings.TARDIS,
                        main_color=Settings.msg_color,
                        used_colors=[Settings.msg_color]
                        )
                data = x.content.decode()
                data = json.loads(data)
                print()
                a_print("               TODAY'S ORCS ARMY LOSS", main_color=Settings.warning_color)
                print_statistics(data)

            else:
                a_print('Something went wrong. Please check your internet connection.',
                        prefix='TARDIS: ',
                        main_color=Settings.warning_color
                        )
        elif cmd[0] == 'statistics' and len(cmd) == 2:
            try:
                date = datetime.strptime(cmd[1], '%d-%m-%Y')
                url = 'https://russianwarship.rip/api/v2/statistics/' + date.strftime('%Y-%m-%d')
                x = requests.get(url)
                if x.status_code == 200:
                    a_print('Look what I found to your request!',
                            prefix='TARDIS: ',
                            main_color=Settings.msg_color,
                            used_colors=[Settings.msg_color]
                            )
                    data = x.content.decode()
                    data = json.loads(data)
                    print()
                    a_print("           ORCS ARMY LOSS ON " + date.strftime('%d-%m-%Y'), main_color=Settings.warning_color)
                    print_statistics(data)
                else:
                    a_print('Something went wrong. Please check date period or your internet connection.',
                            prefix='TARDIS: ',
                            main_color=Settings.warning_color
                            )
            except ValueError:
                a_print('You entered date wrongly. For your info correct date format dd-mm-yyyy',
                        prefix='TARDIS:',
                        main_color=Settings.msg_color
                        )
        else:
            a_print('I do not understand what you are trying to say.',
                    prefix='TARDIS:',
                    main_color=Settings.warning_color
                    )
    else:
        print('Wrong parameters')
