import random
top_of_range = input("Enter the number: ")
print()
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Plase type a number larger than 0 next time")
        quit()

else:
    print("please type a number next time.")
    quit()

random_number = random.randint(0,top_of_range)
while True:
    guess_number = input("Enter your gussed number: ")
    if guess_number.isdigit():
        guess_number = int(guess_number)
    else:
        print("please type a number next time.")
        continue

    if guess_number == random_number:
        print("You got it :)")
        break
    else:
        print("you got it wrong!")