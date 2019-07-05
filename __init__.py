from os import *
from input import *


def command():
    s = popen("adb").read()
    print(s)


def main():
    command()


if __name__ == '__main__':
    main()