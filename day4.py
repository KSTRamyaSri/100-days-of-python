##  Rock Paper Scissors Game ##


## My solution to Day 4 Rock Paper Scissors Project ##


import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
comp_choice = random.randint(0,2)

print("Your Choice: \n")
if user_choice == 0:
    print(rock)
    print("\nComputer Choice: \n")
    if comp_choice == 2:
        print(scissors)
        print("You win!")
    elif comp_choice == 1:
        print(paper)
        print("You lose!")
    else :
        print(rock)
        print("Draw!")
elif user_choice == 1:
    print(paper)
    print("\nComputer Choice: \n")
    if comp_choice == 2:
        print(scissors)
        print("You lose!")
    elif comp_choice == 0:
        print(rock)
        print("You win!")
    else :
        print(paper)
        print("Draw!")
elif user_choice == 2:
    print(scissors)
    print("\nComputer Choice: \n")
    if comp_choice == 0:
        print(rock)
        print("You lose!")
    elif comp_choice == 1:
        print(paper)
        print("You win!")
    else :
        print(scissors)
        print("Draw!")
else :
    print("Invalid Choice!")



## Actual solution to Day 4 Rock Paper Scissors Project ##

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")