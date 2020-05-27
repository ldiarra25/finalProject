import random

rolling = True
print("Welcome")
while rolling:
    print("You got",random.randint(1,6))
    print("Do you want to roll the dice? Y/N")
    rolling = "Y" in input()
else:
    rolling = False
    print("Thanks for playing")
    rolling = "N" in input()