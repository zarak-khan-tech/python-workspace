# # first code 
# print("khush amdeed yt we are learning python programming")

# # data types  

# # integers 

# a = 31
# b = 98
# c = 100
# print (type(a))
# print (type(b))
# print (type(c))

# # float

# d = 52.1
# e = 88.3

# print (type(d))
# print (type(e))


# # complex

# f = 65j
# g = 78j

# print (type(f))
# print (type(g))

# # strings

# h = "zk"
# i = "zarak khan"

# print (type(h))
# print (type(i))

# #boolean 

# j = True
# k = False 

# print (type(j))
# print (type(k))

# # unicode
# # unicode kisi bhi alphabet ka number malooom karnay kay liye hota hai like 

# l = "l"
# print(ord(l))

# # tho print karnay k baad the unicode of l will be 108



# # now i have to tell you that print(ord) will convert character to unicode 
# # and the print(chr) will convert unicode to character like 

# l = 108
# print(chr(l))


# # string indexing

# #like if we want indexes of any characteristics we have to know that k indexeses are starting from zero in positive like
# a = "zarak"
# print(a[4])

# # and for negative index it will start from minus 1 like 
# b = "khan"
# print(b[2],b[-2])


# # string slicings 
# a = "zarak khan coder"
# print(a[0:5:1]) # for print all name like only zarak the index of zarak is 4 but we have to write 5 for printing zarak otherwise it will be zara 

# a = "zarak khan coder"
# print(a[::]) # and this will print all the sting like zarak khan coder 

# a = "zarak khan coder"
# print(a[12:16:1]) # this will print oder only bcz of indexing 


# # type conversion 

# a = 10
# a = str(a)
# print (type(a))


# b = '89'
# b = int(b)
# print(type(b))


# # simple string 
# a = 'zarak khan'
# b = '20'
# print("hello my name is ", a ,"and my age is ", b)


# # formatted strings 
# a = 'zarak khan'
# b = '20'
# print(f"hey my name is {a} and my age is {b}")


# # input 
# age = int(input("what is your age"))
# print(age)

# #............
# name = input('what is you name')
# age = int(input('what is your age'))
# print(name, age)   



# # arthimetic operators 

# a = 65
# b = 9
# # # print(a+b) # plus 
# # # print(a-b) # minus 
# # # print(a*b) # multipy 
# # print(a/b) # devide 
# # print(a//b) # it gives with out points 
# # print(a**b) # power 
# print(a%b) # reminder


# compound assignment operators 

a = 55


# #using compound assignment operators 

# a += 50
# print( a )

# a = 50
# print( a )

# a *= 50
# print( a )

# a /= 50
# print( a )

# a //= 50
# print( a )

# a **= 50
# print( a )

# a %= 50
# print( a )



# comparison operators 
# == equals to 
# != not equals to 
# > greater than 
# < less than 
# >= greater than and equals to
# # <= less than and equals to 


# print(45==45)
# print(55!=65)
# print(98>100)
# print(44>66)
# print(54>=78)
# print(63<=31)


# here we can also compair strings through "Ascii values" and now we are telling that ascii values are basically unicodes of that variables
# string only can compair with strings 
# print (ord ( "a" ))    # for unicodes 
# print ( ord ( "b" )) 

# print ( "a " < " b ")


# logical operators 
# AND, OR, NOT 

# print(45>20 and  20==20 and 89< 100) # and means all are true 
# print(45>20 or 0==20 or 89<100)# and means all are true 
# # print (not 20==20)
# print(True and bool(0))



# Conditional statsments 
# if 
# elif 
# else 

# money = int(input("give me money :- "))
# if money == 40:
#     print("i will buy samosa ")
# elif money >= 50:
#     print ( "i will buy fritters ")
# elif money == 120:
#     print (" i will buy a burgur ")
# else:
#     print("i will have a roast ")
    

# Questions 

# number1 = int(input("plz enter you first num"))
# number2 = int(input("plz enter your second num"))
# if number1 > number2:
#     print(f"{number1} is greater is than {number2}")
# elif number2 > number1:
#     print(f"{number2} is greater is than {number1}")
# else:
#     print("the nums are same")


# Question 2



# gndr = input("plz enter your gender")
# if gndr == "male":
#     print("good morning sir")
# elif gndr == "female":
#     print("good morning madam")
# else:
#     print("good morning customs")



# Question3


# int = int(input("enter the integer"))
# if int %2 == 0:
#     print("the number is even ")
# else:
#     print("the number is odd")

# Questions 4


# char = input("enter your name:-")
# num = int(input("enter your age"))

# if num >= 18:
#     print (f"hello {char} you are a valid voter ")
# elif num == 0:
#     print ( "not in this world" )
# else:
#     print( f"hello {char} you are not a valid voter")

# Question 5 

# year = int(input("Hey enter the year : - "))
# if year%100 == 0 and year%400 == 0:
#     print("its a leap year")
# elif year%100 != 0 and year%4 == 0:
#     print("its a leap year")
# else:
#     print("its a normal year")



# Question 6 elif ladder 

# temp = int(input("enter temp in degrees"))

# if temp < 0:
#     print (" its freezing cold ")
# elif temp >= 0 and temp < 10:
#     print("its very cold")
# elif temp >= 10 and temp < 20:
#     print("its cold")
# elif temp >= 20 and temp < 30:
#     print("its pleasent")
# elif temp >= 30 and temp < 40:
#     print (" its hot")
# else:
#     print("its very hot ")
    


    #   FOR LOOPS 


