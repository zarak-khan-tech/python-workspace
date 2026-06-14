f = open("poem.txt")

content = f.read()

print(content)

if "twinkle" in content:
    print("FOUND")

else:
    print("NOT FOUND")

f.close()