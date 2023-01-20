def reverse_array(a):
    if not a:
        raise Exception

    a1 = [None] * len(a)  # init python array of a specific size with None
    for i in range(0, len(a)):
        a1[i] = a[len(a) - i - 1]
    return a1


def reverse_arr_python_native(a):
    return a[::-1]