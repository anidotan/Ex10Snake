import game_parameters
import pytest
# from linked_list import Node, LinkedList
from better_linked_list import *


class Snake:
    """
    contains a list of all the cells a snake is in
    """

    def __init__(self):
        # creating the snake first three cells
        cell_1 = Node((10, 10))
        cell_2 = Node((10, 9))
        cell_3 = Node((10, 8))
        # creating the snake himself
        self.the_snake = Linked_list()
        self.the_snake.add_to_start(cell_1)
        self.the_snake.add_to_end(cell_2)
        self.the_snake.add_to_end(cell_3)

        # self.the_snake.add_to_start(cell_1)
        # temp_snake.add_to_start(cell_1)
        # temp_snake.add_to_end(cell_2)
        # temp_snake.add_to_end(cell_3)
        # print(f'after printing:{temp_snake}')
        # self.the_snake = temp_snake
        # print(self.the_snake == temp_snake)
        # print(f'type: {type(self.the_snake)}')
        # print(f'the snake {self.the_snake}')

        # self.head: tuple = self.the_snake.head.value
        # self.tail: tuple = self.the_snake.tail.value
        # self.coordinates: list = self.the_snake.all_nodes_as_list()
        # self.length = self.the_snake.count

    def __str__(self):
       return str(self.the_snake)

    def forward_head_only(self, direction):
        """
        adds three cells
        :return:
        """
        if direction == "Up":
            cur_head_cell = self.the_snake.head.value
            x, y = cur_head_cell
            new_head_node = Node(tuple((x, y + 1)))
            self.the_snake.add_to_start(new_head_node)

        elif direction == "Down":
            cur_head_cell = self.the_snake.head.value
            x, y = cur_head_cell
            new_head_node = Node(tuple((x, y - 1)))
            self.the_snake.add_to_start(new_head_node)

        elif direction == "Left":
            cur_head_cell = self.the_snake.head.value
            x, y = cur_head_cell
            new_head_node = Node(tuple((x - 1, y)))
            self.the_snake.add_to_start(new_head_node)

        elif direction == "Right":
            cur_head_cell = self.the_snake.head.value
            x, y = cur_head_cell
            new_head_node = Node(tuple((x + 1, y)))
            self.the_snake.add_to_start(new_head_node)



    def simple_move(self, direction):
        """
        move one forward

        :return: delete last cell and add new one to head
        """
        # todo: add possible moves
        if direction == "Up":
            cur_head_cell = self.the_snake.head.value
            x, y = cur_head_cell
            new_head_node = Node(tuple((x, y + 1)))
            self.the_snake.add_to_start(new_head_node)
            self.the_snake.remove_last()

        elif direction == "Down":
            cur_head_cell = self.the_snake.head.value
            x, y = cur_head_cell
            new_head_node = Node(tuple((x, y - 1)))
            self.the_snake.add_to_start(new_head_node)
            self.the_snake.remove_last()

        elif direction == "Left":
            cur_head_cell = self.the_snake.head.value
            x, y = cur_head_cell
            new_head_node = Node(tuple((x - 1, y)))
            self.the_snake.add_to_start(new_head_node)
            self.the_snake.remove_last()

        elif direction == "Right":
            cur_head_cell = self.the_snake.head.value
            x, y = cur_head_cell
            new_head_node = Node(tuple((x + 1, y)))
            self.the_snake.add_to_start(new_head_node)
            self.the_snake.remove_last()
