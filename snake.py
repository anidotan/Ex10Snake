from linked_list import *


class Snake:
    """
    creates a snake instance for the game of snake
    starts in the length of 3, facing up and its head in cell (10,10)

    methods:
    forward head only - for the times when a snake eats an apple his body
                        stays in the same place and only its head continue
                        moving forward so that his body is actually growing
    simple move - when the snake is just moving - deletes its last cell and
                puts a new want in front of the snake, according to its moving
                direction
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

    def forward_head_only(self, direction):
        """
        adds a cell in front of the head without moving the body
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
        deletes the last cell and adds a new one in front of it according to
        the moving direction
        """
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

    def get_all_coor(self):
        """
        :return: all of the coordinates of the snake as a list[tuple(x,y)]
        """
        return self.the_snake.all_nodes_as_list()

    def get_head(self):
        """
        :return: tuple(x, y) of the snakes head location
        """
        return self.the_snake.head.value
