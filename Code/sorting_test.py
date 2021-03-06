#!python

from sorting import random_ints
from sorting_iterative import is_sorted, bubble_sort, selection_sort, insertion_sort
from sorting_recursive import split_sort_merge, merge_sort, quick_sort
from sorting_integer import counting_sort, bucket_sort
import unittest


class IsSortedTest(unittest.TestCase):

    def test_is_sorted_on_sorted_integers(self):
        # Positive test cases (examples) with lists of sorted integers
        assert is_sorted([]) is True  # Empty lists are vacuously sorted
        assert is_sorted([3]) is True  # Single item is trivially sorted
        assert is_sorted([3, 3]) is True  # Duplicate items are in order
        assert is_sorted([3, 5]) is True
        assert is_sorted([3, 5, 7]) is True
        assert is_sorted([-1, 3, 5, 10]) is True
        assert is_sorted([2, 2, 3, 3, 3, 3, 10]) is True
        assert is_sorted([0, 0, 0, 0, 0, 10]) is True
        assert is_sorted([1, 2, 2, 2, 10, 1000, 10001]) is True

    def test_is_sorted_on_unsorted_integers(self):
        # Negative test cases (counterexamples) with lists of unsorted integers
        assert is_sorted([5, 3]) is False
        assert is_sorted([3, 5, 3]) is False
        assert is_sorted([7, 5, 3]) is False
        assert is_sorted([1, 1, 1, 1, 4, 5, 2]) is False
        assert is_sorted([5, 4, 3, 2, 1]) is False
        assert is_sorted([1, 1, 1, 1, 1, -1, 1, 1, 1, 1]) is False
        assert is_sorted([0, -1, 0]) is False
        assert is_sorted([10, 10, 10, 9, 11]) is False

    def test_is_sorted_on_sorted_strings(self):
        # Positive test cases (examples) with lists of sorted strings
        assert is_sorted(['A']) is True  # Single item is trivially sorted
        assert is_sorted(['A', 'A']) is True  # Duplicate items are in order
        assert is_sorted(['A', 'B']) is True
        assert is_sorted(['A', 'B', 'C']) is True
        assert is_sorted(['A', 'C', 'D', 'E']) is True
        assert is_sorted(['Z', 'Z', 'Z', 'Z']) is True
        assert is_sorted(['A', 'A', 'Z', 'Z', 'Z']) is True
        assert is_sorted(['B', 'C', 'C', 'Z', 'Z', 'Z']) is True
        assert is_sorted(['A', 'A', 'A', 'G', 'G', 'Z', 'Z']) is True

    def test_is_sorted_on_unsorted_strings(self):
        # Negative test cases (counterexamples) with lists of unsorted strings
        assert is_sorted(['B', 'A']) is False
        assert is_sorted(['A', 'B', 'A']) is False
        assert is_sorted(['C', 'B', 'A']) is False
        assert is_sorted(['Z', 'Z', 'Z', 'Z', 'A']) is False
        assert is_sorted(['F', 'F', 'F', 'E', 'B', 'A', 'A']) is False
        assert is_sorted(['R', 'A', 'A', 'A', 'A', 'B', 'C']) is False
        assert is_sorted(['A', 'B', 'C', 'D', 'A']) is False
        # TODO: Write more negative test cases with assert is False statements
        # You'll need a lot more than this to test sorting algorithm robustness
        # ...

    def test_is_sorted_on_sorted_tuples(self):
        # Positive test cases (examples) with lists of sorted tuples
        assert is_sorted([(3, 5)]) is True  # Single item
        assert is_sorted([(3, 'A')]) is True  # Single item
        assert is_sorted([('A', 3)]) is True  # Single item
        assert is_sorted([('A', 'B')]) is True  # Single item
        assert is_sorted([(3, 5), (3, 5)]) is True  # Duplicate items
        assert is_sorted([(3, 'A'), (3, 'A')]) is True  # Duplicate items
        assert is_sorted([('A', 3), ('A', 3)]) is True  # Duplicate items
        assert is_sorted([('A', 'B'), ('A', 'B')]) is True  # Duplicate items
        assert is_sorted([('A', 3), ('B', 5)]) is True  # Both items sorted
        assert is_sorted([('A', 3), ('B', 3)]) is True  # First item sorted
        assert is_sorted([('A', 3), ('A', 5)]) is True  # Second item sorted
        assert is_sorted([(3, 'A'), (5, 'B')]) is True  # Both items sorted
        assert is_sorted([(3, 'A'), (5, 'A')]) is True  # First item sorted
        assert is_sorted([(3, 'A'), (3, 'B')]) is True  # Second item sorted
        assert is_sorted([('A', 'B'), ('A', 'B')]) is True
        assert is_sorted([(-1, 0), (1, 2)]) is True
        assert is_sorted([('C', 10), ('D', 10)]) is True

    def test_is_sorted_on_unsorted_tuples(self):
        # Negative test cases (counterexamples) with lists of unsorted tuples
        assert is_sorted([(5, 'B'), (3, 'A')]) is False  # Both items unsorted
        assert is_sorted([(5, 'A'), (3, 'B')]) is False  # First item unsorted
        assert is_sorted([(3, 'B'), (3, 'A')]) is False  # Second item unsorted
        assert is_sorted([('B', 5), ('A', 3)]) is False  # Both items unsorted
        assert is_sorted([('B', 3), ('A', 5)]) is False  # First item unsorted
        assert is_sorted([('A', 5), ('A', 3)]) is False  # Second item unsorted
        assert is_sorted([('A', 'B'), ('A', 'A')]) is False
        assert is_sorted([(4, 2), (4, 1)]) is False
        assert is_sorted([(1, 2), (1, 2), (1, 1)]) is False
        assert is_sorted([('A', 'G'), ('A', 'E')]) is False

