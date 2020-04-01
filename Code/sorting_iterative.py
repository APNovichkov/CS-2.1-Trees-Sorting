#!python3
from random import shuffle


def is_sorted(items):
    """

    Return a boolean indicating whether given items are in sorted order.

    Running time: O(n) Linear time, only one for loop. Best case is first item is out of place. Worst case array is sorted
    Memory usage: Just the variable to hold the iterator

    """

    for i in range(len(items) - 1):
        if items[i] > items[i + 1]:
            return False

    return True


def bubble_sort(items):
    """

    Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.

    Time Complexity: O(n^2) worst case running time when array is completely reversed. Generally still quadratic...
    Memory Usage: We perform swapping, so everything happens in place. Only memory used is for some of the variables

    """

    if len(items) == 0:
        return []

    limit = len(items) - 1  # set upper limit to array size
    continueSort = True

    while(continueSort):
        continueSort = False  # Set default to false for each run through array
        for i in range(limit):  # Run through all elements until the upper limit
            if items[i] > items[i + 1]:
                _swap(items, i, i + 1)
                continueSort = True  # If there has been at least one swap, we should continue sorting..
        limit -= 1

    return items


# TODO fix bug!
def selection_sort(items):
    """

    Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.

    Running time: O(n^2) average and worst case. Worst case when array is completely reversed
    Memory usage: Just some variables, we are swapping again so no extra memory usage

    """

    if len(items) == 0:
        return []

    limit = 0
    isSorted = False

    while not isSorted:
        isSorted = True
        minIndex = limit
        minValue = items[minIndex]
        for i in range(limit + 1, len(items)):  # Loop from limit+1 to the end of array to find minIndex
            if items[i - 1] < items[i]:
                isSorted = False
                # print('isSortedIsFalse @ index: {}'.format(i))
            if items[i] < minValue:
                minIndex = i
                minValue = items[i]
        _swap(items, minIndex, limit)
        limit += 1

    return items


def insertion_sort(items):
    """

    Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.

    Running time: O(n^2) average and worst case. Worst case when array is completely reversed
    Memory usage: Just some variables, we are swapping again so no extra memory usage

    """

    if len(items) == 0:
        return []

    limit = 1

    for i in range(1, len(items)):
        # Reverse bubble sort
        for j in range(0, limit):
            lo_i = limit - j
            hi_i = limit - j - 1
            if items[lo_i] < items[hi_i]:
                _swap(items, lo_i, hi_i)

        limit += 1

    return items


def _swap(items, i, j):
    tmp = items[i]
    items[i] = items[j]
    items[j] = tmp


if __name__ == '__main__':
    items = [i for i in range(50)]
    shuffle(items)
    # print("Items before sorting: {}".format(items))
    print(f"Is sorted? {is_sorted(items)}")
    # print("Items after Bubble Sort: {}".format(bubble_sort(items)))
    print(f"Is sorted? {is_sorted(bubble_sort(items))}")
    # print("Items after Selection Sort: {}".format(selection_sort(items)))
    print(f"Is sorted? {is_sorted(selection_sort(items))}")
    # print("Items after Insertion Sort: {}".format(insertion_sort(items)))
    print(f"Is sorted? {is_sorted(insertion_sort(items))}")
