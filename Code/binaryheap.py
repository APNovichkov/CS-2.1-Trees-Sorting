#!python


class BinaryMinHeap(object):
    """BinaryMinHeap: a partially ordered collection with efficient methods to
    insert new items in partial order and to access and remove its minimum item.
    Items are stored in a dynamic array that implicitly represents a complete
    binary tree with root node at index 0 and last leaf node at index n-1."""

    def __init__(self, items=None):
        """Initialize this heap and insert the given items, if any."""
        # Initialize an empty list to store the items
        self.items = []
        if items:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this heap."""
        return 'BinaryMinHeap({})'.format(self.items)

    def is_empty(self):
        """Return True if this heap is empty, or False otherwise."""
        # TODO: Check if empty based on how many items are in the list
        # ...
        return len(self.items) == 0

    def size(self):
        """Return the number of items in this heap."""
        return len(self.items)

    def insert(self, item):
        """Insert the given item into this heap.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""

        # Insert the item at the end and bubble up to the root
        self.items.append(item)
        if self.size() > 1:
            self._bubble_up(self._last_index())

    def get_min(self):
        """Return the minimum item at the root of this heap.
        Best and worst case running time: O(1) because min item is the root."""

        if self.size() == 0:
            raise ValueError('Heap is empty and has no minimum item')
        assert self.size() > 0
        return self.items[0]

    def delete_min(self):
        """Remove and return the minimum item at the root of this heap.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""

        if self.size() == 0:
            raise ValueError('Heap is empty and has no minimum item')
        elif self.size() == 1:
            # Remove and return the only item
            return self.items.pop()
        assert self.size() > 1
        min_item = self.items[0]
        # Move the last item to the root and bubble down to the leaves
        last_item = self.items.pop()
        self.items[0] = last_item
        if self.size() > 1:
            self._bubble_down(0)
        return min_item

    def replace_min(self, item):
        """Remove and return the minimum item at the root of this heap,
        and insert the given item into this heap.
        This method is more efficient than calling delete_min and then insert.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""

        if self.size() == 0:
            raise ValueError('Heap is empty and has no minimum item')
        assert self.size() > 0
        min_item = self.items[0]
        # Replace the root and bubble down to the leaves
        self.items[0] = item
        if self.size() > 1:
            self._bubble_down(0)
        return min_item

    def _bubble_up(self, index):
        """Ensure the heap ordering property is true above the given index,
        swapping out of order items, or until the root node is reached.
        Best case running time: O(1) if parent item is smaller than this item.
        Worst case running time: O(log n) if items on path up to root node are
        out of order. Maximum path length in complete binary tree is log n."""

        c_index = index
        p_index = self._parent_index(index)

        while(self._valid_index(p_index) and self.items[c_index] < self.items[p_index]):
            self._swap(c_index, p_index)
            c_index = p_index
            p_index = self._parent_index(c_index)


    def _bubble_down(self, index):
        """Ensure the heap ordering property is true below the given index,
        swapping out of order items, or until a leaf node is reached.
        Best case running time: O(1) if item is smaller than both child items.
        Worst case running time: O(log n) if items on path down to a leaf are
        out of order. Maximum path length in complete binary tree is log n."""

        p_index = index
        left_index = self._left_child_index(p_index)
        right_index = left_index + 1

        while(self._valid_index(left_index)):
            min_index = left_index
            if(self._valid_index(right_index) and self.items[right_index] < self.items[left_index]):
                min_index = right_index

            # Test if we need to bubble down any longer
            if(self.items[p_index] < self.items[min_index]): 
                break
            
            # Swap min and parent index and reset variables
            self._swap(p_index, min_index)
            p_index = min_index
            left_index = self._left_child_index(p_index)
            right_index = left_index + 1


    def _swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def _valid_index(self, index):
        return 0 <= index <= self._last_index()

    def _last_index(self):
        """Return the last valid index in the underlying array of items."""
        return len(self.items) - 1

    def _parent_index(self, index):
        """Return the parent index of the item at the given index."""
        return (index - 1) >> 1  # Shift right to divide by 2

    def _left_child_index(self, index):
        """Return the left child index of the item at the given index."""
        return (index << 1) + 1  # Shift left to multiply by 2


def test_binary_min_heap():
    # Create a binary min heap of 7 items
    items = [9, 25, 86, 3, 29, 5, 55]
    heap = BinaryMinHeap()
    print('heap: {}'.format(heap))

    print('\nInserting items:')
    for index, item in enumerate(items):
        heap.insert(item)
        print('insert({})'.format(item))
        print('heap: {}'.format(heap))
        print('size: {}'.format(heap.size()))
        heap_min = heap.get_min()
        real_min = min(items[: index + 1])
        correct = heap_min == real_min
        print('get_min: {}, correct: {}'.format(heap_min, correct))

    print('\nDeleting items:')
    for item in sorted(items):
        heap_min = heap.delete_min()
        print('delete_min: {}'.format(heap_min))
        print('heap: {}'.format(heap))
        print('size: {}'.format(heap.size()))


if __name__ == '__main__':
    test_binary_min_heap()
