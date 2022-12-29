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
import random

options = [rock, scissors, paper]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Scissors or 2 for Paper.\n"))
print(options[user_choice])

computer_choice = random.randint(0, 2)
print(f"Computer chose:\n{options[computer_choice]}")

if user_choice == computer_choice:
    print("It's a draw!")
elif ((computer_choice - user_choice) % 3 == 1):
    print("You win!")
elif ((computer_choice - user_choice) % 3 == 2):
    print("You loose!")