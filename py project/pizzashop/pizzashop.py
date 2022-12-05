print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
bill =0
if size == "s":
    bill+=15
elif size == "m":
    bill+=20
elif size == "l":
    bill+=25
if size == "s"or size == "l"or size == "m":
    add_pepperoni = input("Do you want pepperoni? Y or N ")
    if add_pepperoni =="y":
        if size == "s":
            bill+=2
        elif size == "l" or size == "m":
            bill+=3
    extra_cheese = input("Do you want extra cheese? Y or N ")      
    if extra_cheese == "y":
        bill+=1
        print(f"your final bill is ${bill}")
    else:
        print(f"your final bill is ${bill}")
else:
    print("wrong size")
