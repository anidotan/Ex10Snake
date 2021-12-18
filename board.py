from typing import List, Tuple
import snake
from bomb import Bomb
from apple import Apple

import game_parameters


class Board:
    def __init__(self, height: int, width: int):
        self.__height = height
        self.__width = width
        self.__locations = [(x, y) for x in range(self.__width) for y in
                            range(self.__height)]
        self.__score = 0
        self.__snake = None
        self.__snake_loc = []
        self.__apples = set()
        self.__apples_loc = []
        self.__bomb = None
        self.__bomb_loc = []
        self.__explosion_loc = []
        self.__explosion_loc = []
        self.__eating_counter = 0


    def initialize_board(self):
        """
        create first board-frame
        1. place the snake
        2. place the bombs
        3. place the apples
        :return: board
        """
        self.__snake = snake.Snake()
        self.__snake = [(10, 10), (10, 9), (10, 8)]
        locations_in_use = self.__snake[:]

        # add 3 apples to the board
        while len(self.__apples) < 3:
            x, y, score = game_parameters.get_random_apple_data()
            apple_location = (x,y)
            if apple_location not in locations_in_use:
                self.__apples.add(Apple(x, y, score))
                locations_in_use.append(apple_location)
                self.__apples_loc.append(apple_location)

        # todo: check if its okay i did bomb loc and not the bomb)
        # add 1 bomb to the board
        while len(self.__bomb_loc) < 1:
            x, y, radius, time = game_parameters.get_random_bomb_data()
            bomb_location = (x,y)
            if bomb_location not in locations_in_use:
                self.__bomb = Bomb(x, y, radius, time)
                locations_in_use.append(bomb_location)
                self.__bomb_loc.append(bomb_location)

        # todo: remove this print
        print('done initializing board')

    def get_score(self):
        return self.__score

    def update_board(self, key):
        colors = ['red', 'green', 'black', 'orange']
        board_dict = {c: [] for c in colors}


        # move snake
        if self.__eating_counter == 0:
            self.__snake.simple_move(key)
            self.__snake_loc = self.__snake.get_all_coor()


        # todo: check if i have enough apples on the board and bombs. maybe in the beginning or in the end?

        # advance bomb or explosion
        elif len(self.__bomb_loc) >= 0 and len(self.__explosion_loc) > 0:
            if len(self.__bomb_loc) > 0:
                board_dict['red'] = self.__bomb_loc.pop()
            else:
                board_dict['orange'] = self.__explosion_loc.pop(0)


        # deal with bomb
        # eating apple
        #
        elif self.__eating_counter > 0:
        # todo: eating an apple
            self.__snake.forward_head_only(key)
            self.__eating_counter -= 1




    def is_valid_board(self) -> bool:
        # checks if the board is valid according to all of the edge cases
        """
        check if:
        1. snake didn't hit itself
        2. snake didn't hit the end of the board
        3. snake didn't touch bomb
        4. snake didn't touch explosion
        :return: bool
        """
        snake_loc = self.__board_dict['snake']
        explosion_loc = self.__board_dict['explosion']
        bombs_loc = self.__board_dict['bombs']
        for loc in snake_loc:
            # check if the snake is inside the board
            if loc not in self.__locations:
                return False
            # check if the snake touched an explosion
            elif len(set(snake_loc).intersection(
                    set(explosion_loc))) == 0 and len(explosion_loc) != 0:
                return False
            # check if the snake touched a bomb
            elif len(set(snake_loc).intersection(set(bombs_loc))) == 0 and len(
                    explosion_loc) != 0:
                return False
            # check if the snake touched itself
            elif len(set(snake_loc)) != len(snake_loc):
                return False
        return True

    def get_board(self):
        board_dict = {}
        board_dict['red'] = self.__bomb_loc
        board_dict['orange'] = self.__bomb_loc
        board_dict['black'] = self.__snake_loc
        board_dict['green'] = self.__apples_loc
        return board_dict
