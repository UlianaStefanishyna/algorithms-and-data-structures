# https://www.hackerrank.com/challenges/tower-breakers-1/problem

def tower_breakers(n, m):
    if m == 1:
        return 2
    elif n % 2 == 0:
        return 2
    else:
        return 1


if __name__ == '__main__':
    print(tower_breakers(1, 4))