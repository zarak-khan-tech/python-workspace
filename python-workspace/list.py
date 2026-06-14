# LISTS 
a = [14,15,55,16,90]
print(a)

# LIST TRAVERSING 
# 1st Method
a = [25,26,27,28,29]
for i in range(len(a)):
    print(a[i])

# 2nd Method

a = [45,56,78,89]
for i in a:
    print(i)

# we are using append method now which is used to add anything at the last like 

fruits = ["apple" , "mango" , "banana"]
fruits.append("watermelon")
fruits.append("orange")
print(fruits)

# WE are using insert method now which is used to insert anything in any place using indexing

nums = [10,50,30]
nums.insert(1,20)
print(nums)

# QUESTIONS 

a = [-55,32,48,-98,-85,77,-555,-888,7887878]

print("positive values are ")
for i in a:
    if i >= 0:
        print(i)
print("negative values are ")
for i in a:
    if i < 0:
        print(i)


# 2nd Question

print("the sum of L is ")
l = [10,25,65,45]
sum = 0
for i in l:
    sum = sum + 1
print(sum/len(l))


# 3rd Question


z = [3,33,5,41,87,98,52,89,65,65,32,646,44,742,744,5,9,1,2,789]

largest = z[0]
index = 0

for i in range(len(z)):
    if z[i] > largest:
        largest = z[i]
        index = i
print(f"your largest number is {largest} and index is {index}")



# 4th Question

k = [10,12,14,19,20,30,25]

largest = k[0]
sec_largest = k[0]

for i in k:
    if i > largest:
        sec_largest = largest
        largest = i
    elif i > sec_largest:
        sec_largest = i


print(sec_largest,largest)



# 5th Question 

t = [10,20,30,40,50,60,70]

for i in range(len(t)-1):
    if t[i] < t[i+1]:
        continue
    else:
        print("your list is not sorted")
else:
    print("your list is sorted")

    


