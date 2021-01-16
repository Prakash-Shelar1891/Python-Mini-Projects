import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user = []
comp = []

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

# Get random cards for User and Computer
def get_card(player):
    temp = random.choice(cards)
    if temp == 10:
        player.append(temp)
    elif temp not in player:
        player.append(temp)
    else:
        get_card(player)

# Check score
def score(user, comp):
    if sum(user) > 21:
        #print("User sum over 21")
        if 11 in user:                 # User is over 21 but has ACE
            print("You have ACE so it will count as 1")
            user.remove(11)
            user.append(1)
            #print('user',user)

        else:                         # User is over 21 and dont have ACE 
            return "User Loss"

while True:
    main_choice = input("\nDo you want to play Backjack game, Type 'y' or 'n': ").lower()
    if main_choice == 'n':
        break

    elif main_choice == 'y':
        print(logo)
        
        if len(user) > 0:
            user.clear()
            comp.clear()

        print("\nAdded 2 cards for you and computer")

        for _ in range(2):
            get_card(user)
            get_card(comp)

        print(f"Your cards are {user} and score is {sum(user)}")
        print(f'Computers first card is: [{comp[0]}]')

        while True:
            # Check for Black Jack
            if sum(user) == 21 and 11 in user:
                if sum(comp) == 21:            # If user and comp both have blackjack then computer must win.
                    print("\nComputer win with Blackjack...!!!!!")
                    break
                else:
                    print("\nYou win with Blackjack...!!!!!")
                    break
            elif sum(comp) == 21 and 11 in comp:
                print("\nComputer win with Blackjack...!!!!!")
                break
            
            choice = input("\nType 'Y' to add card or 'N' to pass: ").lower()
            if choice == 'y':
                get_card(user)                 # Get Random card

                result = score(user, comp)
                print(f"\nYour cards are {user} and score is {sum(user)}")
                print('Computers first card: ',comp[0])
                
                if result == 'User Loss':
                    print("\nYour score is more than 21 so Computer wins...!!!")
                    break
                    
            elif choice == 'n':
                if sum(comp) < 17:              # Computers score is less than 17
                    print("\nComputers turn")
                    get_card(comp)              # One more card is added for computer

                if sum(comp) > 21:
                    print("\nComputer wins...!!!!")
                    break

                elif sum(comp) > sum(user):
                    print("\nComputer wins...!!!!")
                    break

                elif sum(comp) < sum(user):
                    print("\nYou wins...!!!!")
                    break

                elif sum(comp) == sum(user):
                    print("\nDraw...!!!!")
                    break
                break
            
        print(f"\nYour cards are {user} and Final Score is {sum(user)}")
        print(f"Computers's cards are {comp} and Final Score is {sum(comp)}")
