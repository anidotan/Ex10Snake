from typing import List, Tuple


class Board:
    def __init__(self, height: int, width: int,
                 snake_loc: List[Tuple[int, int]],
                 apples: List[Tuple[int, int]],
                 bombs: List[Tuple[int, int]]):
        self.__height = height
        self.__width = width
        self.__locations = [(x, y) for x in range(self.__width) for y in
                            range(self.__height)]
        self.__board = {'snake': snake_loc, 'apples': apples, 'bombs': bombs,
                        'explosion': []}

    # todo: do i need this?
    def __create_location_list(self) -> None:
        """
        creates all possible location on the board as a list of tupples.
        :return:
        """
        self.__locations = [(x, y) for x in range(self.__width) for y in
                            range(self.__height)]

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
        snake_loc = self.__board['snake']
        explosion_loc = self.__board['explosion']
        bombs_loc = self.__board['bombs']
        for loc in snake_loc:
            # check if the snake is inside the board
            if loc not in self.__locations:
                return False
            # check if the snake touched an explosion
            elif set(snake_loc).intersection(set(explosion_loc)) == 0:
                return False
            # check if the snake touched a bomb
            elif set(snake_loc).intersection(set(bombs_loc)) == 0:
                return False
            # check id the snake touched itself
            elif len(set(snake_loc)) != len(snake_loc):
                return False
        return True

