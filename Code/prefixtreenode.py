#!python3

class PrefixTreeNode:
    """PrefixTreeNode: A node for use in a prefix tree that stores a single
    character from a string and a structure of children nodes below it, which
    associates the next character in a string to the next node along its path from
    the tree's root node to a terminal node that marks the end of the string."""

    # Choose a type of data structure to store children nodes in
    # Hint: Choosing list or dict affects implementation of all child methods

    # Chose a hashmap
    CHILDREN_TYPE = dict

    def __init__(self, character=None):
        """Initialize this prefix tree node with the given character value, an
        empty structure of children nodes, and a boolean terminal property."""

        self.character = character
        self.children = PrefixTreeNode.CHILDREN_TYPE()
        self.terminal = False

    def set_terminal(self):
        """
        Time complexity: O(1)
        Memory complexity: O(1)
        """
        self.terminal = True

    def is_terminal(self):
        """
        Return True if this prefix tree node terminates a string.
        Time complexity: O(1)
        Memory complexity: O(1)
        """

        return self.terminal

    def num_children(self):
        """
        Return the number of children nodes this prefix tree node has.
        Time complexity: O(1) - pretty sure .keys() is constant time
        Memory complexity: O(1)
        """

        return len(self.children.keys())

    def has_child(self, character):
        """
        Return True if this prefix tree node has a child node that
        represents the given character amongst its children.
        Time complexity: O(1) - Lookup in HT is constant time
        Memory complexity: O(1)
        """

        return self.children.get(character) is not None

    def get_child(self, character):
        """
        Return this prefix tree node's child node that represents the given
        character if it is amongst its children, or raise ValueError if not.
        Time complexity: O(1) - Lookup in HT is constant time
        Memory complexity: O(1)
        """

        if self.has_child(character):
            return self.children.get(character)
        else:
            raise ValueError(f'No child exists for character {character!r}')

    def add_child(self, character, child_node):
        """
        Add the given character and child node as a child of this node, or
        raise ValueError if given character is amongst this node's children.
        Time complexity: O(1) - Insertion into HT is constant time
        Memory complexity: O(1)
        """

        if not self.has_child(character):
            self.children[character] = child_node
        else:
            raise ValueError(f'Child exists for character {character!r}')

    def get_children(self):
        """
        Time complexity: O(1) - pretty sure .values() is constant time under the hood
        Memory complexity: O(1)
        """
        return self.children.values()

    def __repr__(self):
        """Return a code representation of this prefix tree node."""

        return f'PrefixTreeNode({self.character!r})'

    def __str__(self):
        """Return a string view of this prefix tree node."""

        return f'({self.character})'
