class Game:
    
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)
    
    def score(self):
        result = 0
        rollIdx = 0
        for frameIndex in range(10):
            if self.isStrike(rollIdx):
                result += self.strikeScore(rollIdx)
                rollIdx += 1
            elif self.isSpare(rollIdx):
                result += self.spareScore(rollIdx)
                rollIdx += 2
            else:
                result += self.frameScore(rollIdx)
                rollIdx += 2
        return result

    def isStrike(self, rollIdx):
        return self.rolls[rollIdx] == 10

    def isSpare(self, rollIdx):
        return self.rolls[rollIdx] + self.rolls[rollIdx + 1] == 10

    def strikeScore(self, rollIdx):
        return 10 + self.rolls[rollIdx + 1] + self.rolls[rollIdx + 2]
        
    def spareScore(self, rollIdx):
        return 10 + self.rolls[rollIdx + 2]

    def frameScore(self, rollIdx):
        return self.rolls[rollIdx] + self.rolls[rollIdx + 1] 