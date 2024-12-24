print("welcome to quiz game")
print()
ready = input("Do you want to play: ")
print()
if ready.lower() != "yes":
    quit()

score = 0
answer = input("What is cat? ")
if answer.lower() == "cat":
    print("Correct")
    score += 1
    print()
else:
    print("Incorrect")
    print()

answer = input("What is dog? ") 
if answer.lower() == "dog":
    print("Correct")
    score += 1
    print()
else:
    print("Incorrect")
    print()

print("your total score is", score)
