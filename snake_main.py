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
    gd.show_score(0)
    key_before = "Up"
    game_board = Board(30, 40)
    continue_game = True
    while continue_game:
        key_clicked = gd.get_key_clicked()
        cur_key = get_key(key_clicked, key_before)
        game_board.update_board(cur_key)

        new_score = game_board.get_score()  # get the new score
        gd.show_score(new_score)  # updates the score display

        dict_of_colors = game_board.get_board()  # todo might change
        print(dict_of_colors)  # remove
        # unpack the colors
        for color in dict_of_colors:
            list_cells = dict_of_colors[color]
            if list_cells:
                for location_tuple in list_cells:
                    x, y = location_tuple
                    gd.draw_cell(x, y, color)

        # check if the game have been finished
        # continue_game = game_board.is_valid_board()  # todo

        # updates the key so the snake won't stop moving
        key_before = cur_key

        gd.end_round()