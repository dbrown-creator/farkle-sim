import random

def roll_dice(diceToRoll):
    roll_result = []
    for x in range(diceToRoll):
        r = random.randint(1, 6)
        roll_result.append(r)

    sorted_result = sorted(roll_result)
    print ("Sorted Roll Result: " + str(sorted_result))
    return sorted_result

def get_role_options(diceRolled):
    # Initialize counters
    roleScore = 0
    diceUsed = 0
    rollOptions = []  # (Roll Title, dice used, roll score)

    # Check for straight and flush
    if(len(diceRolled) == 6):
        if(diceRolled[0] == diceRolled[1] and diceRolled[2] == diceRolled[3] and diceRolled[4] == diceRolled[5]):
            # print("Full House,  scores 1500 points")
            rollOptions.append(("Full House", 6, 1500))
        elif (diceRolled[0] == 1 and diceRolled[1] == 2 and diceRolled[2] == 3 and diceRolled[3] == 4 and diceRolled[4] == 5 and diceRolled[5] == 6 ):
            # print("1-6 Straight,  scores 1500 points")
            rollOptions.append(("1-6 Straight", 6, 1500))

    # Check for of-a-kinds
    threeOfScore = 0
    for x in [1,2,3,4,5,6]:
        if(diceRolled.count(x) == 6):
            # print("6 of a Kind - " + x + "'s,  scores 3000 points")
            rollOptions.append(("6 of a Kind - " + x + "'s", 6, 3000))
            break
        elif (diceRolled.count(x) == 5):
            # print("5 of a Kind - " + x + "'s,  scores 2000 points")
            rollOptions.append(("5 of a Kind - " + x + "'s", 5, 2000))
            break
        elif (diceRolled.count(x) == 5):
            # print("4 of a Kind - " + x + "'s,  scores 1000 points")
            rollOptions.append(("5 of a Kind - " + x + "'s", 4, 1000))
            break
        if (diceRolled.count(x) == 3):
            if(x == 1):
                threeOfScore = 300
            else:
                threeOfScore = x * 100
            rollOptions.append(("3 of a Kind - " + str(x) + "'s", 3, threeOfScore))
            # print("3 of a Kind - " + str(x) + "'s,  scores " + str(threeOfScore) + " points")

    # Check for survival rolls
    scoreCounter = 1
    lastRollScore = 0
    rollScore = 0
    for d in diceRolled:
        if d == 1:
            # print ("Taking a one - 100 points")
            rollScore += 100
            diceUsed += 1
        elif d == 5 in diceRolled :
            # print ("Taking a five - 50 points")
            rollScore += 50
            diceUsed += 1

        if(rollScore > lastRollScore):
            rollOptions.append(("Survival Roll " + str(scoreCounter), diceUsed, rollScore))
            if(threeOfScore > 0):
                rollOptions.append(("Survival Roll " + str(scoreCounter) + " + 3-of-a-kind", diceUsed + 3,
                    rollScore + threeOfScore))
            lastRollScore = rollScore
            scoreCounter += 1

    return rollOptions


# Checking roll options results for 1 roll
roll = roll_dice(6)
print (str(roll))
options = get_role_options(roll)
print ("Options = ")
for z in options:
    print(str(z) + "\n")