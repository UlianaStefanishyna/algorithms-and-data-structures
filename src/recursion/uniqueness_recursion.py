"""
Here are some edge cases for this problem:

1. An empty string: When the input string is empty, the start and stop indices should both be 0,
and the function should return True as there are no elements in an empty string.
2. A single-character string: When the input string has only one character, the start and stop
indices should both be 0, and the function should return True as there is only one unique character
in the string.
3. A string with only duplicates: When the input string contains only duplicates, the start and
stop indices should include the entire string, and the function should return False as there are
no unique characters in the string.
4. A string with unique elements: When the input string contains only unique characters,
the start and stop indices should include the entire string, and the function should return True
as there are no duplicate characters in the string.

These edge cases test the limits of the function and ensure that it works correctly when given
inputs that are at the extreme ends of the possible inputs.
"""
import sys, inspect


def unique(string, start, stop) -> bool:
    # print(f'PUT to. {start}-{stop}')
    """
    :param string: string
    :param start: index
    :param stop: index
    :return: True if there are no duplicate elements in slice S[start:stop]
    """
    if stop - start <= 1:
        # print(f'POP from (less). {start}-{stop}')
        return True  # at most 1 item
    elif not unique(string, start, stop - 1):
        return False  # first part has duplicates
    elif not unique(string, start + 1, stop):
        return False  # second part has duplicates
    else:
        # print(f'POP from (more). {start}-{stop}')
        return string[start] != string[stop-1]


# This is the same version as with two recursive calls (^`unique`) but using a stack DS
"""In the code, the is_pop value is used to keep track of whether the current iteration of 
the loop is a pop operation or a push operation. The value of is_pop is True when the 
current iteration is a pop operation, and False when it is a push operation.
"""


def unique_with_stack_exp(string, start, stop):
    stack = [(start, stop, False)]  # PUSH op
    while stack:
        # print(stack)
        start, stop, is_pop = stack.pop()
        if stop - start <= 1:
            continue
        if not is_pop:  # if PUSH op
            stack.append((start, stop - 1, False))  # PUSH op
            stack.append((start, stop - 1, True))  # POP op
        else:
            if string[start] == string[stop - 1]:
                return False
            stack.append((start + 1, stop, True))  # POP op
    return True


def unique_using_stack_linear(string, start, stop) -> bool:
    stack = [(start, stop)]
    while stack:
        start, stop = stack.pop()
        if stop - start <= 1:
            continue
        elif string[start] == string[stop-1]:
            return False
        stack.append((start, stop-1))
        stack.append((start+1, stop))
    return True


def tracefunc(frame, event, arg, indent=[0]):
    if event == "call":
        args, _, _, values = inspect.getargvalues(frame)
        print(indent, "-" * indent[0] + "> call function L#", frame.f_lineno, frame.f_code.co_name, values)
        indent[0] += 2
    elif event == "return":
        indent[0] -= 2
        print(indent, "-" * indent[0] + "< return from L#", frame.f_lineno, frame.f_code.co_name, indent)
    return tracefunc


sys.settrace(tracefunc)

if __name__ == '__main__':
    print('---')
    assert unique_with_stack_exp('abcdeft', 0, 6)
    print('----')
    assert not unique('abbdeft', 0, 3)
    assert not unique_using_stack_linear('abbdeft', 0, 7)

    assert unique_with_stack_exp('abcdefg', 0, 7)
    assert unique('abcdefg', 0, 7)
    assert unique_using_stack_linear('abcdefg', 0, 7)

    # Edge case, length of string is 0
    assert unique_with_stack_exp("", 0, 0)
    assert unique("", 0, 0)
    assert unique_using_stack_linear("", 0, 0)

    # Edge case, length of string is 1
    assert unique_with_stack_exp("a", 0, 1)
    assert unique("a", 0, 1)
    assert unique_using_stack_linear("a", 0, 1)

    # Edge case, start index is greater than stop index
    assert unique_with_stack_exp("abcdefg", 5, 3)
    assert unique("abcdefg", 5, 3)
    assert unique_using_stack_linear("abcdefg", 5, 3)
