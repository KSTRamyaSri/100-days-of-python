print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You\'re at a cross road. Where do you want to go?\n Type \"left\" or \"right\" ")
direction = input().lower()
if direction != "left" :
    print("Fall into hole. Game over")
else:
    print("You\'ve come to a lake. There is an island in the middle of the lake.\nType \"wait\" to wait for a boat. Type \"swim\" to swim across")
    action = input().lower()
    if action != "wait":
        print("Attacked by trout.Game Over.")
    else :
        print("You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. Which colour do you choose??")
        door = input().lower()
        if door == "red" :
            print("Burned by fire.Game Over.")
        elif door == "blue" :
            print("Eaten by Beasts.Game Over.")
        elif door == "yellow" :
            print("You found the treasure! You Win!")
        else :
            print("You chose a door that doesn't exist.Game Over.")


# refinede solution of day3.py


# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
# choice1 = input('You\'re at a crossroad, where do you want to go? '
#                 'Type "left" or "right".\n').lower()

# if choice1 == "left":
#     choice2 = input('You\'ve come to a lake. '
#                     'There is an island in the middle of the lake. '
#                     'Type "wait" to wait for a boat. '
#                     'Type "swim" to swim across.\n').lower()
#     if choice2 == "wait":
#         choice3 = input("You arrive at the island unharmed. "
#                         "There is house with 3 doors. One red, "
#                         "one yellow and one blue. "
#                         "Which colour do you choose?\n").lower()
#         if choice3 == "red":
#             print("It's a room full of fire. Game Over")
#         elif choice3 == "yellow":
#             print("You found the treasure. You Win!")
#         elif choice3 == "blue":
#             print("You enter a room of beasts. Game Over.")
#         else:
#             print("You chose a door that doesn't exist. Game Over.")
#     else:
#         print("You got attacked by an angry trout. Game Over.")

# else:
#     print("You fell in to a hole. Game Over.")