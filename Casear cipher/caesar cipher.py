import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

symbol = '[@_!#$%^&*()<>?/\|}{~:]'

def caesar(text, shift, direction):
    end_text =[]

    # when decoding we must substract and move backword 
    if direction == 'decode':
        shift *= -1

    for char in text:
    #keep the number/symbol/space when the text is encoded/decoded
      if char == ' ' or char.isnumeric() or char in list(symbol):
        end_text.append(char)
        continue
      
      # Shifting char for encoding / decoding
      position = alphabet.index(char)
      new_position = shift + position
      end_text.append(alphabet[new_position])
      
    print(f"The {direction}d text is {''.join(end_text)}")

choice = 'yes'

while choice == 'yes':
  direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  # If the user enters a shift that is greater than the number of letters in the alphabet
  shift = shift % 26
  
  caesar(text, shift, direction)
  
  choice = input("\nDo you want to restart the cipher program? \nType Yes or No: ").lower()
