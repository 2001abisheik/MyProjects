from replit import clear
from art import logo
print(logo)
bidders={}
print("Welcome to secret auction program")
stoploop=False
result=0
winner=" "

while not stoploop:
  name=input("What is your name: ")
  bid=int(input("What is your bid: "))
  bidders[name]=bid
  next=input("Are there any other bidders? type 'yes' or 'no' ")
  if next =="yes":
    clear()
  elif next =="no":
    stoploop=True
for key in bidders:
  result=bidders[key]
  winner=key
  
  if bidders[key]>result:
    result=bidders[key]
    winner=key
    
print(f"winner of the auction is {winner} with bid of {result}")
print(bidders)