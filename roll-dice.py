import random

start = input('Press 1 roll one 2 dice or press 2 to roll a pair of dice: ')

if(start == '1'):
    diceNumber = random.randint(1,6)
    print(diceNumber)
elif(start == '2'):
    diceNumber = random.randint(2,12)
    print(diceNumber)
else:
    print(start)