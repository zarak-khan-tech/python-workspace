# first code and comments 
# \n is used for print the code after \n second line

print("hey i am a good boy \n and i am 20 years old student")


# \" this is used and working as a " in this like 
print("hey my name is \"zarak khan \" and my hobbie is coding") # that will print zarak khan in a "" 


# Here we can also add multiple values in same code 
# and we can use ~ this funtion for seperation of multiple fuctions 
# here when we add end="anything and \n " this will also print 008 and then new line and second code will execute
print("king" , 5 , 3, sep="~", end="008\n")
print("zarak khan")

# TYPE CASTING IN PYTHON
# EXPLICIT TYPECASTING 
str = "55"
num = 10
str_num = int(str)
sum = (str_num + num)
print("The sum is :", sum)

# IMPLICIT TYPECASTING
a = 7
print(a)
print(type(a))

b = 8.7
print(b)
print(type(b))

c = "zk"
print(c)
print(type(c))


# TAKING USER INPUTS

a = input("Enter your first operator: ")
b = input("Enter your second operator: ")
print(a + b)
print(int(a) + int(b))
