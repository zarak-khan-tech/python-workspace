# Number Guessing game

import random
secret = random.randint(1,10)

attempts = 0
 
while True:
    guess = int(input("Enter your Guessing Number: "))
    attempts += 1

    if (guess > secret):
        print("Too High")

    elif (guess < secret):
        print("Too Low")

    else:
        print("You Win!!!")
        print("Attempts:", attempts)
        break