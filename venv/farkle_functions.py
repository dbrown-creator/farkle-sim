import random
import player1

player = player1

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
    rollScoreResult = player.get_role_score(rollResult);
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