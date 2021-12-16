import game_parameters


class Bomb:
    """

    """
    def __init__(self, x: int, y: int, radius: int, time: int):
        self.__x = x
        self.__y = y
        self.__radius = radius
        self.__time = time

    def explosiom(self, time):
        """

        :return: according to the time given, explode the bomb ad send the
        relevant blast signals
        """