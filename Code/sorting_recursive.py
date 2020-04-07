#!python

from sorting_iterative import insertion_sort

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list

    print(f'Merging {items1} and {items2} ')

    out = []
    i = 0
    j = 0

    while(i + j != len(items1) + len(items2)):
        if i == len(items1):
            out.append(items2[j])
            j += 1
            continue

        if j == len(items2):
            out.append(items1[i])
            i += 1
            continue

        # if i == len(items1):
        #     out.append(items2[j:])
        #     break
        #
        # if j == len(items2):
        #     out.append(items1[i:])
        #     break

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

    items = merge(left, right)
    return items

def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order

    if len(items) <= 2:
        return merge(items[:1], items[1:])

    half = len(items) // 2
    left = items[:half]
    right = items[half:]

    return merge(merge_sort(left), merge_sort(right))

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
    # l1 = [3, 5]
    # l2 = [1, 10]
    #
    # merged_l = merge(l1, l2)
    # print(f"Merged: {merged_l}")
    #
    # l3 = [4, 3, 5, 6, 7, 10, 1, 2, 2]
    # split_sort_merged = split_sort_merge(l3)
    # print(f"Split sort merged: {split_sort_merged}")

    l4 = [4, 3, 2, 5, 10, 3, 10, 2, 3, 3, 2, 3, 100, 2, 3]
    merge_sorted = merge_sort(l4)
    print(f'Merge sorted: {merge_sorted}')
