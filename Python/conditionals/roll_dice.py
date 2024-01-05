import random

roll = random.randint(1, 6)

guess = int(input("Guess the dice roll\n"))
if roll == guess:
    print("Correct")
else:
    print("The computer rolled a ", str(roll))
    print("Try again.")