# Python

# Day5: Rock,Paper and Scissors game (Mini Project)
# Topics covered: Taking user input, random module, if-elif-else.  

import random                                   # uses random module to generate random number.

print("Welcome to rock paper scissor:")

a = int(input("Enter 1 to play: \nEnter 2 to quit: \n"))

if ( a == 1):
    human = int(input("Enter 1 for Rock: \nEnter 2 for paper: \nEnter 3 for scissors: \n"))
    computer = random.randint(1,3)                                                            # Generates random number from 1 to 3.

    if (human == 1):
        print("You choose rock.")
    elif(human == 2):
        print("You choose paper.")
    elif(human == 3):
        print("You choose scissors.")
    else:
        print("Invalid input: ")
    
    if (computer == 1):
        print("Computer choose rock.")
    elif(computer == 2):
        print("Computer choose paper.")
    elif(computer == 3):
        print("Computer choose scissors.")

    if (computer == 1 and human == 3 or computer == 2 and human == 1 or computer == 3 and human == 2):
        print("You lose! ")
    elif(human == 1 and computer == 3 or human == 2 and computer == 1 or human == 3 and computer == 2):
        print("You wins! ")
    elif(human == 1 and computer == 1 or human == 2 and computer == 2 or human == 3 and computer == 3):
        print("Draw! ")
        
    
else:
    print("Thank you, have a great day. ")