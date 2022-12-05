print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
total_letter = (name1 +name2).upper()
true=0
love=0

for char in (total_letter):
    if char =="T":
        true+=1
    elif char =="R":
        true+=1
    elif char =="U":
        true+=1
    elif char =="E":
        true+=1
        love+=1
    elif char =="L":
        love+=1
    elif char =="O":
        love+=1
    elif char =="V":
        love+=1
true=str(true)
love=str(love)
true_love=int(true+love)


if true_love >=40 and true_love <=50:
    print(f"Your score is {true_love}, you are alright together.") 
elif true_love >90 or true_love < 10:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
else:
    print(f"Your score is {true_love}")
    