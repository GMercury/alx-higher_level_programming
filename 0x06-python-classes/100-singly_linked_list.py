#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

        @property
        def data(self):
            return self.__data

        @data.setter
        def data(self, data):
            if type(data) is not int:
                raise TypeError("data must be an integer")
            else:
                self.__data = data

        @property
        def next_node(self):
            return self.__next_node

        @next_node.setter
        def next_node(self, next_node):
            if type(next_node) is not __main__.Node:
                raise TypeError("next_node must be a Node object")
            else:
                self.__next_node = next_node


class SinglyLinkedList:
    def __init__(self):
        self.__head = head

        def sorted_insert(self, value)
        new_Node = Node(value)
        while Node.data < value:
            tmp_Node = Node.next_node
        new_Node.next_node = tmp_Node
