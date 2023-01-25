# https://www.hackerrank.com/challenges/caesar-cipher-1/problem
def caesar_cipher(s, k):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_len = len(alphabet)
    cipher_message = ''
    for c in s:
        if not c.isalpha():
            cipher_message += c
            continue
        index, is_upper = find_index(c, alphabet)
        new_index = index + k
        if new_index >= alphabet_len:
            new_index %= alphabet_len
        cipher_message += alphabet[new_index].upper() if is_upper else alphabet[new_index]
    return cipher_message


def find_index(char, alphabet) -> (int, bool):
    for i, item in enumerate(alphabet):
        if char.islower():
            if char == item.lower():
                return i, False
        else:
            if char == item.upper():
                return i, True


def caesar_cipher_with_hashtable(s, k):
    from string import ascii_lowercase
    chars = ascii_lowercase
    cipher = ''
    hash_table = dict((v, k) for k, v in enumerate(chars))
    for c in s:
        tmp = c.casefold()
        if tmp not in hash_table:
            cipher += c
            continue
        i = hash_table[tmp] + k
        if i < 26:
            txt = chars[i]
        else:
            i %= 26
            txt = chars[i]
        cipher += txt if c.islower() else txt.upper()
    return cipher


if __name__ == '__main__':
    print(caesar_cipher('middle-Outz', 2))
    print(caesar_cipher_with_hashtable('middle-Outz', 2))
