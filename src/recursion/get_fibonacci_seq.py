"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the
iterative code in the instructions."""

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34


# using recursion only
def get_fib(position):
    if position <= 0:
        return 0
    elif position == 1:
        return 1
    else:
        return get_fib(position-1) + get_fib(position-2)


# using cache and recursion (dynamic programming)
def calculate_fibonacci_with_cache(position, cache=None):
    if cache is None:
        cache = {0: 0, 1: 1}
    if position in cache:
        return cache[position]
    else:
        result = calculate_fibonacci_with_cache(position-1) + calculate_fibonacci_with_cache(position-2)
        cache[position] = result
        return result


# using iterative approach
def fibonacci_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b


from uniqueness_recursion import tracefunc
import sys
sys.settrace(tracefunc)


def good_fibonacci_linear_recursion(n):  # O(n)
    if n <= 1:
        return n, 0
    else:
        a, b = good_fibonacci_linear_recursion(n - 1)
        return a + b, a


if __name__ == '__main__':
    # assert get_fib(0) == 0
    # assert get_fib(1) == 1
    # assert get_fib(2) == 1
    # assert get_fib(9) == 34
    # assert get_fib(11) == 89
    #
    # assert fibonacci_iterative(0) == 0
    # assert fibonacci_iterative(1) == 1
    # assert fibonacci_iterative(2) == 1
    # assert fibonacci_iterative(9) == 34
    # assert fibonacci_iterative(11) == 89
    #
    # assert calculate_fibonacci_with_cache(0) == 0
    # assert calculate_fibonacci_with_cache(1) == 1
    # assert calculate_fibonacci_with_cache(2) == 1
    # assert calculate_fibonacci_with_cache(9) == 34
    # assert calculate_fibonacci_with_cache(11) == 89
    res, _ = good_fibonacci_linear_recursion(9)
    assert res == 34

