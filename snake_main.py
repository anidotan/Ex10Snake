import game_parameters
from game_display import GameDisplay
from game import Game

from typing import Dict, List, Tuple

OBJECT_COLORS = {'snake': 'Black', 'apples': 'green', 'bombs': 'red',
                'explosion': 'orange'}


def color_board(board: Dict[str, List[Tuple[int, int]]], gd: GameDisplay) -> None:
    for obj, locations in board.items():
        for loc in locations:
            x, y = loc
            # todo: do i want to change this? without globals or give a variable?
            gd.draw_cell(x, y, OBJECT_COLORS[obj])


def main_loop(gd: GameDisplay) -> None:
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
        gd.draw_cell(x, y, "black")
        key_before = key_now

        gd.end_round()
