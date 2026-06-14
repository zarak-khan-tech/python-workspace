a = input("Enter your message here: ")

with open ("msg.txt", "w") as f:
    f.write(a)

print("Message saved successfully")