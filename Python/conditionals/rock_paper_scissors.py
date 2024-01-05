import random

computer_choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(computer_choices)
print("computer choice", computer_choice)

user_choice = input("Do you want to play rock, paper, or scissors?\n")

if computer_choice == user_choice:
    print("TIE")
    print("computer choice", computer_choice)
elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'scissors' and computer_choice == 'paper'):
    print("USER WINS")
    print("computer choice", computer_choice)
elif (computer_choice == 'rock' and user_choice == 'paper') or (computer_choice == 'scissors' and user_choice == 'paper'):
    print("COMPUTER WINS")
    print("computer choice", computer_choice)