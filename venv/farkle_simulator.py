import random
import time

# initialize counter variables
fhCnt = 0
straightCnt = 0
farkleCnt = 0
highDollarRollCnt = 0
totalTurns = 0
totalScore = 0
# threeOfAKindMinimum = 3

# set game parameters
numGames = 1000
gameTo = 10000
turnScoreTarget = 200


def roll_dice(diceToRoll):
    roll_result = []
    # print("Rolling " + str(numDice) + " dice, roll " + str(turn))
    for x in range(diceToRoll):
        r = random.randint(1, 6)
        # print ("Roll " + str(x) + ": Rolled a " + str(r))
        roll_result.append(r)

    sorted_result = sorted(roll_result)
    print ("Sorted Roll Result: " + str(sorted_result))
    return sorted_result


def play_turn(numDice, runningTurnScore, turnRollNumber):
    rollResult = roll_dice(numDice)
    rollScoreResult = get_role_score(rollResult);
    rollScore = rollScoreResult[0]
    diceUsed = rollScoreResult[1]
    runningTurnScore = runningTurnScore + rollScore

    if (rollScore == 0):
        newDice = -1
    elif (numDice - diceUsed == 0):
        newDice = 6
    else:
        newDice = numDice - diceUsed

    # print (">>  Choosing move, runningTurnScore + rollScore = " + str(runningTurnScore + rollScore) +", rollScore = " +
    #        str(rollScore) + ", newDice = " + str(newDice) )
    if(rollScore == 0): # Farkle occurs
        result = 0
    elif runningTurnScore > turnScoreTarget and newDice < 6: # Decide to take points and stop rolling
        print ("Choosing to stop rolling")
        result = rollScore
    else: # keep rolling
        print ("Successful role,  going deeper.  Calling play_turn(" + str(newDice) + ")"
          ", runningTurnScore is " + str(runningTurnScore))
        result = play_turn(newDice, runningTurnScore, turnRollNumber + 1)
        if result == 0:
            return 0
        else:
            return rollScore + result

    return result


def get_role_score(diceRolled):
    # Initialize counters
    roleScore = 0
    diceUsed = 0
    global highDollarRollCnt
    global fhCnt
    global straightCnt
    global farkleCnt

    # Check for High Dollar rolls
    if(len(diceRolled) == 6):
        highDollarRollCnt += 1
        if(diceRolled[0] == diceRolled[1] and diceRolled[2] == diceRolled[3] and diceRolled[4] == diceRolled[5]):
            print("Full House,  scores 1500 points")
            roleScore = 1500
            diceUsed = 6
            fhCnt += 1
            return [roleScore, diceUsed]

        elif (diceRolled[0] == 1 and diceRolled[1] == 2 and diceRolled[2] == 3 and diceRolled[3] == 4 and diceRolled[4] == 5 and diceRolled[5] == 6 ):
            print("1-6 Straight,  scores 1500 points")
            roleScore = 1500
            diceUsed = 6
            straightCnt += 1
            return [roleScore, diceUsed]

    # Check for 3 of a kinds
    if(len(diceRolled) >= 3):
        if(diceRolled.count(1) == 3):
            roleScore += 1000
            diceUsed += 3
            print("Three of a kind - ones, 1000 points")
        elif (diceRolled.count(2) == 3):
            roleScore += 200
            diceUsed += 3
            print("Three of a kind - twos, 200 points")
        elif (diceRolled.count(3) == 3):
            roleScore += 300
            diceUsed += 3
            print("Three of a kind - threes, 300 points")
        elif (diceRolled.count(4) == 3):
            roleScore += 400
            diceUsed += 3
            print("Three of a kind - fours, 400 points")
        elif (diceRolled.count(5) == 3):
            roleScore += 500
            diceUsed += 3
            print("Three of a kind - fives, 500 points")
        elif (diceRolled.count(6) == 3):
            roleScore += 600
            diceUsed += 3
            print("Three of a kind - sixes, 600 points")

    # Check for survival rolls
    if(roleScore == 0):
        if 1 in diceRolled :
            print ("Taking a one - 100 points")
            roleScore += 100
            diceUsed += 1
        elif 5 in diceRolled :
            print ("Taking a five - 50 points")
            roleScore += 50
            diceUsed += 1

    if(roleScore == 0):
        print ("Farkle occurs")
        farkleCnt += 1

    return [roleScore, diceUsed]





print("Hello, this is the farkle simulator")
initialTime = time.perf_counter()

for game in range(1, numGames + 1):
    # Play game
    gameScore = 0
    turnNumber = 1
    print ("\n")
    print ("Beginning to play game number " + str(game))

    while( gameScore < gameTo):
        # Play turn
        print ("Playing turn number: " + str(turnNumber))
        numDice = 6
        runningTurnScore = 0
        turnScore = play_turn(numDice, runningTurnScore, 1)
        print ("Score result for the turn was: " + str(turnScore))
        print ("\n")
        if(turnScore != 0):
            gameScore += turnScore
        turnNumber += 1

    totalTurns += turnNumber
    totalScore += gameScore
    print("End of game                  " + str(game))
    print("Final game score:            " + str(gameScore))
    print("Number of turns played:      " + str(turnNumber))
    print("Average turn score:          " + str(gameScore / turnNumber))

print ("\n")
print("     Time elapsed in seconds:     " + str(time.perf_counter() - initialTime))
print("     Number of games played:      " + str(numGames))
print("     Turn score target:           " + str(turnScoreTarget))
print("     Average turns to win:        " + str(totalTurns / numGames))
print("     Final number of straights:   " + str(straightCnt))
print("     Final number of full houses: " + str(fhCnt))
print("     Final number of farkles:     " + str(farkleCnt))
print("     Average turn score:          " + str(totalScore / totalTurns))
