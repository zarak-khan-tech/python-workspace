with open ("msg.txt", "r") as f:
    content = f.read()
words = content.split()
print("Total words: ", (len(words)))