from replit import clear
from art import logo
import re

print(logo)

bid_dict = {}
def add_bidders(name,bid_price):
  bid_dict[name] = bid_price

def highest_bid(bid_dict):
  highest_bidder = max(bid_dict,key=bid_dict.get)
  bid_value = bid_dict[highest_bidder]
  print(f"\nThe winner of the silent auction is {highest_bidder} with a bid of {bid_value}\n")

continue_bid = True
while continue_bid:
  try:
    name = input("Name of the bidder: \n")
    bid_price = int(input("Please type in the bid you want to place: \n"))
    add_bidders(name,bid_price)
  except:
    print("Please check your input!!")

  user_input = input("Type 'Yes' to make another bid ,type 'No' to check the results\n").lower()
  if re.match("yes",user_input) or re.match("no",user_input):
    if user_input == "no":
      continue_bid = False
      highest_bid(bid_dict)
    else:
      clear()
