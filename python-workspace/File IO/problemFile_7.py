with open ("log.txt") as f:
    lines = f.readlines()

lineNo = 1
for line in lines:
    if("python" in line):
        print(f"python is present in line no {lineNo}")
        break
    lineNo += 1
    
else:
    print("no python is not present")