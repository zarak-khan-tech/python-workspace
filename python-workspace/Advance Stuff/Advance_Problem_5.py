n = int(input("Enter your number: "))

table = [n*i for i in range(1,11)]
with open("2.txt", "a") as f:
    f.write(f"The Table of {n}: {str(2)} \n")