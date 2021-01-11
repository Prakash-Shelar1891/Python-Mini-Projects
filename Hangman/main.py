import random
import hangman_art
import hangman_words

print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)

#'lives' keep track of the number of lives left. 
lives = 6

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(len(chosen_word)):
    display.append('_')

while True:
    guess = input("Guess a letter: ").lower()

    #If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."
    if guess not in chosen_word:
      lives -=1

      if lives == 0:
        print(hangman_art.stages[lives])
        print("You Loose")
        break

      print(f"You guessed {guess}, thats not in the word. you lose a life\n{hangman_art.stages[lives]}\nYou have {lives} lifes left")
      #continue

    #Check guessed letter
    for char in range(len(chosen_word)):
        if chosen_word[char] == guess:
            display[char] = guess
    
    print(' '.join(display))

    #Check if user has got all letters.
    if "_" not in display:
        print("You win.")
        break
