#################################################################
# FILE : snake_main.py
# WRITER : Anina Dotan  208929232, Zuk Arbell 205937139
# EXERCISE : intro2cs2 ex10 2020
# DESCRIPTION: Snake game
# STUDENTS I DISCUSSED THE EXERCISE WITH: None.
# WEB PAGES I USED:
# https://medium.com/@kevin.michael.horan/data-structures-linked-lists-with-python-2d0ec4fdc18c
#################################################################


import game_parameters
from board import Board
from game_display import GameDisplay


def get_key(new_key: str, old_key: str) -> str:
    """
    prevents the snake from going backwards "into his body"
    :param new_key: the new key that's been clicked - string of
                    the new direction or None if nothing was clicked
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
    """
    the main function that drives the game - creates a board, initializing it
    and moving the snake until the games is finished due to being disqualified
    or that there is no more room for new apple
    :param gd: uses given function to get the players input
    :return: doesn't return anything - prints the board
                                       on GUI throughout the game
    """
    # start score 0
    gd.show_score(0)
    # start direction is up
    key_before: str = "Up"
    # create board and initialise it
    game_board = Board(game_parameters.HEIGHT, game_parameters.WIDTH)
    game_board.initialize_board()
    # the flag for ending the game
    continue_game: bool = True
    # printing the first board as it started
    dict_of_colors: dict = game_board.get_board()
    # unpack the colors
    for color in dict_of_colors:
        list_cells = dict_of_colors[color]

        if list_cells:
            for location_tuple in list_cells:
                x, y = location_tuple
                gd.draw_cell(x, y, color)
    # declare end round for initialize
    gd.end_round()

    # starts the main loop of the game
    while continue_game:
        # get the new move input
        key_clicked = gd.get_key_clicked()
        cur_key = get_key(key_clicked, key_before)
        # update the board
        game_board.update_board(cur_key)
        # check if the games should continue
        continue_game = game_board.is_valid_board()
        # get the new score
        new_score = game_board.get_score()
        # updates the score display
        gd.show_score(new_score)

        # start by printing the screen of the current round
        dict_of_colors = game_board.get_board()
        # unpack the colors
        for color in dict_of_colors:
            list_cells: list = dict_of_colors[color]
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
