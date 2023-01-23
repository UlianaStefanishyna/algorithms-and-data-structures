# https://www.hackerrank.com/challenges/one-week-preparation-kit-countingsort1/problem

"""Comparison Sorting Quicksort usually has a running time of , but is there an algorithm that can sort even faster?
In general, this is not possible. Most sorting algorithms are comparison sorts, i.e. they sort a list just by
comparing the elements to one another. A comparison sort algorithm cannot beat  (worst-case) running time,
since  represents the minimum number of comparisons needed to know where to place each element. For more details,
you can see these notes (PDF).

Alternative Sorting Another sorting method, the counting sort, does not require comparison. Instead, you create an
integer array whose index range covers the entire range of values in your array to sort. Each time a value occurs in
the original array, you increment the counter at that index. At the end, run through your counting array,
printing the value of each non-zero valued index that number of times.
"""


def counting_sort(arr):
    frequency_array = [0] * 100
    for item in arr:
        frequency_array[item] += 1
    return frequency_array


if __name__ == '__main__':
    print(counting_sort([1, 2, 4, 2, 5]))
