from bowling_game import Game


class TestGame:

    g = Game()

    def rollMany(self, pins, rolls):
        for i in range(rolls):
            self.g.roll(pins)

    def test_gutter_game(self):
        self.rollMany(0, 20)
        assert self.g.score() == 0
    
    def test_all_ones(self):
        self.rollMany(1, 20)
        assert self.g.score() == 20

    def test_one_spare(self):
        self.g.roll(5)
        self.g.roll(5)
        self.g.roll(3)
        self.rollMany(1, 17)
        assert self.g.score() == 33

    def test_one_strike(self):
        self.g.roll(10)
        self.g.roll(4)
        self.g.roll(3)
        self.rollMany(1, 16)
        assert self.g.score() == 40

    def test_perfect_game(self):
        self.rollMany(10, 12)
        assert self.g.score() == 300

    def test_all_spares(self):
        self.rollMany(5, 21)
        assert self.g.score() == 150