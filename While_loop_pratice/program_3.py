# Guessing Game
import random
user_input = input("Do you want to play! ").lower()

if user_input != 'yes':
     print("Try to type 'yes' in input box if you want to play....")
     quit()
else:
     gusses_number = int(input("Enter the limit of numbers between you want to gusse number: "))
     random_number = random.randint(1,gusses_number)
     while True:
          user_input_2 = int(input("Enter the gussing number: "))
          if user_input_2==random_number:
               print("Your gusses is correct!")
               break
          
          elif  random_number < user_input_2 :
               print("your number is great:")

          elif random_number > user_input_2 :
               print("your number is less:")

          else:
               print("Try again!")
          