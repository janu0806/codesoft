tasks = []

while True:
    print("\n--- To-Do List ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if not tasks:
            print("No tasks yet.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")
    
    elif choice == "2":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")
            try:
                index = int(input("Enter task number to remove: ")) - 1
                if 0 <= index < len(tasks):
                    tasks.pop(index)
                    print("Task removed.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")
    
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")