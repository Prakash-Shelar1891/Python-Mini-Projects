import game_data
import random
score = 0

def game(score):
    
    A = random.choice(game_data.data)           #Get random persons record from list of game_data
    B = random.choice(game_data.data)           #Get random persons record from list of game_data
    
    A_follower_count = A['follower_count']      #Get first persons follower_count
    #print(A_follower_count)

    B_follower_count = B['follower_count']      #Get second persons follower_count
    #print(B_follower_count)
    
    print(f"\nCompare A: {A['name']}, {A['description']} from {A['country']}")
    print("\nVS")
    print(f"\nCompare B: {B['name']}, {B['description']} from {B['country']}")

    choice = input("\nWho has more followers\nType 'A' or 'B': ").upper()
    
    if choice == 'A':                           #User Chooses A
        if A_follower_count >= B_follower_count:
            score += 1
            print(f"\nYou are correct, Your score is {score}\n Lets continue...")
            game(score)                         #Choice is correct so loop again for another 2 persons
        else:
            print(f"\nYou are wrong\nYour final score is {score}")
            
    elif choice == 'B':                         #User Chooses B
        if B_follower_count >= A_follower_count:
            score += 1
            print(f"\nYou are correct, Your score is {score}\n Lets continue...")
            game(score)                         #Choice is correct so loop again for another 2 persons
        else:
            print(f"\nYou are wrong\nYour final score is {score}")


while True:
    main_choice = input("\nDo you want to play Higher_Lower Game, Type 'Y' or 'N': ").lower()
    if main_choice == 'y':
        game(score)
        
    elif main_choice == 'n':
        break
