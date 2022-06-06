import random

choices = ["rock", "paper", "scissors"]

computer = random.choice(choices)
player = None

while player not in choices:
    if player is None:
        player = input("rock, paper, or scissors?: ").lower()
    else:
        print("Not a option!")
        player = input("rock, paper, or scissors?: ").lower()

while player == computer:
    print("Player: (" + player + ") : CPU: (" + computer + ")")
    print("It's a tie!")
    player = input("rock, paper, or scissors?: ").lower()

if player == "rock":
    if computer == "paper":
        print("Player: (" + player + ") : CPU: (" + computer + ")")
        print("You lose!")
    elif computer == "scissors":
        print("Player: (" + player + ") : CPU: (" + computer + ")")
        print("You win!")

if player == "paper":
    if computer == "scissors":
        print("Player: (" + player + ") : CPU: (" + computer + ")")
        print("You lose!")
    elif computer == "rock":
        print("Player: (" + player + ") : CPU: (" + computer + ")")
        print("You win!")

if player == "scissors":
    if computer == "paper":
        print("Player: (" + player + ") : CPU: (" + computer + ")")
        print("You win!")
    elif computer == "rock":
        print("Player: (" + player + ") : CPU: (" + computer + ")")
        print("You lose!")
