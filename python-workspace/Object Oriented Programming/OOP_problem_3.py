class DEMO():
    a = 4

o = DEMO()
print(o.a) # class attribute will run
o.a = 0 # object attribute is set
print(o.a) # now here it will run object attribute 
print(DEMO.a) # and class attribute will not change 


# it does change the class attribute
