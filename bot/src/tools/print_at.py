pr = lambda command: print("\x1b[", command, sep="", end="")


def print_at(char, x, y, color="", bright="0"):
    pr("%d;%df" % (y, x))
    print(color,sep="", end="")
    print(char, end="", flush=True)
