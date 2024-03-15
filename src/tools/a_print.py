import time
from src.tools.cls import cls

CEND = '\33[0m'


def a_print(data, prefix='', wait_after=0.1, main_color='', prefix_color='', speed=0.01, end='\n', used_colors=[],clear_screen=0):
    def find_codes(codes, main_string):
        matches = {}
        for code in codes:
            start_index = 0
            for i in range(len(main_string)):
                j = main_string.find(code, start_index)
                if j != -1:
                    matches[j] = code
                    start_index = j + 1
        return matches

    m = find_codes(used_colors, data)
    p = 0
    output = ''
    while p <= len(data):

        time.sleep(speed)
        if p in m:
            p += len(m[p])
        else:
            p += 1
        output = prefix_color + prefix + CEND + main_color + data[0: p] + '\u2588' + CEND
        if clear_screen == 1:
            cls()
        print(output, end='\r')
    if clear_screen == 1:
        cls()
    print(output.replace('\u2588', ' '), end=end)
    time.sleep(wait_after)


if __name__ == '__main__':
    a_print('Hello', prefix='say: ')
