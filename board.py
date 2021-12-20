import game_parameters
from apple import Apple
from bomb import Bomb
from snake import Snake
from typing import Tuple


class Board:
    def __init__(self, height: int, width: int):
        self.__height = height
        self.__width = width
        self.__count_round = 0
        self.__score = 0
        self.__snake = None
        self.__bomb_instance = None
        self.__all_static_bomb_loc = []
        self.__all_explosion_loc = []
        self.__eating_counter = 0
        self.__locations = [(x, y) for x in range(self.__width) for y in
                            range(self.__height)]
        self.__apple_instances_set = set()
        colors = ['black', 'red', 'green', 'orange']
        self.__board_dict = {c: [] for c in colors}
        self.__continue_game = True

    def initialize_board(self):
        """
        create first board-frame
        1. place the snake
        2. place the bombs
        3. place the apples
        :return: board
        """
        self.__snake = Snake()
        self.__board_dict['black'] = self.__snake.get_all_coor()

        # add 1 bomb to the board
        while len(self.__board_dict['red']) < 1:
            self.__bomb_instance = Bomb()
            bomb_location = self.__bomb_instance.get_location()
            if self.can_place_obj(bomb_location):
                self.__board_dict['red'] = [bomb_location]
                self.__all_static_bomb_loc = self.__bomb_instance.waiting_frames()
                self.__all_explosion_loc = self.__bomb_instance.explosion_frames()

        print(
            f'added a new bomb! expolsion time is: {self.__bomb_instance.get_exploiding_time()}')

        # add 3 apples to the board
        while len(self.__apple_instances_set) < 3:
            apple = Apple()
            apple_location = apple.get_location()
            if apple_location not in self.__board_dict.values():
                self.__apple_instances_set.add(apple)
                green_apples = self.__board_dict['green']
                green_apples.append(apple_location)

    def get_score(self):
        return self.__score

    def get_all_apple_locations(self):
        return [apple.get_location() for apple in self.__apple_instances_set]

    def can_place_obj(self, loc: Tuple[int, int]) -> bool:
        return loc not in self.__board_dict['red'] and loc not in \
               self.__board_dict['black'] and loc not in self.__board_dict[
                   'green'] and loc not in self.__board_dict['orange']

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
        if len(self.__all_static_bomb_loc) > 0:
            current_loc = self.__all_static_bomb_loc.pop()
            self.__count_round += 1
            self.__board_dict['red'] = [current_loc]
        elif len(self.__all_explosion_loc) > 0:
            explosion_loc = self.__all_explosion_loc.pop(0)
            for apple in self.__apple_instances_set:
                if apple.get_location() in explosion_loc:
                    apple_placed = False
                    while not apple_placed:
                        apple.move_apple()
                        new_locaion = apple.get_location()
                        if self.can_place_obj(new_locaion):
                            apple_placed = True
                    # todo: move apple until it has a valid place
            self.__board_dict['orange'] = explosion_loc
            self.__board_dict['red'] = []
        else:  # add new bomb
            print(f'time till bomb exploaded is: {self.__count_round}')
            self.__count_round = 0
            new_bomb = Bomb()
            new_location = new_bomb.get_location()
            if new_location not in self.__board_dict['black'] \
                    and new_location not in self.__board_dict['green']:
                self.__bomb_instance = new_bomb
                print(f'added a new bomb! expolsion time is: {self.__bomb_instance.get_exploiding_time()}')
                self.__all_static_bomb_loc = self.__bomb_instance.waiting_frames()
                self.__all_explosion_loc = self.__bomb_instance.explosion_frames()
                self.__board_dict['orange'] = []
                self.__board_dict['red'] = [self.__all_static_bomb_loc[0]]

        # eating an apple
        apple_to_remove = None
        snake_head = self.__snake.get_head()
        for apple in self.__apple_instances_set:
            if apple.get_location() == snake_head:
                self.__eating_counter += 3
                apple_to_remove = apple
                self.__score += apple.get_apple_score()

        # new apple in case we ate one
        if apple_to_remove is not None:
            self.__apple_instances_set.remove(apple_to_remove)  # removing the old

            # find new apple to add
            apple_placed = False
            while not apple_placed:
                new_apple = Apple()
                new_location = new_apple.get_location()
                # todo - make sure correct
                num_cells_in_use = len(self.__board_dict['red']) + len(self.__board_dict['black']) + len(self.__board_dict['orange']) + len(self.__board_dict['green'])
                if num_cells_in_use == game_parameters.WIDTH * game_parameters.HEIGHT:
                    self.__continue_game = False
                    break
                elif self.can_place_obj(new_location):
                    self.__apple_instances_set.add(new_apple)
                    apple_placed = True

        self.__board_dict['green'] = self.get_all_apple_locations()
        self.__board_dict['black'] = self.__snake.get_all_coor()

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
        current_explosion_loc = self.__all_explosion_loc  # remove not in use
        current_bomb_loc = self.__all_static_bomb_loc  # remove not in use
        list_red = self.__board_dict['red']
        list_orange = self.__board_dict['orange']

        # check if the snake is inside the board
        head_of_snake = self.__snake.get_head()
        cur_x, cur_y = head_of_snake
        if cur_y < 0 or cur_x < 0 or cur_y > self.__height - 1 or cur_x > self.__width - 1:
            self.__continue_game = False

        # check if the snake touched a bomb
        elif list_red and head_of_snake == list_red[0]:
            self.__continue_game = False

        # check if the snake touched an explosion
        elif list_orange and len(
                set(snake_loc).intersection(set(list_orange))) > 0:
            self.__continue_game = False

        # check if the snake touched itself
        elif len(set(snake_loc)) != len(snake_loc):
            self.__continue_game = False

        return self.__continue_game

    def get_board(self):
        list_orange_frames = self.__board_dict['orange']
        all_snake_coor = self.__board_dict['black']

        coor_to_remove = None
        for black_coor in all_snake_coor:
            if black_coor in list_orange_frames:
                coor_to_remove = black_coor

        if coor_to_remove is not None:
            all_snake_coor.remove(coor_to_remove)

        return self.__board_dict
