import game_parameters
from snake import Snake
from apple import Apple
from bomb import Bomb

from typing import Tuple


class Board:
    def __init__(self, height: int, width: int):
        self.__height = height
        self.__width = width
        self.__score = 0
        self.__snake = None
        self.__bomb_instance = None
        self.__all_static_bomb_loc = []
        self.__all_explosion_loc = []
        self.__eating_counter = 0
        self.__locations = [(x, y) for x in range(self.__width) for y in
                            range(self.__height)]
        self.__apple_instances_set = set()
        colors = ['green', 'black', 'red', 'orange']
        self.__board_dict = {c: [] for c in colors}



    # def __str__(self):
    #     return str(f'snake: {self.__snake} apples: {self.__apples}')

    def initialize_board(self):
        """
        create first board-frame
        1. place the snake
        2. place the bombs
        3. place the apples
        :return: board
        """
        self.__snake = Snake()
        locations_in_use = self.__snake.get_all_coor()

        # add 3 apples to the board
        while len(self.__apple_instances_set) < 3:
            apple = Apple()
            apple_location = apple.get_location()
            if apple_location not in locations_in_use:
                self.__apple_instances_set.add(apple)
                locations_in_use.append(apple_location)

        # add 1 bomb to the board
        while len(self.__all_static_bomb_loc) < 1:
            self.__bomb_instance = Bomb()
            bomb_location = self.__bomb_instance.get_location()
            if bomb_location not in locations_in_use:
                locations_in_use.append(bomb_location)
                self.__all_static_bomb_loc = self.__bomb_instance.waiting_frames()
                self.__all_explosion_loc = self.__bomb_instance.explosion_frames()

        # todo: remove this print
        print('done initializing board')


    def get_score(self):
        return self.__score


    def get_all_apple_locations(self):
        return [apple.get_location() for apple in self.__apple_instances_set]

    def update_board(self, key):
        # move snake - no apple
        if self.__eating_counter == 0:
            self.__snake.simple_move(key)
            self.__snake_loc = self.__snake.get_all_coor()

        # move snake while eating apple
        elif self.__eating_counter > 0:
            self.__snake.forward_head_only(key)
            self.__eating_counter -= 1

        # advance bomb or explosion
        # todo: improve this if
        if len(self.__all_static_bomb_loc) > 0:
            current_loc = self.__all_static_bomb_loc.pop()
            self.__board_dict['red'] = [current_loc]
        elif len(self.__all_explosion_loc) > 0:
            explosion_loc = list(self.__all_explosion_loc.pop(0))
            for apple in self.__apple_instances_set:
                if apple.get_location() in explosion_loc:
                    apple.move_apple()

            self.__board_dict['orange'] = explosion_loc

        else:  # add new bomb
            new_bomb = Bomb()
            new_location = new_bomb.get_location()
            if new_location not in self.__board_dict['black'] \
                and new_location not in self.get_all_apple_locations():
                self.__bomb_instance = new_bomb
                self.__all_static_bomb_loc = self.__bomb_instance.waiting_frames()
                self.__all_explosion_loc = self.__bomb_instance.explosion_frames()

        """
        if len(self.__all_static_bomb_loc) >= 0 and len(self.__all_explosion_loc) > 0:
            if len(self.__all_static_bomb_loc) > 0:
                current_loc = self.__all_static_bomb_loc.pop()
                self.__board_dict['red'] = [current_loc]
            else:
                explosion_loc = self.__all_explosion_loc.pop(0)
                for apple in self.__apples:
                    if apple.get_location() in explosion_loc:
                        apple.move_apple()
                        
                self.__board_dict['orange'] = explosion_loc
        
        # add new bomb
        elif len(self.__all_static_bomb_loc) == 0 and len(self.__all_explosion_loc) == 0:
            new_bomb = Bomb()
            new_location = new_bomb.get_location()
        """

        # eating apple
        apple_to_remove = None
        snake_head = self.__snake.get_head()
        for apple in self.__apple_instances_set:
            if apple.get_location() == snake_head:
                self.__eating_counter += 3
                apple_to_remove = apple
                self.__score += apple.get_apple_score()

        # todo: take this off?
        # new apple in case we ate one
        if apple_to_remove is not None:
            self.__apple_instances_set.remove(apple_to_remove) # removing the old

            # find new apple to add
            apple_placed = False
            while not apple_placed:
                new_apple = Apple()
                new_location = new_apple.get_location()
                if new_location not in self.__board_dict['black'] \
                        and new_location not in self.get_all_apple_locations() \
                        and new_location not in self.__board_dict['orange'] \
                        and new_location not in self.__board_dict['red']:
                    self.__apple_instances_set.add(new_apple)

        self.__board_dict['green'] = self.get_all_apple_locations()
        return self.__board_dict


    def is_valid_board(self) -> bool:
        """
        check if:
        1. snake didn't hit itself
        2. snake didn't hit the end of the board
        3. snake didn't touch bomb
        4. snake didn't touch explosion
        :return: bool
        """
        snake_loc = self.__snake.get_all_coor()
        current_explosion_loc = self.__all_explosion_loc
        current_bomb_loc = self.__all_static_bomb_loc
        list_red = self.__board_dict['red']
        list_orange = self.__board_dict['orange']

        # check if the snake is inside the board
        head_of_snake = self.__snake.get_head
        cur_x, cur_y = head_of_snake
        if cur_y < 0 or cur_x < 0 or cur_y > self.__height - 1 or cur_x > self.__width - 1:
            return False
        # check if the snake touched a bomb

        elif list_red and head_of_snake == list_red[0]:
            return False

        # check if the snake touched an explosion
        elif list_orange and head_of_snake in list_orange:
            return False

        # check if the snake touched itself
        elif len(set(snake_loc)) != len(snake_loc):
            return False
        return True

    def get_board(self):
        print("bomb", self.__all_static_bomb_loc)
        print("bomb", self.__bomb_instance)
        print("bomb", self.__all_static_bomb_loc)
        print("snake", self.__snake.get_all_coor())
        print("apples", self.get_all_apple_locations())
        print("ex", self.__all_explosion_loc)


        # self.__board_dict = {}
        self.__board_dict['black'] = self.__snake.get_all_coor()
        self.__board_dict['red'] = self.__all_static_bomb_loc
        self.__board_dict['orange'] = []
        self.__board_dict['green'] = self.get_all_apple_locations()

        return self.__board_dict


