import random

user_win = 0
computer_win = 0

option = ["rock","paper","scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissor or q for Quit: ").lower()

    if user_input == "q":
        quit()

    if user_input not in option:
        continue

    random_number = random.randint(0,2)
    computer_input = option[random_number]

    if user_input == "rock" and computer_input == "scissor":
        print("You won!")
        user_win += 1
    elif user_input == "scissor" and computer_input == "paper":
        print("you won!")
        user_win += 1
    elif user_input == "paper" and computer_input == 'rock':
        print("you won!")
        user_win += 1
    else:
        print("you lost :( ")
        computer_win += 1
