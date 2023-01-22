# https://www.hackerrank.com/challenges/one-week-preparation-kit-lonely-integer/problem

def lonely_integer_1(a):
    a.sort()
    print(a)
    d = dict()
    for i, item in enumerate(a):
        if not d.get(item):
            d.update({item: 1})
        if i > 0:
            if a[i - 1] == a[i]:
                d.update({item: d.get(item) + 1})
            else:
                if d.get(a[i - 1]) > 1:
                    del d[a[i - 1]]
            if i == len(a) - 1:
                if d.get(a[i - 1]) > 1:
                    del d[a[i - 1]]
    return d.popitem()


def lonely_integer_2(a):
    d = dict()
    for i in a:  # Time: O(N), Space O(N)
        if not d.get(i):
            d.update({i: 1})
        else:
            d.update({i: d.get(i) + 1})

    for i in a:  # Time: O(N)
        if d.get(i) == 1:
            return i


if __name__ == '__main__':
    print(lonely_integer_1([1, 1, 3, 2, 3, 2, 5, 6, 8, 8, 6]))
    print(lonely_integer_2([1, 1, 3, 2, 3, 2, 5, 6, 8, 8, 6]))
