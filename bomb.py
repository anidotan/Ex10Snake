import game_parameters


class Bomb:
    """

    """
    def __init__(self, x: int, y: int, radius: int, time: int):
        self.__x = x
        self.__y = y
        self.__radius = radius
        self.__time = time

    def explosion(self):
        """

        :return: list of lists with the differnet cells for the blast in each frame
        """
        list = []
        up = self.__y + self.__radius - 1
        down = self.__y - self.__radius + 1
        right = self.__x + self.__radius - 1
        left = self.__x - self.__radius + 1

        for i in range(left, right + 1):

            for j in range (down, up + 1):
                frame_tuple = tuple((i, j))
                list.append(frame_tuple)


        print(list)
        print(max(list))

        # for u in range(-1 * self.__x, self.__x + 1):
        #
        #     for v in range(-1 * self.__y, self.__y + 1):
        #         if (abs(self.__x - u)) + (abs(self.__y - v)) == self.__radius - 1:
        #             cur_tuple = tuple((v, u))
        #             list.append(cur_tuple)
        #
        # print(list)

if __name__ == '__main__':
    bomb1 = Bomb(10, 10, 3, 3)
    bomb1.explosion()