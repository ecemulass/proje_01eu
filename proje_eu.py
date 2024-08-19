import random

print('Welcome to the game called "Are You Gonna Beat Me"')
options = ["rock", "paper", "scissors"]

gamer_score = 0
computer_score = 0

while gamer_score < 2 and computer_score < 2:

    gamer = input('What is your choice? (rock, paper, scissors, or exit): ').lower()
    computer = random.choice(options)
    print(f"Computer's choice: {computer}")

    if gamer == "exit":
        print("Are you kidding me? Why are you here though?")
        break

    if gamer not in options:
        print('There is something wrong, please try again.')
        continue

    if gamer == computer:
        print('It is a tie! Score doesn\'t change.')

    elif gamer == "rock":
        if computer == "scissors":
            print('Congrats! You are the winner.')
            gamer_score += 1
        else:
            print("You lost.")
            computer_score += 1

    elif gamer == "paper":
        if computer == "rock":
            print('Congrats! You are the winner.')
            gamer_score += 1
        else:
            print('You lost.')
            computer_score += 1
    
    elif gamer == "scissors":
        if computer == "paper":
            print('Congrats! You are the winner.')
            gamer_score += 1
        else:
            print('You lost.')
            computer_score += 1

    print(f"Score: You {gamer_score} - Computer {computer_score}")

    answer = input('Do you want to continue? (yes or no): ').lower()
    if answer == 'no':
        print("Thanks for playing!")
        break
    elif answer == 'yes':
        continue
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        break
