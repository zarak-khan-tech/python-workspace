a = input("Enter your message here: ")

with open ("msg.txt", "a") as f:
    f.write(a+ "\n")

print("Message saved successfully")