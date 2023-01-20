from array_list.reverse_array import reverse_array, reverse_arr_python_native


def test_algorithm():
    res = reverse_array([1, 2, 3])
    assert res == [3, 2, 1]


def test_python_native():
    res = reverse_arr_python_native([1, 2, 3])
    assert res == [3, 2, 1]

