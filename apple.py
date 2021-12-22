from typing import Tuple

import game_parameters


class Apple:
    def __init__(self):
        x, y, score = game_parameters.get_random_apple_data()
        self.__x = x
        self.__y = y
        self.__score = score

    def get_apple_score(self) -> int:
        """
        get the score of the apple
        """
        return self.__score

    def get_location(self) -> Tuple[int,int]:
        """
        get the location of the apple
        """
        return self.__x, self.__y

    def get_score_by_loc(self, loc: Tuple[int,int]) -> int:
        """
        get the score of the apple by its location
        """
        x, y = loc
        if x == self.__x and y == self.__y:
            return self.__score
        return 0

    def move_apple(self) -> None:
        """
        move the apple location
        """
        x, y, score = game_parameters.get_random_apple_data()
        self.__x = x
        self.__y = y
