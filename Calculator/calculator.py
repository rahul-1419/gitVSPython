def add (num1,num2):
    return num1 + num2

def sub (num1,num2):
    return num1 - num2

def mul (num1,num2):
    return num1 * num2

def div (num1,num2):
    return num1 / num2

print("Select opration want to perform:\n"
      "1: add \n"
      "2: sub \n"
      "3: mul \n"
      "4: div \n")

select = int(input("Select option: "))

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if (select == 1):
    print("The sum of ", num1 , "+", num2 , "is: ",  add(num1,num2))
    

elif (select == 2):
    print("The sum of ", num1 , "-", num2 , "is: ",  sub(num1,num2))

elif (select == 1):
    print("The sum of ", num1 , "*", num2 , "is: ", mul(num1,num2))

elif (select == 1):
    print("The sum of ", num1 , "/", num2 , "is: ",  div(num1,num2))

else:
    print("Invalid input")

