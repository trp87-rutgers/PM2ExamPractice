"""
An assortment of sorting algorithms implimented in Python 3,
along with a brief test suite.
"""

import functools
import time

from structures import MinimumHeap # My data structure implimentations


def swap(container, i, j):
    """ A generic swap function for indexable containers. """
    container[i], container[j] = container[j], container[i]

    return container

def is_sorted(l):
    """
    Check if a container is sorted. Found this on StackOverflow.
    """
    return all(l[i] <= l[i+1] for i in range(len(l)-1))


def timeit(func):
    """
    Wrap a function so that it may automatically record the time
    elapsed during execution. Also found on StackOverflow.
    """
    @functools.wraps(func)
    def newfunc(*args, **kwargs):
        start_time = time.time()
        return_val = func(*args, **kwargs)
        elapsed_time = time.time() - start_time
        print("function '{}' finished in {} ms".format(func.__name__, int(elapsed_time * 1000)))
        return return_val

    return newfunc


def insertion_sort(container):
    """
    An implimentation of insertion sort.

    Runs in O(n) at best and O(n^2) at worst.
    """
    i = 1

    while i < len(container):
        j = i
        while j > 0 and container[j-1] > container[j]:
            swap(container, j, j-1)
            j -= 1
        i += 1

    return container


def selection_sort(container):
    """
    An implimentation of selection sort.

    Runs in O(n^2) for all cases.
    """
    item_count = len(container)

    for i in range(item_count - 1):
        minimum_index = i

        for j in range(i+1, item_count):
            if container[j] < container[minimum_index]:
                minimum_index = j

        if minimum_index != i:
            swap(container, i, minimum_index)

    return container


def merge_sort(container):
    """
    An implimentation of merge sort using Python slices.

    Runs in O(n*log(n)) time for all cases.
    """
    if len(container) < 2:
        return container

    m = len(container) // 2 # int division cause if its odd

    left, right = container[:m], container[m:]

    merge_sort(left)
    merge_sort(right)

    i, j, k = 0, 0, 0

    # Inserts smallest into the array and keeps goin till one runs out
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            container[k] = left[i]
            i += 1
        else:
            container[k] = right[j]
            j += 1
        k += 1

    # Finish off the array that had more elements left
    while i < len(left):
        container[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        container[k] = right[j]
        j += 1
        k += 1

    return container


def quick_sort(container):
    """
    An implimentation of 2-way quicksort.

    Typically runs in O(n*log(n)), except for the O(n^2) worst
    case on already sorted arrays due to the pivot being the
    smallest item. This implimentation has that flaw since it
    uses the first item as the pivot.
    """
    def partition(source, low, high):
        i, j = low, high + 1

        while True:
            while source[i+1] < source[low]:
                i += 1
                if i == high:
                    break

            i += 1

            while source[low] < source[j-1]:
                j -= 1
                if j == low:
                    break

            j -= 1

            if i >= j:
                break

            swap(source, i, j)

        swap(source, low, j)

        return j

    def sort(source, low, high):
        if high <= low:
            return

        j = partition(source, low, high)

        sort(source, low, j - 1)
        sort(source, j+1, high)

    sort(container, 0, len(container) - 1)

    return container


def three_way_quick_sort(container):
    """
    An implimentation of in-place 3-way quicksort.

    Runs in O(n*log(n)) time except for the worst case O(n^2).
    """

    def sort(source, low, high, median_pivot=False):
        """ An in-place three way quicksort algorithm. """
        if high <= low:
            return

        index, lesser, greater = low, low, high

        pivot = source[low]  # Pivot is always the first item

        while index <= greater:
            if source[index] < pivot:
                swap(source, lesser, index)
                lesser += 1
                index += 1
            elif source[index] > pivot:
                swap(source, index, greater)
                greater -= 1
            else:
                index += 1

        sort(source, low, lesser - 1)
        sort(source, greater + 1, high)

    sort(container, 0, len(container) - 1)

    return container


def heap_sort(container):
    """
    An implimentation of heap sort using a min heap implimentation.
    """

    heap = MinimumHeap()

    for item in container:
        heap.insert(item)

    return [heap.del_min() for _ in range(heap.data_count)]


if __name__ == "__main__":
    from random import shuffle

    my_list = [x for x in range(10000)]

    shuffle(my_list)

    sorting_functions = (
        insertion_sort,
        selection_sort,
        merge_sort,
        quick_sort,
        three_way_quick_sort,
        heap_sort,
        sorted,
    )

    print("Running {} sorting algorithms!".format(len(sorting_functions)))

    for timed_func in (timeit(func) for func in sorting_functions):
        result = timed_func(list(my_list))  # Run the timed function on a copy
        assert is_sorted(result)
