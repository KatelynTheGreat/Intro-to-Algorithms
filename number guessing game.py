#imports
import math
import random

#self-explanitory
random_number = random.randint(1, 100)


#the entire game
def algorithmGame(rando_number):

    rando_number = random_number

    score = int(10)

    guess = int(input('I have thought of a number between 1 and 100. Can you guess what it is? Write your answer here: '))

    if guess == rando_number:
        print(f"Congrats! You guessed right!! You finished with a score of {score}.")
    elif guess > rando_number:
        score -= 1
        print(f"A bit lower than that! You've lost a point and now your score is at {score}.")
        algorithmGame(rando_number)
    elif guess < rando_number:
        score -= 1
        print(f"A bit higher than that! You've lost a point and now your score is at {score}.")
        algorithmGame(rando_number)
    else:
        print('what')
        algorithmGame(rando_number)
    
    if score == 0:
        print("Aw man, your score reached zero! Well, there's always next time!!")
    
    



algorithmGame(random_number)