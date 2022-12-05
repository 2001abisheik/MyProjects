from replit import clear
from art import logo
def calc():
  def add(num1,num2):
    result=num1+num2
    return result
  def sub(num1,num2):
    result=num1-num2
    return result
  def mul(num1,num2):
    result=num1*num2
    return result
  def div(num1,num2):
    result=num1/num2
    return result
  def operator():
    operation_sym={"+":add,"-":sub,"*":mul,"/":div,}
    for key in operation_sym:
      print(key)
    operation=input("Choose what to perform: ")
    operation=operation_sym[operation]
    return operation
    
  print(logo)
  num1=float(input("Enter first number: "))
  num2=float(input("Enter second number: "))
  answer=operator()(num1, num2)
  print(answer)
  yes = True
  if input("Type 'Y' to stop the calc and 'N' to continue").upper() =="Y":
      yes = False
      clear()
  while yes:
    num3=float(input("Enter next number: "))
    answer=operator()(answer, num3)
    print(answer)
    if input("Type 'Y' to stop the calc and 'N' to continue: ").upper() =="Y":
      yes = False
      clear()
      calc()
calc()
  
  
