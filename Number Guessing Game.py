import random

def user_guess(attempts):

    print(f"\nYou have {attempts} attempts left.")
    try:
        user = int(input("Guess Number: "))
        if user == comp:
            return "Found"
        elif user > comp:
            return("\nYour guess is Too High...")
            user_guess()
        elif user < comp:
            return("\nYour guess is Too Low...")
            user_guess()
    except Exception:
        return("\nWrong input")

    

def difficulty(level):
    for attempts in range(level, 0, -1):
        a = user_guess(attempts)
        if a == "Found":                  # If guess matches 
            print("\nYour Guess is correct...\nYou win!!!!!")
            break
        else:
            print(a)                      # Print guess High or Low
            if attempts == 1:
                print(f"Your attempts are over!!!!\n The number is: {comp}")
            else:
                print("Guess again!!!")
    
while True:
    choice = input("\nWant to play Number Guessing Game, Type 'Y' to play or 'N' to close: ").lower()

    if choice == 'y':
        print("\nWelcome To Number Guessing Game")
        comp = random.randint(1,100)
        #print(comp)

        level = input("\nChoose your dificulty level, Type 'Easy' or 'Hard': ").lower()
        print("\nGuess number between 1 to 100")
        if level == 'easy':
            level = 10
        elif level == 'hard':
            level = 5
        else:
            print("Wrong input")
            continue

        difficulty(level)
          
    elif choice == 'n':
        break
