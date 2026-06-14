# numbers = [1,2,3,4,5]
# total = 0 
# for i in numbers:
#     total = total+i
# print(total)


# p = [3,7,2,9,5]
# largest = p[0]
# for i in p:
#     if i > largest:
#         largest = i

# print(largest)


# numbers = [1,2,3,4,5,6]
# even_numbers = []

# for i in numbers:
#     if i %2 == 0:
#         even_numbers.append(i)
# print(even_numbers)

# numbers = [1,2,3,4,5,6]
# even_counts = 0
# odd_counts  = 0
# for num in numbers:
#     if num %2 == 0:
#         even_counts = even_counts + 1
#     else:
#         odd_counts = odd_counts + 1

# print("EVEN", even_counts)
# print("ODD", odd_counts)



# k = [10, 12, 14, 19, 20, 30, 25]

# largest = float('-inf')
# sec_largest = float('-inf')

# for i in k:
#     if i > largest:
#         sec_largest = largest
#         largest = i
#     elif i > sec_largest and i != largest:
#         sec_largest = i

# print("Second Largest:", sec_largest)



# numbers  = [1,2,2,3,3,4,5,6,6,7,8,8,9]

# new_list = []

# for num in numbers:
#     if num  not in new_list:
#         new_list.append(num)
# print(new_list)


# numbers = [1,2,2,3,3,3,4,4,4,4,5,6,6,6,6,7,7,7,7,7,8,8,8,8,8,9,9,9,9,9,9,9]

# max_count = 0
# most_common = None

# for num in numbers:
#     count = 0 
#     for i in numbers:
#         if i == num:
#             count = count + 1

#     if count > max_count:
#         max_count = count 
#         most_common = num 

# print (max_count, most_common)


# numbers = [1,2,3,3,3,4,4,4,5,6,7,8,9,9]

# result = []

# for num in numbers:
#     count = 0
#     for i in numbers:
#         if i == num:
#             count = count + 1
#     if count == 1:
#             result.append(num)

# print(result)


# numbers = [10,20,30,40,50]
# total = 0
# for num in numbers:
#     total += num
# average = total/len(numbers)
# result = []
# for num in numbers:
#     if num > average:
#         result.append(sum)
# print(result)



# n = 15 
# m = 7
# ans_1 = n+m
# print("addition of ", n , "and", m ,"is", ans_1)
# ans_2 = n-m
# print("Subtraction of", n , "and", m , "is", ans_2)
# ans_3 = n*m 
# print("Multiplication of", n ,"and", m , "is", ans_3)
# ans_4 = n/m
# print("Division of", n ,"and",m, "is", ans_4)
# ans_5 = n**m
# print("Power of", n , "and" , m , "is" , ans_5)
# ans_6 = n//m
# print("Floor of" , n , "and" , m , "is" , ans_6)
# ans_7 = n%m 
# print("Reminder of " , n , "and " , m , "is" , ans_7)


# # Making a calculator but simple one 

# first_num = int(input("enter your first number:"))
# second_num = int(input("enter your second number:"))
# operator = input("enter your operator:(+,-,*,/)")

# if operator == "+":
#     print(f"addition of first and second numbers are {first_num + second_num}")
# elif operator == "-":
#     print(f"subtraction of first and second numbers are {first_num - second_num}")
# elif operator == "*":
#     print(f"multiplication of first and second numbers are {first_num * second_num}")
# elif operator == "/":
#     print(f"devision of first and second numbers are {first_num / second_num}")
# else:
#     print("invalid operation")



# # TYPE CASTING
# number = input("Enter you number: ")
# new = int(number)
# print("before ", type(number))
# print("after", type(new))

# num1 = input("Enter your first number: ")
# num2 = input("Enter your second number: ")
# print("The sum of", num1, "and", num2, "is", int(num1)+int(num2))
# print("The multiplication of", num1, "and", num2, "is", int(num1)*int(num2))


# num = input("Enter your float number: ")
# float_number = float(num)
# integer = int(float_number)
# string = str(float_number)
# print("float:", type(float_number), float_number)
# print("integer:", integer)
# print("string:", string)

