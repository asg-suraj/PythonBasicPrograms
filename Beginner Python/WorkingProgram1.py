#Complete Program
#This is guess the number game 

import random

print('Hello What is your name')

name = input()

SecretNumber = random.randint(1,20)
print( 'Hello,'+str(name)+' I am Thinking of Number between 1 to 20 try to guess it')

for guessTaken in range (1,8):
    print('Hey, Guess the Number')
    guess = int(input())

    if(guess < SecretNumber):
        print('Your number is low')
    
    elif(guess > SecretNumber):
        print('Your number is High')
    else:
        break

if(guess == SecretNumber):
    print('Voila, u got me !! The number u guessed in '+ str(guessTaken) + " guesses")
else:
    print('u lost, the number is '+ str(SecretNumber))
