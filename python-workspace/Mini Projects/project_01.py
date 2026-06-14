""" 1 sanke 
-1 water 
0 gun """


import random

computer = random.choice( [-1, 0, 1] )
yourstr = input("Enter your choice: ")
yourDict = {"s": 1, "w":-1, "g":0}
reverseDict = {1 : "snake", -1 : "water", 0 : "gun" }

you = yourDict[yourstr]

print(f"Computer Choose {reverseDict[computer]}\n You choose {reverseDict[you]}")
if computer == you:
    print(" ITS A DRAW ")

else:
    if (computer == -1 and you == 1):
        print("You win!")
    elif (computer == -1 and you == 0):
        print("You lose!")
    elif (computer == 1 and you == -1):
        print("You lose!")
    elif (computer == 1 and you == 0):
        print("You win!")
    elif (computer == 0 and you == -1):
        print("You Win!")
    elif (computer == 0 and you == 1):
        print("You Lose!")
    else:
        print("Something went wrong!")