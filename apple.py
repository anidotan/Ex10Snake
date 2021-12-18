class Apple:
    def __init__(self, x, y, score):
        # todo: maybe change this to a tuple?
        self.__x = x
        self.__y = y
        self.__score = score

    def get_apple_score(self):
        return self.__score

    def get_location(self):
        return self.__x, self.__y