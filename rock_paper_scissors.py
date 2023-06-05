import random

userWins = 0
computerWins = 0

options = ['rock', 'paper', 'scissors']

while True:
    userInput = input('type rock/paper/scissors or Q ro quit:  ').lower()
    if userInput == 'q':
        break
    elif userInput not in options:
        continue

    randomNumber = random.randint(0,2)

    computerPick = options[randomNumber]
    print('computer picked', computerPick)
    if userInput == 'rock' and computerPick == 'scissors':
        userWins += 1
        print('you won')
    elif userInput == 'paper' and computerPick == 'rock':
        userWins += 1
        print('you won')
    elif userInput == 'scissors' and computerPick == 'paper':
        userWins += 1
        print('you won')
    else :
        computerWins +=1
        print('you lost')

print('you won', userWins, 'times.')
print('computer won', computerWins, 'times.')
print('Goodbye!')