# a = range (1, 20,2)
# for i in a:
#     print(i)

# for i in range(20, 80,4):
#     print(i)


# now print the tables 

# for i in range(10,101,10):
#     print(i)


# taking input for table 

# n = int(input("which table u wants to print"))
# for i in range(n,(n*11),n):
#     print(i)


# loops for  strings using indexing

# q = "king zarak khan yousafzai"
# for i in range(len(q)):
#     print(q[i])


# loops for  strings using direct method 

# a = "king is back in python"
# for i in a:
#     print(i)

# now break continue and else ones in loops 

# for i in range(1,11,1):
#     if i == 5:
#         break 
#     else:
#         print(i)


# for i in range(1,11,1):
#     if i == 5:
#         continue
#     else:
#         print(i)


# for loop questions 

# n = int(input("plz enter an integer"))
# for i in range(n):
#     print('hello world')

# n = int(input("plz enter your number"))
# for i in range(1,n+1):
#     print(i) 


# n = int(input("plz enter your number"))
# for i in range(n,0,-1):
#     print(i)


# n = int(input("plz enter your table"))

# for i in range(n,(n*11),n):
#     print(i)

# n = int(input('enter your table: '))
# for i in range(1,21):
#     print(f"{n} * {i} = {n*i}")


# n = int(input("enter a number"))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
# print(f"your sum is {sum}")


# n = int(input("enter your number:-"))
# fac = 1
# for i in range(1,n+1):
#     fac = fac * i
# print(f"your factorial is {fac}")


# n = int(input("enter your number :- "))
# even = 0 
# odd = 0

# for i in range(1,n+1):
#     if i%2 == 0:
#         even = even +i
#     else:
#         odd = odd +i
# print(f"your sum of even and odd are {even}, {odd}")


# n = int(input("which factors you want to print"))

# for i in range(1,n+1):
#     if n%i == 0:
#         print(i)


# n = int(input("enter your number:- "))
# sum = 0

# for i in range(1,n):
#     if n%i == 0:
#        sum = sum + i
# print(sum)
# if sum == n:
#     print("your number is perfect")
# else:
#     print("your number is not perfect")



# n = int(input("enter your number for checking is it prime or not:- "))
# count = 0
# for i in range(1,n+1):
#     if n%i == 0: 
#         count = count + 1 
# print(count)

# if count == 2:
#     print("your number is prime ")

# else:
#     print("your number is not prime ")


# a = "zarakkhanyousafzai"
# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]
# print(b)


# a = "naman"
# b = ""

# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]
# if b == a:
#     print("its is a pallindrome")
# else:
#     print("its not a pallindrome")


# a = "agsfgariuhaidsgi248723653465968!@#$%#$*^%$$%^^#$%^#$%^$sfhlishgiuhl38474q368&^*&^*^#*&^*^#T &*SHGDUGUTuadstf87weweugfyu"
# char = 0
# dig = 0
# spchr = 0
# for i in a:
#     if i.isalpha():
#         char += 1
#     elif i.isdigit():
#         dig += 1 
#     else:
#         spchr += 1 
# print(f"your digits are {dig}\n your alphabets are {char}\n your special characeters are {spchr}\n")
  


# WHILE LOOPS 

# a = 1
# while a <=30:
#     print(a)
#     a += 1


# a = int(input("enter your numbers:- "))

# while a > 0:
#     print(a % 10)
#     a = a // 10

# a = int(input("enter your numbers:- "))
# rev = 0
# while a > 0:
#      rev = rev*10 + a % 10
#      a = a // 10
# print(rev)


# a = int(input("enter your numbers:- "))
# copy = a
# rev = 0
# while a > 0:
#      rev = rev*10 + a % 10
#      a = a // 10
# if copy == rev:
#      print('pallindrome')
# else:
#      print("not pallindrome")




# # WHILE LOOP GAME


# import random
# num = random.randint(1,100)
# tries = 0

# while True:
#     guess = int(input("enter your guessing number between 1 and 100:- "))

#     if num == guess:
#         tries += 1
#         print(f"your guess are right you successfully guessed it in {tries} tries")
#         break
#     elif num < guess:
#         print("guess a little lower")
#         tries += 1
#     elif num > guess:
#         print("guess a little higher")
#         tries += 1
#     else:
#         print("sorry you are wrong ")






#             FUNCTIONS :-    reusable blocks of code 


# def zk():
#     print("here we are making functions with zk")
# zk()
# zk()
# zk()
# zk()
# zk()
# zk()
# zk()
# zk()


#   POSITIONAL ARGUMENT

# def sum(a,b):
#     print(f"the sum of your numbers are {a+b}")
# sum(23,43)
# sum(656,4312)
# sum(26,4393)
# sum(298,478)
# sum(4545,487)

# # KEYWORD ARGUMENT

# def intro(name,age):
#     print(f"hellow my name is {name} and my age is {age}")
# intro(age = 20 , name = "zarak")



#   DEFAULT ARGUMENT


def sum(a,b=55):
    print(f"the sum is {a+b}")
sum(12)

def sum(a,b=55):
    print(f"the sum is {a+b}")
sum(12,66)