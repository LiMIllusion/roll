import sys
from random import randint
import re

def rollDice (dice="1d6"):


    diceNotationRegex = re.compile(r'\d*d\d+([+-]\d+)?')
    if not diceNotationRegex.search(dice):
        raise Exception ("Invalid dices passed to the program. Check dice notation")


    numberOfDices = ""
    rangeOfNumbers = ""
    bonusOrMalus= ""
    rollsOfDices=[]
    iterationType = 0
    '''
        iterationTypes = 
        0 - numberOfDices, the numbers before the 'd' in nndnn+/-nn
        1 - rangeOfNumbers, the numbers after the 'd' in nndnn+/-nn
        2 - bonusOrMalus, the values from the +/- in nndnn+/-nn
    '''

    for diceStringIndex in range (len(dice)):
        if dice[diceStringIndex] == 'd':
            iterationType += 1 
            if not numberOfDices:
                numberOfDices += "1"
            continue
        if dice[diceStringIndex] == '-' or dice[diceStringIndex] == '+' :
            iterationType += 1 
            bonusOrMalus += dice[diceStringIndex]
            continue
        if dice[diceStringIndex].isdigit():
            if iterationType == 0:
                numberOfDices += dice[diceStringIndex]
            elif iterationType == 1: 
                rangeOfNumbers += dice[diceStringIndex]
            elif iterationType == 2: 
                bonusOrMalus += dice[diceStringIndex]
            else:
                pass
            continue
    
    print("================================")
    print("Number of Dices: "+numberOfDices)
    
    print("Range: "+rangeOfNumbers)

    if bonusOrMalus :
        print("Bonus or Malus: " + bonusOrMalus)
    
    
    for roll in range (int(numberOfDices)):
        rollsOfDices.append(randint(1, int(rangeOfNumbers)))
        print("Roll #" + str(roll+1) + ": "+str(rollsOfDices[-1]))
    totalValue = sum(rollsOfDices) + (int(bonusOrMalus) if bonusOrMalus else 0)
    print("\nTotal: "+ "+".join(str(val) for val in rollsOfDices) + (bonusOrMalus if bonusOrMalus else "") + " = " + str(totalValue))
    
    
    print("================================")

if __name__ == "__main__":

    if "-h" in sys.argv or "--help" in sys.argv:
        pass
    all_dices= sys.argv[1:]
    if not all_dices:
        rollDice()
        sys.exit(0)
    for dice in all_dices:
        rollDice(dice)
    sys.exit(0)