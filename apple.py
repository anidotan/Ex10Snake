from typing import Tuple
import game_parameters


class Apple:
    def __init__(self):
        x, y, score = game_parameters.get_random_apple_data()
        self.__x = x
        self.__y = y
        self.__score = score

    def __str__(self):
        return f'{self.__x}, {self.__y}, {self.__score}'

    def get_apple_score(self):
        return self.__score

    def get_location(self):
        return self.__x, self.__y

    def get_score_by_loc(self, loc: Tuple[int,int]):
        x, y = loc
        if x == self.__x and y == self.__y:
            return self.__score
        return 0

    def move_apple(self):
        x, y, score = game_parameters.get_random_apple_data()
        self.__x = x
        self.__y = y
