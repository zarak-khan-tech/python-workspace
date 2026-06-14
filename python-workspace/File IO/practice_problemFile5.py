old = input("Enter your old word you want to remove from here: ")
new = input("Enter your new word you want to add here: ")

with open("msg.txt", "r") as f:
    content = f.read()

contentNew = content.replace(old, new) 

with open("msg.txt", "w") as f:
    f.write(contentNew)