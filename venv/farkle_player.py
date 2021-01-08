class farklePlayer:
    def __init__(id, strategy):
        self.id = id
        self.strategy = strategy
        self.gameScore = 0

        # Player event counters
        self.highDollarRollCnt = 0
        self.fhCnt = 0
        self.straightCnt = 0
        self.farkleCnt = 0

        if (strategy == 'High Dollar Roles'):
            self.
        elif (strategy == 'Conservative'):
        elif s


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
        if (rollScore == 0):  # Farkle occurs
            result = 0
        elif runningTurnScore > turnScoreTarget and newDice < 6:  # Decide to take points and stop rolling
            print ("Choosing to stop rolling")
            result = rollScore
        else:  # keep rolling
            print ("Successful role,  going deeper.  Calling play_turn(" + str(newDice) + ")"
                                                                                          ", runningTurnScore is " + str(
                runningTurnScore))
            result = play_turn(newDice, runningTurnScore, turnRollNumber + 1)
            if result == 0:
                return 0
            else:
                return rollScore + result

        return result