# age = input("Enter your age: ")
# int_age = int(age)
# print("After 5 years your age will be: ", int_age + 5)

# number = input("Enter your number: ")
# num = int(number)
# if num % 2 == 0:
#     print("This is an even number: ", num)
# else:
#     print("This is odd number: ", num)

# nm = "zarak"
# print(nm[-4:-2])

# # STRINGS ETC 


# hello  = input("Enter your string: ")
# print("string: " , hello)
# print("The length of", hello , "is", len(hello))

# a = input("Give me your input: ")
# print(len(a))
# print(a[0:3])
# print(a[-3:])

# st = input("ENter your string: ")
# print(st.upper())
# print(st.lower())


# stp = input("enter: ")
# print(stp.strip())


# z = input("Enter string:  ")
# print(z.replace(" ","-"))

# me = input("ENter your input: ")
# print(me.upper(), me.replace(" " , "-"))
# print(me.strip())
# print(me.replace(" ", "_"))

# import pyttsx3

# engine = pyttsx3.init()
# engine.say("fuck you bitch")
# engine.runAndWait


# ### LISTS AND TUPLES #### 

# numbers = [10, 20, 30, 40, 50]

# print(numbers[0])
# print(numbers[-1])


# numbers = [10, 20, 30]
# numbers.append(40)
# numbers.insert(0,5)
# print(numbers)


# numbers = [10, 20, 30, 40, 50]

# numbers.remove(30)
# numbers.pop(-1)

# print(numbers)

# numbers = [10, 20, 30, 40, 50]

# print(len(numbers))
# print(30 in numbers)


# numbers = [10, 20, 30, 40, 50]

# print(numbers[0:3])
# print(numbers[-2:])



# numbers = [10, 20, 30, 40, 50]
# numbers.reverse()
# print(numbers)

# numbers = (10, 20, 30, 40, 50)

# print(numbers[0])
# print(numbers[-1])



# ##########  DICTIONARY AND SETS ###########


# student = {
#     "name": "Zarak Khan",
#     "age": 20,
#     "marks": 99,
#     "hobbies" : "cricket"
# }

# print(student)
# print(student["name"])
# print(student["marks"])
# print(student["hobbies"])
# print(student["age"])





# student = {
#     "name": "Ali",
#     "age": 18
# }


# (student["marks"]) = 95
# (student["age"]) = 20

# print(student)




# student = {
#     "name": "zarak khan",
#     "age": 20,
#     "marks": 100,
#     "hobbies": "cricket",
#     "skills": "python",
# }

# print("Dict_Keys", student.keys())
# print("Dict_Values", student.values())






# student = {
#     "name": "zarak khan",
#     "age": 20,
#     "marks": 100,
#     "hobbies": "cricket",
#     "skills": "python",
# }


# print(student["skills"])





# student = {
#     "name": "zarak khan",
#     "age": 20,
#     "marks": 100,
#     "hobbies": "cricket",
#     "skills": "python",
# }


# student.pop("hobbies")
# print(student)




# set = {1,2,4,7,5,8,3,6,9}
# print(set)



# numbers = {10, 20, 30}
# numbers.add(40)
# numbers.remove(20)
# print(numbers)
 



# ########### IF ELIF ELSE STATMENT ########################



# a1 = int(input("Enter your 1 number: "))
# a2 = int(input("Enter your 2 number: "))
# a3 = int(input("Enter your 3 number: "))
# a4 = int(input("Enter your 4 number: "))

# if(a1>a2 and a1>a3 and a1>a4):
#     print(f"Greatest number is a1 {a1}")
    

# elif(a2>a1 and a2>a3 and a2>a4):
#     print(f"Greatest number is a2 {a2}")
    

# elif(a3>a2 and a3>a1 and a3>a4):
#     print(f"Greatest number is a3 {a3}")
    

# if(a4>a2 and a4>a3 and a4>a1):
#     print(f"Greatest number is a4 {a4}")
    





# Question no 2 


