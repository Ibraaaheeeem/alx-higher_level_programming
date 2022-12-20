#!/usr/bin/python3
"""Documentation for singly linked list classes"""


class Node():
    """Node class for a singly-linked list"""

    def __init__(self, data, next_node=None):
        """Instantiation of a singly-linked list node
        Args:
            data (int): data contained in the node
            next_node (Node, optional): the next node of the list
        Raises:
            TypeError: if the data is not an integer of next_node is not
            a Node instance
        """

        if type(data) != int:
            raise TypeError("data must be an integer")
        self.__data = data

        if next_node is None or isinstance(next_node, Node):
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")

    @property
    def data(self):
        """Returns the data value in the current node