class IntegerSortTest(unittest.TestCase):

    def test_sort_on_empty_list(self):
        items = []
        sort(items)
        assert items == []  # List should not be changed

    def test_sort_on_small_lists_of_integers(self):
        items1 = [3]
        sort(items1)
        assert items1 == [3]  # List should not be changed
        items2 = [5, 3]
        sort(items2)
        assert items2 == [3, 5]  # List should be in sorted order
        items3 = [5, 7, 3]
        sort(items3)
        assert items3 == [3, 5, 7]
        items4 = [1, 2, 1]
        sort(items4)
        assert items4 == [1, 1, 2]
        items5 = [-1, 0, -1]
        sort(items5)
        assert items5 == [-1, -1, 0]
        items6 = [1, 1, 0, 10]
        sort(items6)
        assert items6 == [0, 1, 1, 10]

    def test_sort_on_small_lists_of_integers_with_duplicates(self):
        items1 = [3, 3]
        sort(items1)
        assert items1 == [3, 3]  # List should not be changed
        items2 = [3, 5, 3]
        sort(items2)
        assert items2 == [3, 3, 5]  # List should be in sorted order
        items3 = [5, 5, 3, 5, 3]
        sort(items3)
        assert items3 == [3, 3, 5, 5, 5]
        items4 = [7, 5, 3, 7, 5, 7, 5, 3, 7]
        sort(items4)
        assert items4 == [3, 3, 5, 5, 5, 7, 7, 7, 7]
        items5 = [4, 2, 1, 4, 2, 1, 4, 2, 1]
        sort(items5)
        assert items5 == [1, 1, 1, 2, 2, 2, 4, 4, 4]
        items6 = [1, 0, 0, 0, 0, 1]
        sort(items6)
        assert items6 == [0, 0, 0, 0, 1, 1]
        items7 = [-5, 1, 0, 0, 0, 10, 1]
        sort(items7)
        assert items7 == [-5, 0, 0, 0, 1, 1, 10]

    def test_sort_on_lists_of_random_integers(self):
        # Generate list of 10 random integers from range [1...20]
        items1 = random_ints(10, 1, 20)
        sorted_items1 = sorted(items1)  # Create a copy of list in sorted order
        sort(items1)  # Call mutative sort function to sort list items in place
        assert items1 == sorted_items1

        # Generate list of 20 random integers from range [1...50]
        items2 = random_ints(20, 1, 50)
        sorted_items2 = sorted(items2)  # Copy
        sort(items2)  # Mutate
        assert items2 == sorted_items2

        # Generate list of 30 random integers from range [1...100]
        items3 = random_ints(30, 1, 100)
        sorted_items3 = sorted(items3)  # Copy
        sort(items3)  # Mutate
        assert items3 == sorted_items3

    def test_sort_on_lists_of_random_integers_with_duplicates(self):
        # Generate list of 20 random integers from range [1...10]
        items1 = random_ints(20, 1, 10)
        sorted_items1 = sorted(items1)  # Create a copy of list in sorted order
        sort(items1)  # Call mutative sort function to sort list items in place
        assert items1 == sorted_items1

        # Generate list of 50 random integers from range [1...20]
        items2 = random_ints(50, 1, 20)
        sorted_items2 = sorted(items2)  # Copy
        sort(items2)  # Mutate
        assert items2 == sorted_items2

        # Generate list of 100 random integers from range [1...30]
        items3 = random_ints(100, 1, 30)
        sorted_items3 = sorted(items3)  # Copy
        sort(items3)  # Mutate
        assert items3 == sorted_items3

    # Doesnt work anymore because we are choosing random pivots
    # def test_partition_sort(self):
    #     items1 = [1, 4, 2, 3]
    #     pivot_index = partition(items1, 0, 3)
    #     assert pivot_index == 2
    #     items2 = [3, 2, 1, 4, 10, 2]
    #     pivot_index = partition(items2, 0, len(items2) - 1)
    #     assert pivot_index == 2


