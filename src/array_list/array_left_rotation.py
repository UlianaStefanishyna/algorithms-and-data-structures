
# https://www.hackerrank.com/challenges/ctci-array-left-rotation
def rot_left(a: [], d: int):
    if d < 0:
        raise Exception
    if d == 0 or d == len(a):
        return a
    if d > len(a):
        d %= len(a)
    a1 = list()
    for i in range(0, len(a)):
        a1.append(a[d])
        d = 0 if (d == len(a) - 1) else d + 1
    return a1


# solution 2
def rot_left_1(a, d):
    if d < 0:
        raise Exception
    if d == 0 or d == len(a):
        return a
    if d > len(a):
        d %= len(a)
    print(a[d:])  # d is included
    print(a[:d])  # d is not included
    return a[d:] + a[:d]
