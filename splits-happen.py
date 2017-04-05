# Design and Development Challenge - Bowling Score
# Author: Chad Price (chadsprice@gmail.com)

# characters used to represent special rolls
STRIKE = 'X'
SPARE = '/'
MISS = '-'

# Takes a string representing a bowling line (e.g. 'X7/9-X-88/-6XXX81') and
# returns the score for that game (e.g. 167).
# Each character represents a roll.
# The given line must be valid, containing a correct number of rolls and frames.
def bowlingScore(line):
    # a list of the number of pins knocked down in each roll
    rolls = []
    # parse each roll into the number of pins knocked down
    for roll in line:
        if roll == STRIKE:
            # a stike knocks down all 10 pins
            rolls.append(10)
        elif roll == MISS:
            # a miss knocks down 0 pins
            rolls.append(0)
        elif roll == SPARE:
            # a spare knocks down the remaining pins (10 - the last roll)
            rolls.append(10 - rolls[-1])
        else:
            # the number of pins is a digit 1-9
            rolls.append(int(roll))
    # a list of the scores for each frame
    frames = []
    # the index keeping track of the first roll of the current frame
    rollIndex = 0
    # for each of the 10 frames
    for frameIndex in range(10):
        if line[rollIndex] == STRIKE:
            # a strike is 10 plus the number of pins knocked down in the next
            # two rolls
            frames.append(10 + rolls[rollIndex+1] + rolls[rollIndex+2])
            # this frame has only one roll
            rollIndex += 1
        elif line[rollIndex+1] == SPARE:
            # a spare is 10 plus the number of pins knocked down in the next
            # roll (in the next frame)
            frames.append(10 + rolls[rollIndex+2])
            # this frame has two rolls
            rollIndex += 2
        else:
            # otherwise, the score is the total number of pins knocked down in
            # the two tries
            frames.append(rolls[rollIndex] + rolls[rollIndex+1])
            # this frame has two rolls
            rollIndex += 2
    # return the total score of all 10 frames
    return sum(frames)

if __name__ == "__main__":
    # validation test cases
    testLines = [("XXXXXXXXXXXX", 300), ("9-9-9-9-9-9-9-9-9-9-", 90), ("5/5/5/5/5/5/5/5/5/5/5", 150), ("X7/9-X-88/-6XXX81", 167)]
    # run the test cases
    for testLine in testLines:
        line = testLine[0]
        expected = testLine[1]
        actual = bowlingScore(testLine[0])
        # print any test case that fails
        if actual != expected:
            print "Failed test case (" + line + "): expected=" + str(expected) + " actual=" + str(actual)
