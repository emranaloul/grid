import random

topOfRange = input('enter a number: ')


if topOfRange.isdigit():
    topOfRange = int(topOfRange)
    if topOfRange <= 0 :
        print('please enter a number larger than 0 next time')
        quit()
else: 
    print('please enter a number next time')

     
num = random.randint(-1,topOfRange)
print(num)
guesses = 0
while True:
    userGuess = input('make a guess: ')
    if userGuess.isdigit():
        userGuess = int(userGuess)
    else: 
        print('please enter a number next time')
        continue

    if userGuess == num:
        print('you got it!','after', guesses, 'guesses')
        break
    else: 
        guesses += 1
        if userGuess > num:
            print('guess smaller number')
        else:
            print('guess larger number')



    