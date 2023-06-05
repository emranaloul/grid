print('welcome to my computer quiz!!')

playing = input('Do you want to play? ')



if playing != 'yes': 
    quit()
score = 0
print('let`s play :)')

answer =  input('what the sun is? ')

if answer == 'star':
    print('correct')
    score +=1
else:
    print('incorrect')

answer =  input('what you are? ')

if answer == 'human':
    print('correct')
    score +=1
else:
    print('incorrect')

    
print('your score is ',score,  ' of 2')