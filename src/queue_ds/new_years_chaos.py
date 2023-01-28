from copy import deepcopy


def minimumBribes(q: list):
    d = {item: i for i, item in enumerate(q)}
    q.sort()
    bribes = 0
    for i, item in enumerate(q):
        if i - d[item] > 2:
            return 'Too chaotic'
        elif i - d[item] > 0:
            bribes += i - d[item]
    return bribes


def minimum_bribes_2(q: list):
    d = {item: [i] for i, item in enumerate(q)}
    q.sort()
    bribes = 0
    for i, item in enumerate(q):
        res_index = d[item][0]
        # if res_index > i:
        #     continue
        if i - res_index > 2:
            return 'Too chaotic'
        elif i - res_index == 2:
            q[i], q[i-1] = q[i-1], q[i]
            q[i-1], q[i-2] = q[i-2], q[i-1]
            bribes += 2
            d[q[i]].append(i-1)
            d[q[i]].append(i-2)
            d[q[i-1]].append(i)
            d[q[i-2]].append(i-1)
        elif i - res_index == 1:
            q[i], q[i-1] = q[i-1], q[i]
            d[q[i]].append(i-1)
            d[q[i]].append(i-2)
            d[q[i-1]].append(i)
            bribes += 1
        # elif d[item][0] - i == 1:
        #     q[i], q[i-1] = q[i-1], q[i]
        #     bribes += 1
        # elif len(d[item]) > 1 and i > 0:
        #     if d[item][i] > d[item][i-1]:
        #         q[i], q[i-1] = q[i-1], q[i]
        #         bribes += 1

    for i, item in enumerate(q):
        if d[item][0] == i:
            continue
        if d[item][0] - i == 1:
            q[i], q[i-1] = q[i-1], q[i]
            bribes += 1
    # print(q)
    return bribes


if __name__ == '__main__':
    assert minimumBribes([2, 1, 5, 3, 4]) == 3
    assert minimum_bribes_2([2, 1, 5, 3, 4]) == 3

    assert minimumBribes([2, 5, 1, 3, 4]) == 'Too chaotic'
    assert minimum_bribes_2([2, 5, 1, 3, 4]) == 'Too chaotic'

    assert minimumBribes([1, 2, 3, 5, 4, 6, 7, 8]) == 1
    assert minimum_bribes_2([1, 2, 3, 5, 4, 6, 7, 8]) == 1

    assert minimumBribes([5, 1, 2, 3, 7, 8, 6, 4]) == 'Too chaotic'
    assert minimum_bribes_2([5, 1, 2, 3, 7, 8, 6, 4]) == 'Too chaotic'

    # print(minimumBribes([1, 2, 5, 3, 7, 8, 6, 4]))
                        # 1, 2, 3, 4, 5, 6, 7, 8

    print(minimum_bribes_2([1, 2, 5, 3, 7, 8, 6, 4]))
    assert minimum_bribes_2([1, 2, 5, 3, 7, 8, 6, 4]) == 7
    # assert minimumBribes([1, 2, 5, 3, 7, 8, 6, 4]) == 7

    # 1, 2, 3, 4, 5, 6, 7, 8 -> (5->4->3) x2 - 2 - 4 (2) -> 4-2
    # 1, 2, 5, 3, 4, 6, 7, 8 -> (7->6->4) x2 - 4 - 6 (2) -> 6-4
    # 1, 2, 5, 3, 7, 4, 6, 8 -> (8->6->4) x2 - 5 - 7 (2) -> 7-5
    # 1, 2, 5, 3, 7, 8, 4, 6 -> (6->4) x1 - 6 - 5 (1) -> 5-6
    # 1, 2, 5, 3, 7, 8, 6, 4

    # 1 - [0]
    # 2 - [1]
    # 3 - [2, 3]
    # 4 - [3, 4, 5, 6, 7]
    # 5 - [4, 3, 2]
    # 6 - [5, 6, 7, 6]
    # 7 - [6, 5, 4]
    # 8 - [7, 6, 5]
