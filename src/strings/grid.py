def gridChallenge(grid):
    n = len(grid)
    m = len(grid[0])
    grid[0] = sorted(grid[0])
    print(grid[0])
    for i in range(1,n):
        grid[i] = sorted(grid[i])
        for j in range(m):
            if grid[i-1][j] > grid[i][j]:
                return "NO"
    return "YES"


if __name__ == '__main__':
    print(gridChallenge(['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']))
