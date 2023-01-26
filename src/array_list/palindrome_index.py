# https://www.hackerrank.com/challenges/palindrome-index/problem
def palindrome_index(s):
    # if is_palindrome(s):
    #     return -1
    #
    # s1 = s[0:len(s)//2]
    # mid_char_index = len(s) // 2 if len(s) % 2 == 0 else len(s) // 2 + 1
    # s2 = s[mid_char_index:]
    # s2 = s2[::-1]
    # for i in range(len(s1)):
    #     if s1[i] != s2[i]:
    #         new_s1 = s1[:i] + s1[i + 1:]
    #         if is_palindrome(new_s1+s2):
    #             return i
    #         else:
    #             new_s2 = s2[:i] + s2[i+1:]
    #             if is_palindrome(s1+new_s2):
    #                 return i + i + 1
    # return -2
    # # for i, j in zip(range(0, len(s)//2 + 1), range(len(s) - 1, len(s)//2, -1)):

    left = 0
    right = len(s) - 1
    index_to_remove = -1
    while left < right:
        if s[left] != s[right]:
            if is_palindrome_2(s, left + 1, right):
                index_to_remove = left
            else:
                index_to_remove = right
            break
        left += 1
        right -= 1
    return index_to_remove


def is_palindrome(s: str):
    mid_char_index = len(s) // 2 if len(s) % 2 == 0 else len(s) // 2 + 1
    s2 = s[mid_char_index:]
    return True if s[0:len(s) // 2] == s2[::-1] else False


def is_palindrome_2(s: str, left: int, right: int):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def isPalindrome(s): return s == s[::-1]


def palindromeIndex(s):
    if isPalindrome(s):
        return -1
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            if isPalindrome(s[:i] + s[i + 1:]):
                return i
            elif isPalindrome(s[:len(s) - 1 - i] + s[len(s) - i:]):
                return len(s) - 1 - i
            return -1


if __name__ == '__main__':
    s = 'baaa'
    print(palindrome_index(s))
    print(palindromeIndex(s))
