# Python program to convert time from 12 hour to 24 hour format


def convert24(str1):

    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]
    elif str1[-2:] == "AM":
        return str1[:-2]
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]
    else:
        return str(int(str1[:2]) + 12) + str1[2:8]


def string_slicing():
    str = 'yellow'
    print(str[1])  # => 'e' Position # from the start if a positive number , starts from 0
    print(str[-1])  # => 'w' Position # from the end if a negative number, starts from 1 (which is -1)
    print(str[4:6])  # => 'ow'
    print(str[:4])  # => 'yell' Last not included!
    print(str[-3:])  # => 'low' colon always indicates a range


if __name__ == '__main__':
    print(convert24("00:00:00 AM"))
    string_slicing()
