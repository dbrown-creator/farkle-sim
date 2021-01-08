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


# print("Hello, this is the farkle simulator")
# initialTime = time.perf_counter()
#
# for game in range(1, numGames + 1):
#     # Play game
#     gameScore = 0
#     turnNumber = 1
#     print ("\n")
#     print ("Beginning to play game number " + str(game))
#
#     while( gameScore < gameTo):
#         # Play turn
#         print ("Playing turn number: " + str(turnNumber))
#         numDice = 6
#         runningTurnScore = 0
#         turnScore = play_turn(numDice, runningTurnScore, 1)
#         print ("Score result for the turn was: " + str(turnScore))
#         print ("\n")
#         if(turnScore != 0):
#             gameScore += turnScore
#         turnNumber += 1
#
#     totalTurns += turnNumber
#     totalScore += gameScore
#     print("End of game                  " + str(game))
#     print("Final game score:            " + str(gameScore))
#     print("Number of turns played:      " + str(turnNumber))
#     print("Average turn score:          " + str(gameScore / turnNumber))
#
# print ("\n")
# print("     Time elapsed in seconds:     " + str(time.perf_counter() - initialTime))
# print("     Number of games played:      " + str(numGames))
# print("     Turn score target:           " + str(turnScoreTarget))
# print("     Average turns to win:        " + str(totalTurns / numGames))
# print("     Final number of straights:   " + str(straightCnt))
# print("     Final number of full houses: " + str(fhCnt))
# print("     Final number of farkles:     " + str(farkleCnt))
# print("     Average turn score:          " + str(totalScore / totalTurns))
