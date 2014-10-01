from random import randint

print('come-out')
firstRoll = randint(1, 6) 
secondRoll = randint(1, 6)
rollSum = firstRoll + secondRoll        
print(rollSum)
if rollSum == 7 or rollSum == 11:
    print('You win!')
elif rollSum == 2 or rollSum == 3 or rollSum == 12:
    print('Craps, you lose.')
else:
    print('The point is', rollSum)
    firstRoll = randint(1, 6)
    secondRoll = randint(1, 6)
    rollSum2 = firstRoll + secondRoll         
    print(rollSum2)
    while rollSum2 != rollSum and rollSum2 != 7:
        firstRoll = randint(1, 6)
        secondRoll = randint(1, 6)
        rollSum2 = firstRoll + secondRoll
        print(rollSum2)
    if rollSum2 == 7:
        print('Seven out, you lose.')
    else:
        print('Pass, you win!')
