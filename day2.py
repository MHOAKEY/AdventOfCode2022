# ("A", "X") Rock  defeats ("C", "Z") Scissors, Scissors defeats ("B", "Y") Paper, and Paper defeats Rock.

# The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

rockValue = 1
# rock = "A" or "X"
rock = "A X"
rockPaper = "A Y"
rockScissor = "A Z"

paperValue = 2
# paper = "B" or "Y"
paperRock = "B X"
paper = "B Y"
paperScissor = "B Z"

scissorsValue = 3
# scissors = "C" or "Z"
scissorRock = "C X"
scissorPaper = "C Y"
scissor = "C Z"

lose = 0
draw = 3
win = 6


matches = []
scoreABC = []
scoreABCTotal = 0
scoreXYZ = []
scoreXYZTotal = 0

scoreABC2 = []
scoreABC2Total = 0
scoreXYZ2 = []
scoreXYZ2Total = 0


with open('RPS.txt') as f:
    for eachLine in f:
        matches.append(eachLine.strip())


for i in matches:
    if i == rock:
        scoreABC.append(str(rockValue + draw))
        scoreXYZ.append(str(rockValue + draw))
    if i == rockPaper:
        scoreABC.append(str(rockValue + lose))
        scoreXYZ.append(str(paperValue + win))
    if i == rockScissor:
        scoreABC.append(str(rockValue + win))
        scoreXYZ.append(str(scissorsValue + lose))
    if i == paperRock:
        scoreABC.append(str(paperValue + win))
        scoreXYZ.append(str(rockValue + lose))
    if i == paper:
        scoreABC.append(str(paperValue + draw))
        scoreXYZ.append(str(paperValue + draw))
    if i == paperScissor:
        scoreABC.append(str(paperValue + lose))
        scoreXYZ.append(str(scissorsValue + win))
    if i == scissorRock:
        scoreABC.append(str(scissorsValue + lose))
        scoreXYZ.append(str(rockValue + win))
    if i == scissorPaper:
        scoreABC.append(str(scissorsValue + win))
        scoreXYZ.append(str(paperValue + lose))
    if i == scissor:
        scoreABC.append(str(scissorsValue + draw))
        scoreXYZ.append(str(scissorsValue + draw))
    else: 
        scoreABC.append("0")
        scoreXYZ.append("0")

for index in range(0, len(scoreABC)):
    scoreABC[index] = int(scoreABC[index])

for index in range(0, len(scoreXYZ)):
    scoreXYZ[index] = int(scoreXYZ[index])

for num in scoreABC:
    scoreABCTotal += num

for num in scoreXYZ:
    scoreXYZTotal += num

print(str(scoreABCTotal) + " " + str(scoreXYZTotal))


# X rock = lose
# Y paper = draw
# Z scissor = win

# rock > scissor
# paper > rock
# scissor > paper

for i in matches:
    if i == rock:
        scoreXYZ2.append(scissorsValue + lose)
    if i == rockPaper:
        scoreXYZ2.append(rockValue + draw)
    if i == rockScissor:
        scoreXYZ2.append(paperValue + win)
    if i == paperRock:
        scoreXYZ2.append(rockValue + lose)
    if i == paper:
        scoreXYZ2.append(paperValue + draw)
    if i == paperScissor:
        scoreXYZ2.append(scissorsValue + win)
    if i == scissorRock:
        scoreXYZ2.append(paperValue + lose)
    if i == scissorPaper:
        scoreXYZ2.append(scissorsValue + draw)
    if i == scissor:
        scoreXYZ2.append(rockValue + win)


for num in scoreXYZ2:
    scoreXYZ2Total += num

print(str(scoreXYZ2Total))
