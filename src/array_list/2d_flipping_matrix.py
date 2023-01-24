# https://www.hackerrank.com/challenges/flipping-the-matrix/problem?h_r=internal-search
def flipping_matrix(matrix):
    n = len(matrix)
    s = 0
    for i in range(n // 2):
        for j in range(n // 2):
            s += max(matrix[i][j], matrix[i][n - 1 - j], matrix[n - 1 - j][i], matrix[n - 1 -j][n - 1 - i])
    return s


if __name__ == '__main__':
    matrix = [[112, 42, 83, 119],
              [56, 125, 56, 49],
              [15, 78, 101, 43],
              [62, 98, 114, 108]]
    print('Initial Matrix:')
    [print(item) for item in matrix]
    max_s = flipping_matrix(matrix)
    print(f'Max sum of square is {max_s}')
