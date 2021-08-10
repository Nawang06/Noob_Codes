from art import logo

def add (n1,n2):
  result = n1 + n2
  return result

def subtract (n1,n2):
  result = n1 - n2
  return result

def multiply (n1,n2):
  result = n1 * n2
  return result

def division (n1,n2):
  result = n1 / n2
  return result

operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":division,  
}

def calculator ():
  print(logo)
  num1 = float(input("What's the first number? "))

  for symbol in operations:
    print(symbol)

  symbol = input("Enter the operation which you want to perform: ")
  num2 = float(input("What's the second number? "))
  answer = operations[symbol](num1,num2)
  is_continue = True

  while(is_continue):
    print(f"{num1} {symbol} {num2} = {answer}")
    choice = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation and q to quit: ")
    if(choice == "n"):
      is_continue = False
      calculator()
    elif(choice == "q"):
      break
    else:
      symbol = input("Pick the next operation: ")
      num2 = float(input("What's the next number?: "))
      answer = operations[symbol](answer,num2)

calculator()