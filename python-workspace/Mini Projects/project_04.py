# To-Do LIST 

tasks = []

while True:
    print("1. Add Task ")
    print("2. Show Task ")
    print("3. Exit ")

    choise = input("Enter your Choise: ")

    if choise == '1':
        task = input("Enter your Task: ")
        tasks.append(task)

    elif choise == '2':
        print("task")

    elif choise == '3':
        break

    else:
        print("Invalid Choise")