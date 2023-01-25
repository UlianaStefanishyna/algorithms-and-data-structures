# https://www.hackerrank.com/challenges/one-week-preparation-kit-zig-zag-sequence/problem
def find_zig_zag_sequence(a, n):
    a.sort()
    mid = int((n + 1) / 2 - 1)
    a[mid], a[n - 1] = a[n - 1], a[mid]

    st = mid + 1
    ed = n - 2
    while st <= ed:
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range(n):
        if i == n - 1:
            print(a[i])
        else:
            print(a[i], end=' ')
    return


if __name__ == '__main__':
    n = 7
    a = [1, 2, 3, 4, 5, 6, 7]
    find_zig_zag_sequence(a, n)
    assert a == [1, 2, 3, 7, 6, 5, 4]
