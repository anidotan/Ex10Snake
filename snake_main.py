import game_parameters
from game_display import GameDisplay
from board import Board


def get_key(new_key, old_key):
    """
    prevents the snake from going backwards "into his body"
    :param new_key: the new key that's been clicked
    :param old_key: the key before
    :return: the new relevant key
    """
    if new_key is None:
        key_now = old_key
    elif old_key == "Up" and new_key == "Down":
        key_now = old_key
    elif old_key == "Down" and new_key == "Up":
        key_now = old_key
    elif old_key == "Left" and new_key == "Right":
        key_now = old_key
    elif old_key == "Right" and new_key == "Left":
        key_now = old_key
    else:
        key_now = new_key

    return key_now


def old_main_loop(gd: GameDisplay) -> None:
    gd.show_score(0)
    x, y = 10, 10
    key_before = "Up"
    while True:
        key_clicked = gd.get_key_clicked()
        if key_clicked is None:
            key_now = key_before
        else:
            key_now = key_clicked

        if (key_now == 'Left') and (x > 0):
            x -= 1
        elif (key_now == 'Right') and (x < game_parameters.WIDTH):
            x += 1
        elif (key_now == 'Up') and (y < game_parameters.HEIGHT):
            y += 1
        elif (key_now == 'Down') and (x < game_parameters.HEIGHT):
            y -= 1
        gd.draw_cell(x, y, "red")
        gd.show_score(10)
        key_before = key_now

        gd.end_round()


def main_loop(gd: GameDisplay) -> None:
    # start score 0
    gd.show_score(0)
    # start direction is up
    key_before = "Up"
    # create board and initialise it
    game_board = Board(game_parameters.HEIGHT, game_parameters.WIDTH)
    game_board.initialize_board()
    # the flag for ending the game
    continue_game = True

    while continue_game:
        # start by printing the screen
        color_of_end_game = game_board.get_board()
        # dict_of_colors = {'green': [(37, 19), (20, 6), (15, 29)], 'black': [(19, 12), (18, 12), (17, 12), (16, 12), (15, 12), (14, 12), (13, 12), (12, 12), (11, 12), (10, 12), (10, 11), (10, 10), (10, 9), (9, 9), (8, 9), (7, 9), (6, 9), (5, 9)], 'red': [], 'orange': [(16, 7), (15, 8), (17, 10), (20, 7), (19, 10), (16, 9), (19, 6), (17, 6), (20, 9), (21, 8), (18, 5), (18, 11)]}
        # example of bad frame - explosion not on top od snake
        print(color_of_end_game)

        # unpack the colors
        for color in color_of_end_game:
            list_cells = color_of_end_game[color]

            if list_cells:
                for location_tuple in list_cells:
                    x, y = location_tuple
                    gd.draw_cell(x, y, color)

        key_clicked = gd.get_key_clicked()
        cur_key = get_key(key_clicked, key_before)
        game_board.update_board(cur_key)  # remove

        new_score = game_board.get_score()  # get the new score
        gd.show_score(new_score)  # updates the score display

        # dict_of_colors = game_board.get_board()  # todo might change
        # # unpack the colors
        # for color in dict_of_colors:
        #     list_cells = dict_of_colors[color]
        #     # print("4", list_cells) remove
        #     if list_cells:
        #         for location_tuple in list_cells:
        #             x, y = location_tuple
        #             gd.draw_cell(x, y, color)





        # check if the game have been finished
        continue_game = game_board.is_valid_board()  # todo
        if not continue_game:
            color_of_end_game = game_board.get_board()
            for color in color_of_end_game:
                list_cells = color_of_end_game[color]

                if list_cells:
                    for location_tuple in list_cells:
                        x, y = location_tuple
                        if y < 0 or x < 0 or y > game_parameters.HEIGHT - 1 or x > game_parameters.WIDTH - 1:  # todo make better - used to not raise erroe if snake out of board
                            continue
                        else:
                            gd.draw_cell(x, y, color)

        # updating the key so it we'll have a default moving direction
        key_before = cur_key
        gd.end_round()


