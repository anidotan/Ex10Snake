import game_parameters
from game_parameters import get_random_bomb_data, WIDTH, HEIGHT


class Bomb:
    """
    creates a bomb instance for the game of snake

    attributes:
    x - the location of the bomb on the x axis
    y - the location of the bomb on the y axis
    radius - the radius of the bomb explosion
    time - the number of game round until the bomb starts to explode

    methods:
    explosion frames - a list of sets. each set has in it all the frames of a
                        single shock wave of a bomb.
                        the first set is the beginning of the explosion and
                        each following set is a single spreading shock wave
    waiting frames - a list with repeating tuple of the bomb location (x, y)
                    the length of the list and number of repetition is the same
                    as the time (number of rounds) until the bomb
                    should explode
    get locations - returns the
    """
    def __init__(self):
        x, y, radius, time = get_random_bomb_data()
        self.__x = x
        self.__y = y
        self.__radius = radius
        self.__time = time

    def __str__(self):
        return f'{(self.__x, self.__y, self.__radius, self.__time)}'

    def explosion_frames(self):
        """
        :return: list of lists with the different cells for the blast in each frame
        """
        list_of_frames = []
        for r in range(self.__radius):

            set_of_tuples_in_single_frame = set()
            right_x = self.__x + r
            upper_y = self.__y + r
            left_x = self.__x - r

            bad_frame = False
            for i in range(r + 1):
                a = tuple((self.__x + i, upper_y - i))
                if self.__x + i < 0 or upper_y - i < 0 or\
                        self.__x + i > game_parameters.WIDTH - 1 or\
                        upper_y - i > game_parameters.HEIGHT - 1:
                    bad_frame = True
                    break
                set_of_tuples_in_single_frame.add(a)
                b = tuple((right_x - i, self.__y - i))
                if right_x - i < 0 or self.__y - i < 0 or\
                        right_x - i > game_parameters.WIDTH - 1 or\
                        self.__y - i > game_parameters.HEIGHT - 1:
                    bad_frame = True
                    break
                set_of_tuples_in_single_frame.add(b)
                c = tuple((self.__x - i, upper_y - i))
                if self.__x - i < 0 or upper_y - i < 0 or\
                        self.__x - i > game_parameters.WIDTH - 1 or\
                        upper_y - i > game_parameters.HEIGHT - 1:
                    bad_frame = True
                    break
                set_of_tuples_in_single_frame.add(c)
                d = tuple((left_x + i, self.__y - i))
                if left_x + i < 0 or self.__y - i < 0 or\
                        left_x + i > game_parameters.WIDTH - 1 or\
                        self.__y - i > game_parameters.HEIGHT - 1:
                    bad_frame = True
                    break
                set_of_tuples_in_single_frame.add(d)

            list_of_frames.append(list(set_of_tuples_in_single_frame))
            if bad_frame:
                list_of_frames.pop()
                break

        return list_of_frames

    def waiting_frames(self) -> list[tuple]:
        """
        :return: list of the bomb location as tuple. number of repetitions
                is in accordance to the number of rounds until the bomb explodes
        """
        list_all_frames = []
        bomb_tuple = tuple((self.__x, self.__y))
        for i in range(self.__time):
            list_all_frames.append(bomb_tuple)

        return list_all_frames

    def get_location(self):
        """
        :return: the location of the bomb as a tuple[x: int, y: int]
        """
        return tuple((self.__x, self.__y))
