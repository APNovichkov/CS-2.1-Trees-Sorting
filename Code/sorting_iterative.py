#!python

def is_sorted(items):
    """
    Return a boolean indicating whether given items are in sorted order.

    Ascending : True/False

    Running time: O(n) Linear time, only one for loop. Best case is first item is out of place. Worst case array is sorted
    Memory usage: O(1), Just the variable to hold the iterator
    """

    for i in range(len(items) - 1):
        if items[i] > items[i + 1]:
            return False

    return True

def is_sorted_ordered(items, ascending):
    """
    Return a boolean indicating whether given items are in sorted order.

    ascending : True/False

    Running time: O(n) Linear time, only one for loop. Best case is first item is out of place. Worst case array is sorted
    Memory usage: O(1) Just the variable to hold the iterator
    """

    for i in range(len(items) - 1):
        if ascending:
            if items[i] > items[i + 1]:
                return False
        else:
            if items[i] < items[i + 1]:
                return False

    return True

def is_sorted_with_key(items, key):
    """
    Return a boolean indicating whether given items are in sorted order.

    key: a lambda function that can transform what items are being compared

    Running time: O(n) Linear time, only one for loop. Best case is first item is out of place. Worst case array is sorted
    Memory usage: O(1) Just the variable to hold the iterator
    """

    for i in range(len(items) - 1):
        if key(items[i]) > key(items[i + 1]):
            return False

    return True

def bubble_sort(items):
    """
    Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.

    Time Complexity: O(n^2) worst case running time when array is completely reversed. Generally still quadratic...
    Memory Usage: O(1), We perform swapping, so everything happens in place. Only memory used is for some of the variables
    """

    if len(items) == 0:
        return []

    limit = len(items) - 1  # set upper limit to array size
    continue_sort = True

    while(continue_sort):
        continue_sort = False  # Set default to false for each run through array
        for i in range(limit):  # Run through all elements until the upper limit
            if items[i] > items[i + 1]:
                _swap(items, i, i + 1)
                continue_sort = True  # If there has been at least one swap, we should continue sorting..

        limit -= 1

    return items

def bubble_sort_ordered(items, ascending):
    """
    Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.

    ascending : True/False

    Time Complexity: O(n^2) worst case running time when array is completely reversed. Generally still quadratic...
    Memory Usage: O(1), We perform swapping, so everything happens in place. Only memory used is for some of the variables
    """

    if len(items) == 0:
        return []

    limit = len(items) - 1  # set upper limit to array size
    continue_sort = True

    while(continue_sort):
        continue_sort = False  # Set default to false for each run through array
        for i in range(limit):  # Run through all elements until the upper limit
            if ascending:
                if items[i] > items[i + 1]:
                    _swap(items, i, i + 1)
                    continue_sort = True  # If there has been at least one swap, we should continue sorting..
            else:
                if items[i] < items[i + 1]:
                    _swap(items, i, i + 1)
                    continue_sort = True  # If there has been at least one swap, we should continue sorting..
        limit -= 1

    return items

def bubble_sort_with_key(items, key):
    """
    Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.

    key: a lambda function that can transform what items are being compared

    Time Complexity: O(n^2) worst case running time when array is completely reversed. Generally still quadratic...
    Memory Usage: O(1), We perform swapping, so everything happens in place. Only memory used is for some of the variables
    """

    if len(items) == 0:
        return []

    limit = len(items) - 1  # set upper limit to array size
    continue_sort = True

    while(continue_sort):
        continue_sort = False  # Set default to false for each run through array
        for i in range(limit):  # Run through all elements until the upper limit
            if key(items[i]) > key(items[i + 1]):
                _swap(items, i, i + 1)
                continue_sort = True  # If there has been at least one swap, we should continue sorting..

        limit -= 1

    return items

def selection_sort_ordered(items, ascending):
    """
    Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.

    ascending : True/False

    Running time: O(n^2) average and worst case. Worst case when array is completely reversed
    Memory usage: O(1), Just some variables, we are swapping again so no extra memory usage
    """

    # Edge case
    if len(items) == 0:
        return []

    limit = 0

    while limit < len(items):
        min_max_index = limit
        min_max_value = items[min_max_index]
        for i in range(limit + 1, len(items)):  # Loop from limit+1 to the end of array to find min_max_index
            if ascending:
                if items[i] < min_max_value:
                    min_max_index = i
                    min_max_value = items[i]
            else:
                if items[i] > min_max_value:
                    min_max_index = i
                    min_max_value = items[i]
        _swap(items, min_max_index, limit)
        limit += 1

    return items


def selection_sort(items):
    """
    Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.

    Running time: O(n^2) average and worst case. Worst case when array is completely reversed
    Memory usage: O(1), Just some variables, we are swapping again so no extra memory usage
    """

    # Edge case
    if len(items) == 0:
        return []

    limit = 0

    while limit < len(items):
        minIndex = limit
        minValue = items[minIndex]
        for i in range(limit + 1, len(items)):  # Loop from limit+1 to the end of array to find minIndex
            if items[i] < minValue:
                minIndex = i
                minValue = items[i]
        _swap(items, minIndex, limit)
        limit += 1

    return items

