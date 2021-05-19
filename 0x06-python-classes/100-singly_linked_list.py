#!/usr/bin/python3
"""Class Node definition"""


class Node:
    """Class Node"""
    def __init__(self, data, next_node=None):
        """Function to initialize the Node object"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """property to retrieve it"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter of data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """property of next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """"set the pointer of next_node"""
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Class LinkedList"""
    def __init__(self):
        """Function to initialize the Linked List"""
        self.__head = None

    def sorted_insert(self, value):
        """ Insert a new node in the correct index
        of a sorted linked list"""
        new_node = Node(value)
        if not self.__head or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while (tmp.next_node and ((tmp.next_node).data < value)):
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """Print singly linked list"""
        tmp = self.__head
        result = ""
        while (tmp):
            result = result + str(tmp.data)
            tmp = tmp.next_node
            if (tmp):
                result = result + "\n"
        return (result)
