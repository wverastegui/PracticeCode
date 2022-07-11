rolls = []


def roll(pins):
    return rolls.append(pins)
    

def score():
    result = 0
    rollIdx = 0
    for frameIndex in range(10):
        if is_Strike(rollIdx):
            result += strikeScore(rollIdx)
            rollIdx += 1
        elif is_Spare(rollIdx):
            result += spareScore(rollIdx)
            rollIdx += 2
        else:
            result += frameScore(rollIdx)
            rollIdx += 2
    return result


def is_Strike(rollIdx):
    return rolls[rollIdx] == 10


def is_Spare(rollIdx):
    return rolls[rollIdx] + rolls[rollIdx + 1] == 10


def strikeScore(rollIdx):
    return 10 + rolls[rollIdx + 1] + rolls[rollIdx + 2]
        

def spareScore(rollIdx):
    return 10 + rolls[rollIdx + 2]


def frameScore(rollIdx):
    return rolls[rollIdx] + rolls[rollIdx + 1] 