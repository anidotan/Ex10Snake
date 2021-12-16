import pytest
import board


@pytest.mark.parametrize("width,height,snake_loc,apples,bombs,explosion,expected_out",
                         [
                             (40,30,[(10,10), (10,9), (10,8)],[(1,1),(2,2)],[(11,20)], [] ,True),
                             (40,30,[(-1,10), (0,10), (1,10)],[(1,1),(2,2)],[(11,20)],[], False),
                             (40,30,[(0,10), (1,10)],[(1,1),(2,2)],[(11,20)], [0,10], False),
                             (40,30,[(0,10), (1,10)],[(1,1),(2,2)],[(11,20)], [1,10], False),
                             (40,30,[(0,10), (1,10), (2,10), (3,10),(3,11),(3,12), (2,12), (1,12), (1,11)],[(1,1),(2,2)],[],[],False)
                         ])
def test_is_valid_board(width,height,snake_loc,apples,bombs,explosion,expected_out):
    b = board.Board(width, height, snake_loc, apples, bombs)
    b.set_explosions(explosion)
    assert b.is_valid_board() == expected_out
