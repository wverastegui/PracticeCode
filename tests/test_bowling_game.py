from src.bowling_game import roll, score

nroll = roll
def rollMany(pins, rolls):
    for i in range(rolls):
        nroll(pins)


def test_gutter_game():
    rollMany(0, 20)
    assert score() == 0

    
def test_all_ones():
    rollMany(1, 20)
    assert score() == 20


def test_one_spare():
    roll(5)
    roll(5)
    roll(3)
    rollMany(0, 17)
    assert score() == 16


def test_one_strike():
    roll(10)
    roll(4)
    roll(3)
    rollMany(0, 16)
    assert score() == 24


def test_perfect_game():
    rollMany(10, 12)
    assert score() == 300


def test_all_spares():
    rollMany(5, 21)
    assert score() == 150