class StringSortTest(unittest.TestCase):

    def test_sort_on_small_lists_of_strings(self):
        items1 = ['A']
        sort(items1)
        assert items1 == ['A']  # List should not be changed
        items2 = ['B', 'A']
        sort(items2)
        assert items2 == ['A', 'B']  # List should be in sorted order
        items3 = ['B', 'C', 'A']
        sort(items3)
        assert items3 == ['A', 'B', 'C']
        items4 = ['G', 'G', 'A', 'C']
        sort(items4)
        assert items4 == ['A', 'C', 'G', 'G']
        items5 = ['Z', 'Y', 'W', 'A', 'A']
        sort(items5)
        assert items5 == ['A', 'A', 'W', 'Y', 'Z']

    def test_sort_on_fish_book_title(self):
        items = 'one fish two fish red fish blue fish'.split()
        sorted_items = sorted(items)  # Create a copy of list in sorted order
        sort(items)  # Call mutative sort function to sort list items in place
        assert items == sorted_items

    def test_sort_on_seven_dwarf_names(self):
        items = 'Doc Grumpy Happy Sleepy Bashful Sneezy Dopey'.split()
        sorted_items = sorted(items)  # Copy
        sort(items)  # Mutate
        assert items == sorted_items


def get_sort_function():
    """Read command-line argument and return sort function with that name."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    if len(args) == 0:
        script = sys.argv[0]  # Get script file name
        print('Usage: {} sort_function'.format(script))
        print('Example: {} bubble_sort'.format(script))
        return

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        if sort_name in globals():
            sort_function = globals()[sort_name]
            return sort_function
        else:
            # Don't explode, just warn user and show list of sorting functions
            print('Sorting function {!r} does not exist'.format(sort_name))
            print('Available sorting functions:')
            for name in globals():
                if 'sort' in name:
                    print('    {}'.format(name))
            return


# If using PyTest, change this variable to the sort function you want to test
sort = quick_sort


if __name__ == '__main__':
    # Get sort function from command-line argument
    # FIXME: This is causing unittest to throw an error
    # sort = get_sort_function()
    unittest.main()
