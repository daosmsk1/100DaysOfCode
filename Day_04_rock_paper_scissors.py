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

#Write your code below this line 👇

move_list = [rock, paper, scissors]

user_choice = input("What do you chose? Type 0 for Rock, 1 for Paper, 2 for Scissors \n")
user_choice = int(user_choice)
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(move_list[user_choice])

    pc_choice = random.randint(0, 2)
    print("Computer chose: \n", move_list[pc_choice])

    if user_choice == 0:
        if pc_choice == 1:
            print("You lose")
        else:
            print("You win")
    elif user_choice == 1:
        if pc_choice == 2:
            print("You lose")
        else:
            print("You win")
    elif user_choice == 2:
        if pc_choice == 0:
            print("You lose")
        else:
            print("You win")
    else:
        print("Draw")