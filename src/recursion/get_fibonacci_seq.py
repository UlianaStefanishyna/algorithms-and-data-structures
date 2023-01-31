"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the
iterative code in the instructions."""

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34


def get_fib(position):
    if position <= 0:
        return 0
    elif position == 1:
        return 1
    else:
        return get_fib(position-1) + get_fib(position-2)


if __name__ == '__main__':
    assert get_fib(0) == 0
    assert get_fib(1) == 1
    assert get_fib(2) == 1
    assert get_fib(9) == 34
    assert get_fib(11) == 89
