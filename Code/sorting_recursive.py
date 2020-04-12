#!python

from sorting_iterative import insertion_sort
from random import seed
from random import randint

def merge(items1, items2):
    """
    Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.

    Running time: O(n), just running through both of the arrays once
    Memory usage: O(n), created a new array of size n to do the merging
    """

    if items1 is None:
        return items2

    if items2 is None:
        return items1

    out = []
    i = 0
    j = 0

    while(i + j != len(items1) + len(items2)):
        if i == len(items1):
            out.extend(items2[j:])
            break

        if j == len(items2):
            out.extend(items1[i:])
            break

        if items1[i] <= items2[j]:
            out.append(items1[i])
            i += 1
        else:
            out.append(items2[j])
            j += 1

    return out

def split_sort_merge(items):
    """
    Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.

    Running time: O(n^2) still, but faster than just insertion sort because we cut time by 2
    Memory usage: O(n) because we created 1 array of constant sapce when we merged left and right sides
    """

    half = len(items) // 2
    left = items[:half]
    right = items[half:]

    insertion_sort(left)
    insertion_sort(right)

    items[:] = merge(left, right)


def merge_sort(items):
    """
    Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.

    Running time: O(nlogn), same for Best/Worst case, consistently the same Time Complexity
    Memory Usage: O(nlogn), Have to create a new array per split to combine two arrays
    """

    if len(items) <= 2:
        return merge(items[:1], items[1:])

    half = len(items) // 2
    left = items[:half]
    right = items[half:]

    items[:] = merge(merge_sort(left), merge_sort(right))
    return items

def partition_constant(items, low, high):
    pivot = high

    i = low
    for j in range(low, high):
        if items[j] <= items[pivot]:
            swap(items, i, j)
            i += 1

    (items[i], items[high]) = (items[high], items[i])

    return i

def partition_random(items, low, high):
    """
    Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.

    Running time: O(n) worst and best case, running from low to high
    Memory usage: O(1) because partitioning in-place
    """
    seed(1)
    pivot = randint(low, high - 1)

    i = low
    for j in range(low, high + 1):
        if j == pivot:
            continue
        if items[j] <= items[pivot]:
            if i == pivot:
                pivot = j
            swap(items, i, j)
            i += 1

    (items[i], items[pivot]) = (items[pivot], items[i])

    return i


def swap(items, i, j):
    items[i], items[j] = items[j], items[i]

def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.

    Best case running time: O(nlogn) when we choose a good pivot, because then we have balanced partitioning
    Worst case running time: O(n^2) when we have a reverse list, we end up with a one-sided linked list partitioning
    Memory usage: O(1) Becase we are partitioning in-place, not creating any new arrays
    """

    if high is None or low is None:
        low = 0
        high = len(items) - 1

    if low < high:
        p_index = partition_random(items, low, high)
        quick_sort(items, low, p_index - 1)
        quick_sort(items, p_index + 1, high)


if __name__ == '__main__':

    # l5 = [4, 3, 2, 3, 2, 10, 9, 5]
    # print(f'before sorting: {l5}')
    # # partition(l5, 0, len(l5)-1)
    # quick_sort(l5)
    # print(f'quick sorted: {l5}')

    # l1 = [3, 5]
    # l2 = [1, 10]
    #
    # print(f'Trying to merge {l1} and {l2}')
    # merged_l = merge(l1, l2)
    # print(f"Merged: {merged_l}\n")
    #
    # l3 = [4, 3, 5, 6, 7, 10, 1, 2, 2]
    # print(f'Trying to split sort merge {l3}')
    # split_sort_merge(l3)
    # print(f"Split sort merged: {l3}\n")
    #
    l4 = [8, 14, 2, 20, 15, 7, 17, 20, 2]
    # l4 = [2, 4, 2]
    print(f'Trying to sort {l4}')
    merge_sort(l4)
    print(f'Merge sorted: {l4}\n')
