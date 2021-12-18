import game_parameters
import snake
from apple import Apple
from bomb import Bomb

from typing import Tuple


class Board:
    def __init__(self, height: int, width: int):
        self.__height = height
        self.__width = width
        # self.__locations = [(x, y) for x in range(self.__width) for y in
        #                     range(self.__height)]
        self.__score = 0
        self.__snake = None
        self.__snake_loc = []
        self.__apples = set()
        # self.__apples_loc = []
        self.__bomb = None
        self.__bomb_loc = []
        self.__explosion_loc = []
        self.__eating_counter = 0

    def create_new_bomb(self):
        pass


    def get_all_apple_locations(self):
        return [apple.get_location() for apple in self.__apples]


    def initialize_board(self):
        """
        create first board-frame
        1. place the snake
        2. place the bombs
        3. place the apples
        :return: board
        """
        self.__snake = snake.Snake()
        locations_in_use = self.__snake.get_all_coor()

        # add 3 apples to the board
        while len(self.__apples) < 3:
            apple = Apple()
            apple_location = apple.get_location()
            if apple_location not in locations_in_use:
                self.__apples.add(apple)
                locations_in_use.append(apple_location)
                # self.__apples_loc.append(apple_location)

        # todo: check if its okay i did bomb loc and not the bomb)
        # add 1 bomb to the board
        while len(self.__bomb_loc) < 1:
            self.__bomb = Bomb()
            bomb_location = self.__bomb.get_location
            if bomb_location not in locations_in_use:
                locations_in_use.append(bomb_location)
                self.__bomb_loc = self.__bomb.waiting_frames()
                self.__explosion_loc = self.__bomb.explosion_frames()

        # todo: remove this print
        print('done initializing board')

    def get_score(self):
        return self.__score

    def update_board(self, key):
        # todo: check if i have enough apples on the board and bombs. maybe in the beginning or in the end?
        colors = ['green', 'black', 'red', 'orange']
        board_dict = {c: [] for c in colors}

        # move snake
        if self.__eating_counter == 0:
            self.__snake.simple_move(key)
            # todo: do i want snake_loc?
            self.__snake_loc = self.__snake.get_all_coor()

        # move snake while eating apple
        if self.__eating_counter > 0:
            self.__snake.forward_head_only(key)
            self.__eating_counter -= 1

        # advance bomb or explosion
        # todo: improve this if
        if len(self.__bomb_loc) >= 0 and len(self.__explosion_loc) > 0:
            if len(self.__bomb_loc) > 0:
                board_dict['red'] = self.__bomb_loc.pop()
            else:
                explosion_loc = self.__explosion_loc.pop(0)
                for apple in self.__apples:
                    if apple.get_location() in explosion_loc:
                        apple.move_apple()
                board_dict['orange'] = self.__explosion_loc.pop(0)

        if len(self.__bomb_loc) == 0 and len(self.__explosion_loc) == 0:
            new_bomb = Bomb()
            new_location = new_bomb.get_location()

            if new_location not in board_dict['black'] \
                    and new_location not in self.get_all_apple_locations():
                self.__bomb = new_bomb
                self.__bomb_loc = self.__bomb.waiting_frames()
                self.__explosion_loc = self.__bomb.explosion_frames()

        # todo: improve big O

        # eating apple
        apple_to_remove = None
        snake_head = self.__snake.get_head()
        for apple in self.__apples:
            if apple.get_location() == snake_head:
                self.__eating_counter += 3
                apple_to_remove = apple
                self.__score += apple.get_apple_score()
        if apple_to_remove is not None:
            self.__apples.remove(apple_to_remove)
            apple_placed = False
            while not apple_placed:
                new_apple = Apple()
                new_location = new_apple.get_location()
                if new_location not in board_dict['black'] \
                    and new_location not in self.get_all_apple_locations() \
                    and new_location not in board_dict['orange'] \
                    and new_location not in board_dict['red']:
                        self.__apples.add(new_apple)


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
        # board_dict['green'] = self.__apples_loc
        return board_dict
