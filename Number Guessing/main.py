import random

Top = print("Type the max number to guess: ")
if Top.isdigit():
    Top = int(Top)
    if Top <= 0:
        print("Type a number larget than 0 :)")
        quit()
else:
    print("Type a digit next time")
    quit()

num = random.randrange(0, Top)

while True:
    guess = input("Make a Guess: ")
    if guess.isdigit():
        guess = int(guess)
        if guess == num:
            print("You got it!")
            break
        else:
            print("Try again")
    else:
        print("Type a digit next time")
        continue
    