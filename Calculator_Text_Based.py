logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1, n2):
  return n1 + n2

def sub(n1, n2):
  return n1 - n2

def mul(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return ((n1 / n2), n2)

op = {"+": add,
      "-": sub,
      "*": mul,
      "/": divide
     }


def calc():
  print(logo)
  try:
    n1 = float(input("what's the first number?: "))
    #Print operators symbols from dictionary
    for key in op:
      print(key)
    #Get input of symbol
    operation = input("Pick an operation: ")
    n2 = float(input("what's the next number?: "))

    #Get function name from ditionary 
    function = op[operation]
    #Call function
    result = function(n1, n2)
    
    print(f"{n1} {operation} {n2} = {result}")

    #For more calculations
    while True:
      check = input(f"\nType 'Y' to continue calculating with {result} \nor type 'N' to start the new calculations,\nOr Type 'Close' for closing Calculator\n").strip().lower()

      if check == 'n':     #For New calculation
        print("\nCalculator Restarted!!!")
        calc()             #Recursion starts execution from beginning
      elif check == 'y':   #For continuing calculation on previous result
          operation = input("Pick an operation: ")
          n3 = float(input("what's the next number?: "))
          function = op[operation]
          new_result = function(result, n3)
          print(f"{result} {operation} {n3} = {new_result}")
          result = new_result
      elif check == 'close':
          break

  except Exception:
    print("\nWrong Input...\nCalculator Restarted!!!")
    calc()
calc()
