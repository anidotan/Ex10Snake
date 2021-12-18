from board import Board
import game_parameters
from typing import Dict, List, Tuple


class Game:
    def __init__(self):
        self.__score = 0
        self.__game_ended = False
        self.__current_board = None
        self.__height = game_parameters.HEIGHT
        self.__width = game_parameters.WIDTH

    def inilialize_board(self):
        """
        create first board-frame
        1. place the snake
        2. place the bombs
        3. place the apples
        :return: board
        """
        apples = []
        bombs = []
        snake = [(10,10), (10,9), (10,8)]
        locations_in_use = snake[:]
        # add 3 apples to the board
        while len(apples) < 3:
            apple_location = game_parameters.get_random_apple_data()
            if apple_location not in locations_in_use:
                apples.append(apple_location)
                # todo: do i want to do it like this?
                # locations_in_use.append(apple_location)
        locations_in_use.extend(apples)

        # add 1 bomb to the board
        while len(bombs) < 1:
            bomb_location = game_parameters.get_random_bomb_data()
            if bomb_location not in locations_in_use:
                apples.append(bomb_location)
                locations_in_use.append(bomb_location)

        board = Board(game_parameters.HEIGHT,game_parameters.WIDTH, snake, apples, bombs)
        self.__current_board = board

    def __eat_apple(self, new_board, actions):
        """
        update new board
        :param new_board:
        :param actions:
        :return:
        """
        # todo: advance_snake, update score
        actions['add_new_apple'] = True
        actions['eating_apple'] = True
        return actions


    def __bomb_exploaded(self, new_board, actions):
        actions['bomb_exploaded'] = True
        # todo: erase any bombs in your way, advance bomb (remove instance from list)


    def __advance_snake(self):
        pass

    def __single_round(self, key_input: str, actions: Dict[str, bool]):
        """
        1. get input
        2. move snake
        4. check if there is a bomb explosion -> erase apples in the area
        3. check if game ended

        4. check if snake ate apple -> progress + update score
        5. update apples + bombs for the next round
        6. draw board
        7. end round

        Dict:
        {'bomb_exploded': bool,
        'eating_apple' \ 'grow_snake': bool,
        'add_new_apple': bool,
        'add_new_bomb': bool

        :return:
        """
        self.__advance_snake()
        # List[Tuple[int,int]], List[List[Tuple[int,int]]]
        new_board = self.__current_board.get_board().copy()
        if actions['bomb_exploaded']:
            new_board['bombs'] = self.__bomb_exploaded()

        if actions['eating_apple']:
            new_board['apples'] = self.__eat_apple()

        if actions['add_new_apple']:
            pass

    def update_score(self):
        pass

    def get_current_board(self):
        return self.__current_board
