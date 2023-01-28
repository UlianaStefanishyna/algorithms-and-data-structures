def super_digit_1_liner(n, k):
    return n if len(str(n)) == 1 else super_digit_1_liner(int(sum(int(i) for i in str(n))) * k, 1)


def super_digit_inner_func_map(n, k):
    def sum_digits(_int):
        return int(sum(map(int, list(str(_int)))))
    return n if len(str(n)) == 1 else super_digit_inner_func_map(sum_digits(n) * k, 1)


def superDigit3(n, k):
    if int(n) * k < 10:
        return int(n)*k
    else:
        sum = 0
        for s in n:
            sum += int(s)
        sum *= k
        output = superDigit3(str(sum), 1)

    return output


def super_digit_iterative_func(n, k):
    curr = sum(int(c) for c in n)
    curr *= k
    curr = str(curr)
    while len(curr) > 1:
        curr = str(sum(int(c) for c in curr))
    return int(curr)


if __name__ == '__main__':
    assert super_digit_1_liner(9875, 4) == 8
    assert super_digit_1_liner(148, 3) == 3
    assert super_digit_inner_func_map(9875, 4) == 8
    assert superDigit3('9875', 4) == 8
    assert super_digit_iterative_func('9875', 4) == 8
