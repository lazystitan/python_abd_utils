from os import *


def stitch(*args):
    result = ""
    for item in args:
        result += str(item) + " "
    return result.strip()


def drag_and_drop(position1, position2, time=-1):
    (x1, y1) = position1
    (x2, y2) = position2
    prefix = "adb shell input draganddrop "
    command = stitch(prefix, x1, y1, x2, y2)
    if time != -1:
        command = stitch(command, time)
    return popen(command).read()


def swipe(position1 , position2, time):
    (x1, y1) = position1
    (x2, y2) = position2
    prefix = "adb shell input swipe"
    command = stitch(prefix, x1, y1, x2, y2, time)
    # print(command)
    return popen(command).read()


def tap(position):
    (x, y) = position
    prefix = "adb shell input tap "
    command = stitch(prefix, x, y)
    # print(command)
    return popen(command).read()


def long_tap(position):
    (x, y) = position
    return swipe((x, y), (x, y), 500).read()


if __name__ == '__main__':
    drag_and_drop((530, 1128), (530, 1000))