# marks1 = int(input("Enter your marks1: "))
# marks2 = int(input("Enter your marks2: "))
# marks3 = int(input("Enter your marks3: "))

# total_percentage = (100*(marks1+marks2+marks3))/300

# if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
#     print(f"you are pass {total_percentage}")
# else:
#     print(f"you are fail, try again later {total_percentage}")



# # Question no 2:


# p1 = "make alot of money"
# p2 = "buy now "
# p3 = "subscribe now "
# p4 = "click this"

# message = input("Enter your comment: ")

# if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
#     print("this comment is  a spam")

# else:
#     print("this comment is not a spam")




### Question 3 

# username = input("Enter your username:  ")

# if (len(username)<10):
#     print("Your username contain less than 10 characters: ")

# else : 
#     print("NOT ACCEPTED")


###### QUESTION no 4 

# lt = ["zarak" , "hassan", "ali" , "faizan", "shoaib"]

# name = input("Enter your name:: ")

# if (name in lt ):
#     print("your name is in the list")

# else:
#    print ("your name is not in the list")




#### Question 5

# post = input("Enter your post::::")

# if("Zarak khan".lower() in post.lower()):
#     print("THIS POST IS TALKING ABOUT ZARAK KHAN")
# else:
#     print("THIS POST IS NOT TALKING ABOUT ZARAK KHAN")





########  PRACTICE #############

# num = int(input("Enter your number: "))

# if(num>=0):
#     print("positive")
# else:
#     print("negative")




# marks = int(input("Enter your marks: "))

# if(marks < 40):
#     print("fail")

# elif(marks >= 40 and marks <= 79):
#     print("pass")

# elif(marks >= 80):
#     print("Excellent")

# else:
#     print("not a value")
    


# number = int(input("Enter your number: "))

# if(number%3 == 0 and number%5 == 0):
#     print("Your number is divisible by both ")

# elif(number%3 == 0):
#     print("only divisible by 3")

# elif(number%5 == 0):
#     print("only divisible by 5")

# else:
#     print("not divisible")



# num1 = int(input("Enter your 1st number: "))
# num2 = int(input("Enter your 2st number: "))
# num3 = int(input("Enter your 3st number: "))

# if(num1>=num2 and num1>=num3):
#     print(f"The largest Number is num1 {num1}")

# elif(num2>=num1 and num2>=num3):
#     print(f"The largest Number is num2 {num2}")

# else:
#     print(f"The largest Number is num3 {num3}")





############################



# char = "a,e,i,o,u"

# vowel = input("enter your character:  ")

# if(vowel in char):
#     print("vowel")
# else:
#     print("constant")





# vowel = input("enter your character:  ")

# if(vowel in "aeiou"):
#     print("vowel")
# else:
#     print("consonant")



#######################################################################



# number = int(input("Enter your number: "))

# if(number%2==0 and number%3==0):
#     print("Good")

# elif(number%2==0):
#     print("Nice")

# elif(number%3==0):
#     print("Okay")

# else:
#     print("Bad")



#######################################################################



############ LOOPS ##########


# n = int(input("Enter your table : "))

# for i in range(1, 11):
#     print(f"{n} X  {i}  =  {n*i}")


#######################################################################


# l = ["Zarak", "Zohaib", "Jahanzaib", "Arsalan","Bazil", "Basheer"]

# for names in l:
#     if(names.startswith("Z")):
#         print(f"hello {names}")



#######################################################################


# n = int(input("Enter your table : "))

# i = 1
# while(i<11):
#     print(f"{n} X  {i}  =  {n*i}")
#     i += 1




#######################################################################




# n = int(input("Enter your number : "))

# for i in range(2, n):
#     if (n%i==0):
#         print("Number is not prime")
#         break
# else:
#     print("Number is prime")




#######################################################################


# n = int(input("enter your fckin number: "))
# i = 1
# sum = 0 
# while(i<=n):
#     sum += i
#     i += 1
# print(sum)



#######################################################################



# n = int(input("Enter your number: "))

# product = 1

# for i in range(1, n+1):
#     product = product * i

