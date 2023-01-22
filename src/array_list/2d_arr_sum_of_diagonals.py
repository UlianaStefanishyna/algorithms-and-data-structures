# https://www.hackerrank.com/challenges/one-week-preparation-kit-diagonal-difference/problem
def diagonal_difference(arr):
    sum_left = 0
    sum_right = 0
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if i == j:
                sum_left += arr[i][j]
            if j == len(arr) - 1 - i:
                sum_right += arr[i][j]
    return abs(sum_left - sum_right)


if __name__ == '__main__':
    print(diagonal_difference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]))
