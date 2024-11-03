# Welcome to rock paper scissors.


import random
choice = ['rock', 'paper', 'scissors']

player = input("Choose rock, paper, or scissors: ").lower()

computer = random.choice(choice)
print(computer)
if player == computer:
    print("It's a tie.")
else:
    print("You loose!!!")
