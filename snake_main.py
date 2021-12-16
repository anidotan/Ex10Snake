import game_parameters
from game_display import GameDisplay

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
        gd.draw_cell(x, y, "red")
        key_before = key_now

        gd.end_round()