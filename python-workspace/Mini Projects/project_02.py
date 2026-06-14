""" Making a simple calculator """

num1 = int(input("Enter your First number: "))
opt = input("Enter your operator (+,-,*,/): ")
num2 = int(input("Enter your Second number: "))

if (opt == "+"):
    print(num1+num2)
elif (opt == "-"):
    print(num1-num2)
elif (opt == "*"):
    print(num1*num2)
elif (opt == "/"):
    if (num2 == 0):
        print("Number is Not Divided")
    else:
        print(num1/num2)
else:
    print("Error!!!")