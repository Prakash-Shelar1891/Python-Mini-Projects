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
import random

game = ['Rock', 'Paper', 'Scissors']

while True:
    user = int(input("\nWhat do you choose? \nType 0 for Rock, \n1 for Paper or \n2 for Scissors.\n"))

    if user in range(0,2):
      if user == 0:
        print(rock)
      elif user == 1:
        print(paper)
      elif user == 2:
        print(scissors)

      user = game[user]
      print("Your choice is:",user)

      comp = random.randint(0,2)
      if comp == 0:
        print(rock)
      elif comp == 1:
        print(paper)
      elif comp == 2:
        print(scissors)

      comp = game[comp]
      print("Computers choice is:",comp)

      if user == 'Scissors' and comp =='Paper':
        print("You win")
      elif user == 'Paper' and comp == 'Rock':
        print("You Win")
      elif user == 'Rock' and comp == 'Scissors':
        print("You win")
      elif user == comp:
        print("Tie...!!!")
      else:
        print("Computer win")
    else:
      print("Invalid Input")

