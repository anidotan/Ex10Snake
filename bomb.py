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
    """
    def __init__(self, x: int, y: int, radius: int, time: int):
        self.__x = x
        self.__y = y
        self.__radius = radius
        self.__time = time

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
            for i in range(r + 1):
                a = tuple((self.__x + i, upper_y - i))
                set_of_tuples_in_single_frame.add(a)
                b = tuple((right_x - i , self.__y - i))
                set_of_tuples_in_single_frame.add(b)
                c = tuple((self.__x - i , upper_y - i))
                set_of_tuples_in_single_frame.add(c)
                d = tuple((left_x + i, self.__y - i))
                set_of_tuples_in_single_frame.add(d)

            list_of_frames.append(set_of_tuples_in_single_frame)

        return list_of_frames

    def waiting_frames(self):
        """
        :return: list of the bomb location as tuple. number of repetitions
                is in accordance to the number of rounds until the bomb explodes
        """
        list_all_frames = []
        bomb_tuple = tuple((self.__x, self.__y))
        for i in range(self.__time):
            list_all_frames.append(bomb_tuple)

        return list_all_frames
