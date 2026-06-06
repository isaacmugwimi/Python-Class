import random


secret = random.randint(1,2)
while True:
    guess = int(input("Guess: "))
    if guess ==secret:
        print("Correct guess: ", guess)
        break
    else:
        print("Wrong guess: ",guess)
        print("The correct number was: ", secret)
        # Generating a new number
        secret =random.randint(1,2)