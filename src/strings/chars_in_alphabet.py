import string


def chars_in_alphabet():
    h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
    word = 'zaba'
    max_v = 0

    for i, char in enumerate(word):
        index = string.ascii_lowercase.index(char)
        if h[index] > max_v:
            max_v = h[index]
    return max_v * len(word)