def selection_sort_with_key(items, key):
    """
    Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.

    key: a lambda function that can transform what items are being compared

    Running time: O(n^2) average and worst case. Worst case when array is completely reversed
    Memory usage: O(1), Just some variables, we are swapping again so no extra memory usage
    """

    # Edge case
    if len(items) == 0:
        return []

    limit = 0

    while limit < len(items):
        minIndex = limit
        minValue = key(items[minIndex])
        for i in range(limit + 1, len(items)):  # Loop from limit+1 to the end of array to find minIndex
            if key(items[i]) < minValue:
                minIndex = i
                minValue = key(items[i])
        _swap(items, minIndex, limit)
        limit += 1

    return items

def insertion_sort_ordered(items, ascending):
    """
    Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.

    ascending: True/False

    Running time: O(n^2) average and worst case. Worst case when array is completely reversed
    Memory usage: O(1), Just some variables, we are swapping again so no extra memory usage
    """

    if len(items) == 0:
        return []

    limit = 1

    for i in range(1, len(items)):
        # Reverse bubble sort
        for j in range(0, i):
            lo_i = i - j
            hi_i = i - j - 1

            if ascending:
                if items[lo_i] < items[hi_i]:
                    _swap(items, lo_i, hi_i)
            else:
                if items[lo_i] > items[hi_i]:
                    _swap(items, lo_i, hi_i)

        limit += 1

    return items

def insertion_sort(items):
    """
    Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.

    Running time: O(n^2) average and worst case. Worst case when array is completely reversed
    Memory usage: O(1), Just some variables, we are swapping again so no extra memory usage
    """

    if len(items) == 0:
        return []

    limit = 1

    for i in range(1, len(items)):
        # Reverse bubble sort
        for j in range(0, i):
            lo_i = i - j
            hi_i = i - j - 1
            if items[lo_i] < items[hi_i]:
                _swap(items, lo_i, hi_i)

        limit += 1

    return items

def insertion_sort_with_key(items, key):
    """
    Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.

    key: a lambda function that can transform what items are being compared

    Running time: O(n^2) average and worst case. Worst case when array is completely reversed
    Memory usage: O(1), Just some variables, we are swapping again so no extra memory usage
    """

    if len(items) == 0:
        return []

    limit = 1

    for i in range(1, len(items)):
        # Reverse bubble sort
        for j in range(0, i):
            lo_i = i - j
            hi_i = i - j - 1
            if key(items[lo_i]) < key(items[hi_i]):
                _swap(items, lo_i, hi_i)

        limit += 1

    return items

def _swap(items, i, j):
    items[i], items[j] = items[j], items[i]


if __name__ == '__main__':
    student_tuples = [
        ('john', 'A', 12),
        ('jane', 'B', 10),
        ('dave', 'B', 15),
    ]

    print(f'students before: {student_tuples}')
    bubble_sort_with_key(student_tuples, lambda student: student[2])
    print(f'students after bubble sort with key: {student_tuples}')
    print(f'Is sorted by key: {is_sorted_with_key(student_tuples, lambda student: student[2])}')

    student_tuples = [
        ('john', 'A', 12),
        ('jane', 'B', 10),
        ('dave', 'B', 15),
    ]

    print(f'students before: {student_tuples}')
    selection_sort_with_key(student_tuples, lambda student: student[2])
    print(f'students after selection sort with key: {student_tuples}')
    print(f'Is sorted by key: {is_sorted_with_key(student_tuples, lambda student: student[2])}')

    student_tuples = [
        ('john', 'A', 12),
        ('jane', 'B', 10),
        ('dave', 'B', 15),
    ]

    print(f'students before: {student_tuples}')
    insertion_sort_with_key(student_tuples, lambda student: student[2])
    print(f'students after insertion sort with key: {student_tuples}')
    print(f'Is sorted by key: {is_sorted_with_key(student_tuples, lambda student: student[2])}')

    # l1 = [1, 4, 2, 5, 3]
    # print(f'Items before: {l1}')
    # bubble_sort_ordered(l1, False)
    # print(f'Items after ordered bubble sort: {l1}')
    # print(f'is_sorted? {is_sorted_ordered(l1, False)}')
    #
    # l2 = [1, 4, 2, 5, 3]
    # print(f'Items before: {l2}')
    # selection_sort_ordered(l2, False)
    # print(f'Items after ordered selection sort: {l2}')
    # print(f'is_sorted? {is_sorted_ordered(l2, False)}')
    #
    # l3 = [1, 4, 2, 5, 3]
    # print(f'Items before: {l3}')
    # insertion_sort_ordered(l3, False)
    # print(f'Items after ordered insertion sort: {l3}')
    # print(f'is_sorted? {is_sorted_ordered(l3, False)}')
