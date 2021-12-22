# todo: what is this? - the web that we took the function from
# https://medium.com/@kevin.michael.horan/data-structures-linked-lists-with-python-2d0ec4fdc18c
from typing import Any


class Node:
    """
    creates a single node of data with value and a pointer for the next node
    """
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None

    def __str__(self) -> str:
        return str(self.value)


class Linked_list:
    """
    creates a linked list of nodes

    possible methods:
    add to start - adds a new node to the beginning of the linked list
    add to end - adds a new node to the end of the linked list
    all nodes as list - returns a list of all the data of different Nodes
                        by order from first to last
    remove last - removes the last Node in the linked list
    get head - returns the data of the first bode in the linked list
    """
    def __init__(self) -> None:
        self.count = 0
        self.tail = None
        self.head = None

    def add_to_start(self, new_node: Node) -> None:
        """
        Add node to start of list
               (Head)[2] -> [3](Tail)
        (Head)[1] -> [2] -> [3](Tail)
        """
        temp = self.head
        self.head = new_node
        new_node.next = temp

        self.count += 1
        if self.count == 1:
            self.tail = self.head

    def add_to_end(self, new_node: Node) -> None:
        """
        Add node to end of list
        (Head)1 -> 2(Tail)
        (Head)1 -> 2 -> 3(Tail)
        """
        if self.count == 0:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.count += 1

    def all_nodes_as_list(self) -> list[Any]:
        """
        returns a list of all the data in the linked list from start to finish
        :return: list of all the data in the different nodes by order
        """
        pointer = self.head
        list_all: list = []
        finished: bool = False
        while not finished:
            list_all.append(pointer.value)
            pointer = pointer.next
            if pointer is None:
                finished = True
        return list_all

    def remove_last(self) -> None:
        """
        Remove node from end of list
        (Head)1 -> 2 -> 3(Tail)
        (Head)1 -> 2(Tail)
        """
        if self.count > 0:
            if self.count == 1:
                self.head = None
                self.tail = None
            else:
                current = self.head
                while current.next != self.tail:
                    current = current.next
                current.next = None
                self.tail = current
            self.count -= 1

    def get_head(self) -> Any:
        """
        :return: the data value of the firs Node in the linked list
        """
        return self.head






 # # todo: take care of this comment - i think its not used
    # def __str__(self) -> str:  # see if useful - i added and can be deleted
    #     pointer = self.head
    #     if self.head is None:
    #         return ""
    #     final = ""
    #     finished = False
    #     while not finished:
    #         final += str(pointer.value)
    #         pointer = pointer.next
    #         if pointer is None:
    #             finished = True
    #     return final

"""
    def remove_first(self):
       
        # Remove node from start of list
        # (Head)[1] -> [2] -> [3](Tail)
        #        (Head)[2] -> [3](Tail)
     
        if self.count > 0:
            self.head = self.head.next
            self.count -= 1
            if self.count == 0:
                self.tail = None

    def remove_from_list(self, search_value):
        
        # Remove node by value
        # (Head)[1] -> [2] -> [3](Tail)
        # (Head)[1] --------> [3](Tail)
      
        previous = None
        current = self.head

        while current is not None:
            # A match is found!
            if current.value == search_value:

                # We're in the middle or end of the list
                if previous is not None:
                    previous.next = current.next
                    # We're at the very end of the list
                    if current.next is None:
                        self.tail = previous
                    self.count -= 1
                # We're at the very start of the list
                else:
                    self.remove_first()
                return True
            previous = current
            current = current.next
        return False

"""

