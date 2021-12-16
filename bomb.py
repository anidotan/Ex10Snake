import game_parameters


class Bomb:
    """

    """
    def __init__(self, x: int, y: int, radius: int, time: int):
        self.__x = x
        self.__y = y
        self.__radius = radius
        self.__time = time

    def explosion(self, time):
        """

        :return: list of lists with the differnet cells for the blast in each frame
        """

        hello world