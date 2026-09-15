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

rock_paper_scissors = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
pc_choice = random.randint(0, 2)
if user_choice == pc_choice:
    print(rock_paper_scissors[user_choice], "equals", rock_paper_scissors[pc_choice])
elif (user_choice == 0 and pc_choice == 2) or (user_choice == 1 and pc_choice == 0) or (user_choice == 2 and pc_choice == 1):
    print(rock_paper_scissors[user_choice], "beats", rock_paper_scissors[pc_choice])
else:
    print(rock_paper_scissors[pc_choice], "beats", rock_paper_scissors[user_choice])