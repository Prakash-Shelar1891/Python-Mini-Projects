from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the secret Auction program.")

bid_record = {}
while True:
  name = input("Enter Your Name: ")
  bid = int(input("Enter Your Bid amount $: "))

  bid_record[name] = bid

  ch = input("\nAre there any other bidders? Type 'Yes' or 'No': ").lower()
  if ch == 'yes':
    clear()
  else:
    break

max_bid = 0
for key in bid_record:
  if max_bid < bid_record[key]:
    max_bid = bid_record[key]
    name = key
    
print(f"\nThe winner is {name} with a bid of ${max_bid}")
