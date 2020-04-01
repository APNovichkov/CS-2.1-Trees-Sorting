#!python3


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Time Complexity: O(n^2) worst case running time when array is completely reversed. Generally still quadratic...
    Memory Usage: We perform swapping, so everything happens in place. Only memory used is for the 3 variables"""

    limit = len(items) - 1  # set upper limit to array size
    continueSort = True

    while(continueSort):
        continueSort = False  # Set default to false for each run through array
        for i in range(limit):  # Run through all elements until the upper limit
            if items[i] > items[i + 1]:
                tmp = items[i]  # Swap elements here
                items[i] = items[i + 1]
                items[i + 1] = tmp
                continueSort = True  # If there has been at least one swap, we should continue sorting..
        limit -= 1

    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item

    limit = 0
    while()


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items

def _swap(items, i, j):
    pass


if __name__ == '__main__':
    items = [4, 5, 2, 3, 6, 1, 10, 2, 4]
    print("Items before sorting: {}".format(items))
    print("Items after sorting: {}".format(bubble_sort(items)))