# print(f"the factorial of {n} is {product}")


#######################################################################


# n = int(input("Enter your number: "))

# for i in range(1, n+1):
#     print(" "* (n-i), end=" ")
#     print("*"* (2*i-1), end=" ")
#     print("")



#######################################################################


# n = int(input("Enter your number: "))

# for i in range(1,n+1):
#     print("*"*i, end="" )
#     print(" ")



#######################################################################



# n = int(input("Enter your number: "))

# for i in range(1, n+1):
#     if(i == 1 or i == n):
#         print("*"*n, end="")
#     else:
#         print("*", end="")
#         print(" "*(n-2), end="")
#         print("*", end="")
#     print(" ")



#######################################################################



# n = int(input("Enter your number: "))

# for i in range(1,11):
#     print(f"{n} X {11-i} = {n*(11-i)}")


#######################################################################


# for i in range(1, 6):
#     print(i)

#######################################################################


# for i in range (5, 0, -1):
#     print(i)

#######################################################################

# total = 0
# for i in range(1,6):
#     total += i
# print("total",total)


#######################################################################

# for i in range(1,11):
#     if(i%2 == 0 ):
#         print("Even = ", i)


#######################################################################

# for i in range(1,6):
#     print("*"*i)

#######################################################################

# i = 1
# while(i<=5):
#     print(i)
#     i += 1

#######################################################################

# i = 5
# while(i>=1):
#     print(i)
#     i -= 1


#######################################################################

# i = 1
# total = 0
# while(i <= 5):
#     total += i
#     i += 1
# print("total",total)


#######################################################################


# while True :
#     num = int(input("Enter your number: "))
    
#     if num == 0:
#         break

# print("loop ended")



#######################################################################



############################ FUNCTIONS AND RECURSION ###############################


# def greatest(a, b, c):
#     if (a>b and a>c):
#         return a
#     elif (b>a and b>c):
#         return b
#     elif (c>a and c>b):
#         return c
# a = 1 
# b = 4
# c = 5

# print(greatest(a,b,c))



#######################################################################



# def f_to_c(f):
#     return 5*(f-32)/9

# f = int(input("Enter temperature: "))
# c = f_to_c(f)
# print(f"{round(c,2)} degree C")



#######################################################################



# def sum(n):
#     if (n==1):
#         return 1
#     return sum(n-1)+n
# print(sum(4))
# print(sum(5))
# print(sum(2))
# print(sum(8))
# print(sum(77))


#######################################################################



# def pattern(n):
#     if (n==0):
#         return
#     print("*" * n)
#     pattern(n-1)

# pattern(5)
# pattern(4)
# pattern(3)
# pattern(2)
# pattern(1)
# pattern(0)



#######################################################################



# def inch_to_cms(inch):
#     return inch * 2.54

# n = int(input("Enter inches: "))
# print(f"The corresponding result is {inch_to_cms(n)}")


#######################################################################


# def greet():
#     print("Hello, welcome to Python")
# greet()

#######################################################################


# def greet(name):
#     print("HEllo,", name)

# greet("Zarak khan")
# greet("Ali")
# greet("Hassan")
# greet("King khan")

#######################################################################


# def add(a,b):
#     return a + b

# print(add(45,10))


#######################################################################


# def check_even(num):
#     if(num%2 == 0):
#         return "even"
#     else:
#         return "odd"
    
# print(check_even(4))
# print(check_even(7))

#######################################################################


# def max_num(a,b):
#     if (a>b):
#         return "A is greater",a
#     else:
#         return "B is greater",b
    
# print(max_num(10,20))
# print(max_num(10,5))
# print(max_num(88,20))
# print(max_num(108,220))
# print(max_num(1000,204))


#######################################################################


# def countdown(n):
#     if (n==0):
#         return

#     print(n)
#     countdown(n-1)

# countdown(5)


#######################################################################



# def factorial(n):
#     if(n==1):
#         return 1
#     return n*factorial(n-1)

# print(factorial(2))


#######################################################################






























a = 10
b = 5

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)