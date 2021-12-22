import game_parameters
from game_display import GameDisplay
from board import Board

# todo: add typing


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
    # printing the first board as it started
    dict_of_colors = game_board.get_board()
    # unpack the colors
    for color in dict_of_colors:
        list_cells = dict_of_colors[color]

        if list_cells:
            for location_tuple in list_cells:
                x, y = location_tuple
                gd.draw_cell(x, y, color)

    gd.end_round()

    while continue_game:
        # get the new move input
        key_clicked = gd.get_key_clicked()
        cur_key = get_key(key_clicked, key_before)
        # update the board
        game_board.update_board(cur_key)

        continue_game = game_board.is_valid_board()

        new_score = game_board.get_score()  # get the new score
        gd.show_score(new_score)  # updates the score display

        # start by printing the screen
        dict_of_colors = game_board.get_board()

        # unpack the colors
        for color in dict_of_colors:
            list_cells = dict_of_colors[color]

            if list_cells:
                for location_tuple in list_cells:
                    x, y = location_tuple
                    if y < 0 or x < 0 or y > game_parameters.HEIGHT - 1 or \
                            x > game_parameters.WIDTH - 1:
                        continue
                    else:
                        gd.draw_cell(x, y, color)

        # updating the key so it we'll have a default moving direction
        key_before = cur_key
        gd.end_round()
