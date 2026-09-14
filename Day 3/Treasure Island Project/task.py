print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
# choice1 = input('You are at a crossroad, where do you want to go? Type "up" or "right" or "left" or "down".\n')
# if choice1 == "up":
#     choise2 = input("You've come to a lake. Now where do you want to go? Type 'right' or 'left'.\n")
#     if choise2 == "right":
#         print("You've found the treasure!")
#     elif choise2 == "left":
#         choice1 = input(
#             'You have made it back where you started! You are at a crossroad, where do you want to go? Type "up" or "right" or "left" or "down".\n')
#     else:
#         print("You've come to a dead end.")
# elif choice1 == "right":
#     choice2 = input("You've come to a river. Now where do you want to go? Type 'right' or 'left'.\n")
#     if choice2 == "right":
#         print("You've found the treasure!")
#     elif choice2 == "left":
#         choice1 = input(
#             'You have made it back where you started! You are at a crossroad, where do you want to go? Type "up" or "right" or "left" or "down".\n')
#     else:
#         print("You've come to a dead end.")
# elif choice1 == "left":
#     choice2 = input("You've come to a forest. Now where do you want to go? Type 'right' or 'left'.\n")
#     if choice2 == "right":
#         print("You've found the treasure!")
#     elif choice2 == "left":
#         choice1 = input(
#             'You have made it back where you started! You are at a crossroad, where do you want to go? Type "up" or "right" or "left" or "down".\n')
#     else:
#         print("You've come to a dead end.")
# elif choice1 == "down":
#     choice2 = input("You've come to a shipyard. Now where do you want to go? Type 'right' or 'left'.\n")
#     if choice2 == "right":
#         print("You've found the treasure!")
#     elif choice2 == "left":
#         returnValue = input() # Returns the code to the beginning.
#     else:
#         print("You've come to a dead end.")
# else:
#     print("You've come to a dead end.")


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

# creation of dictionary (dict)
LOCATIONS = {
    "up": "lake",
    "right": "river",
    "left": "forest",
    "down": "shipyard"
}

while True:
    choice1 = input('You are at a crossroad. Where do you want to go? (up / right / left / down)\n> ').lower().strip() # .strip() - removes leading and trailing spaces. .lower() - converts the string to lowercase.

    if choice1 not in LOCATIONS:
        print("You've come to a dead end.")
        break

    location = LOCATIONS[choice1]
    choice2 = input(f"You've come to a {location}. Now where do you want to go? (right / left)\n> ").lower().strip()

    if choice2 == "right":
        print("You've found the treasure!")
        break
    elif choice2 == "left":
        print("You have made it back to where you started!\n")
    else:
        print("You've come to a dead end.")
        break

