#!python

from sorting_iterative import insertion_sort

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.

    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

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
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    half = len(items) // 2
    left = items[:half]
    right = items[half:]

    insertion_sort(left)
    insertion_sort(right)

    items[:] = merge(left, right)


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    if len(items) <= 2:
        items[:] = merge(items[:1], items[1:])
        return items

    half = len(items) // 2
    left = items[:half]
    right = items[half:]

    items[:] = merge(merge_sort(left), merge_sort(right))

def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort


if __name__ == '__main__':
    l1 = [3, 5]
    l2 = [1, 10]

    print(f'Trying to merge {l1} and {l2}')
    merged_l = merge(l1, l2)
    print(f"Merged: {merged_l}\n")

    l3 = [4, 3, 5, 6, 7, 10, 1, 2, 2]
    print(f'Trying to split sort merge {l3}')
    split_sort_merge(l3)
    print(f"Split sort merged: {l3}\n")

    l4 = [4, 3]
    print(f'Trying to sort {l4}')
    merge_sort(l4)
    print(f'Merge sorted: {l4}\n')
