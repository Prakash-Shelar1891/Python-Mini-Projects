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
    
    try:
        #Get input from user of their choice
        user = int(input("\nWhat do you choose? \nType 0 for Rock, \n1 for Paper or \n2 for Scissors.\n"))

    except Exception:
        print("Please give valid input")
        continue
    
    if user in range(0,3):  #Check users input is valid
      #Print Symbols of users input
      if user == 0:
        print(rock)
      elif user == 1:
        print(paper)
      elif user == 2:
        print(scissors)

      #Get actual value (Rock, Paper, Scissors)
      user = game[user]
      print("Your choice is:",user)

      #Genaarate random num for computer
      comp = random.randint(0,2)
      #Print Symbols
      if comp == 0:
        print(rock)
      elif comp == 1:
        print(paper)
      elif comp == 2:
        print(scissors)

      #Get actual value (Rock, Paper, Scissors)
      comp = game[comp]
      print("Computers choice is:",comp)

      #Code for checking winner
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

    #Ask user to play again or stop
    c = input("\nDo you want to play again? Type Y or N ").upper()
    if c != 'Y':
        break

