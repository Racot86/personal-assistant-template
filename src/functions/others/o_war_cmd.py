import json
import requests
from settings import Settings
from datetime import datetime, timedelta
from src.tools.a_print import a_print


def o_war_cmd(cmd):
    cmd.pop(0)
    if len(cmd) > 0:
        if cmd[0] == 'statistics' and cmd[1] == 'today':
            url = 'https://russianwarship.rip/api/v2/statistics/latest'
            x = requests.get(url)
            if x.status_code == 200:
                a_print('Look what I found to your request!',
                        prefix='TARDIS: ',
                        prefix_color=Settings.time_color,
                        main_color= Settings.input_color,
                        used_colors=[Settings.time_color, Settings.msg_color]
                        )
                data = x.content.decode()
                data = json.loads(data)
                data = data['data']
                print("TODAY'S RUSSIAN CRAP ARMY LOSS")

                print('   date: {:12}                     day: {:<}'.format(data['date'], data['day']))
                print('  --------------------------------------------------')

                delta = data['increase']
                for k, v in data['stats'].items():
                    if delta[k] != 0:
                        print('{:>28}: {:<}'.format(k.replace('_', ' '), str(v) + '(' + str(delta[k]) + ')'))
                    else:
                        print('{:>28}: {:<}'.format(k.replace('_', ' '), v))

                print('< resource: {:12}'.format(data['resource']))
                print('')
                print('< GLORY TO UKRAINE!')
            else:
                print('Something went wrong. Please check your internet connection.')

    else:
        print('Wrong parameters')
