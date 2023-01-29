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

    def _add_path(d, q, index):
        for i in range(index, len(q)):
            d[q[i]].append(i)
        print(d)

    for i, item in enumerate(q):
        res_index = d[item][0]
        if i - res_index > 2:
            return 'Too chaotic'
        elif i - res_index == 2:
            q[i], q[i-1] = q[i-1], q[i]
            q[i-1], q[i-2] = q[i-2], q[i-1]
            _add_path(d, q, i-2)
            bribes += 2
        elif i - res_index == 1:
            q[i], q[i-1] = q[i-1], q[i]
            _add_path(d, q, i-1)
            bribes += 1
    initial_q = list(d.keys())
    for i in range(len(q)):
        if q[i] != initial_q[i] and d[initial_q[i]][0] < i:
            bribes += i - d[initial_q[i]][0]

    # if initial_q != q:
    #     print('not')
    print(d)
    print(q)
    return bribes


def minimum_bribes_3(q):
    nr_of_bribes = 0
    balance = 0
    for expected_id, actual_id in enumerate(q, start=1):
        this_person_bribes = actual_id - expected_id
        if this_person_bribes > 2:
            print("Too chaotic")
            return "Too chaotic"
        if this_person_bribes > 0:
            nr_of_bribes += this_person_bribes
        elif abs(this_person_bribes) < balance // 2:
            nr_of_bribes += 1
        balance += this_person_bribes
    print(nr_of_bribes)
    return nr_of_bribes


if __name__ == '__main__':
    # assert minimumBribes([2, 1, 5, 3, 4]) == 3
    # assert minimum_bribes_2([2, 1, 5, 3, 4]) == 3
    # assert minimum_bribes_3([2, 1, 5, 3, 4]) == 3
    #
    # assert minimumBribes([2, 5, 1, 3, 4]) == 'Too chaotic'
    # assert minimum_bribes_2([2, 5, 1, 3, 4]) == 'Too chaotic'
    # assert minimum_bribes_3([2, 5, 1, 3, 4]) == 'Too chaotic'
    #
    # assert minimumBribes([1, 2, 3, 5, 4, 6, 7, 8]) == 1
    # assert minimum_bribes_2([1, 2, 3, 5, 4, 6, 7, 8]) == 1
    # assert minimum_bribes_3([1, 2, 3, 5, 4, 6, 7, 8]) == 1
    #
    # assert minimumBribes([5, 1, 2, 3, 7, 8, 6, 4]) == 'Too chaotic'
    # assert minimum_bribes_2([5, 1, 2, 3, 7, 8, 6, 4]) == 'Too chaotic'
    # assert minimum_bribes_3([5, 1, 2, 3, 7, 8, 6, 4]) == 'Too chaotic'

    # print(minimumBribes([1, 2, 5, 3, 7, 8, 6, 4]))
                        # 1, 2, 3, 4, 5, 6, 7, 8

    # print(minimum_bribes_2([1, 2, 5, 3, 7, 8, 6, 4]))
    assert minimum_bribes_3([1, 2, 5, 3, 7, 8, 6, 4]) == 7
    # print(minimum_bribes_3([1, 2, 5, 3, 7, 8, 6, 4]))
    # assert minimum_bribes_2([1, 2, 5, 3, 7, 8, 6, 4]) == 7
    # assert minimumBribes([1, 2, 5, 3, 7, 8, 6, 4]) == 7

    # 1, 2, 3, 4, 5, 6, 7, 8 -> (5->4->3) x2 - 2 - 4 (2) -> 4-2
    # 1, 2, 5, 3, 4, 6, 7, 8 -> (7->6->4) x2 - 4 - 6 (2) -> 6-4
    # 1, 2, 5, 3, 7, 4, 6, 8 -> (8->6->4) x2 - 5 - 7 (2) -> 7-5
    # 1, 2, 5, 3, 7, 8, 4, 6 -> (6->4) x1 - 6 - 5 (1) -> 5-6
    # 1, 2, 5, 3, 7, 8, 6, 4

    # 1 - [0]
    # 2 - [1]
    # 5 - [2] > 2,3
    # 3 - [3] > 3,2,4
    # 7 - [4] > 4,5
    # 8 - [5] > 5,6
    # 6 - [6] > 6,5,5,4,6,5
    # 4 - [7] > 7,3,3,2,6,7


    # 3 - [2, 3]
    # 4 - [3, 4, 5, 6, 7]
    # 5 - [4, 3, 2]
    # 6 - [5, 6, 7, 6]
    # 7 - [6, 5, 4]
    # 8 - [7, 6, 5]
