tasks = []
def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print("Task added to the to-do list")

def display_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):# to keep count of no of loops
            print(f"{i}. {task}")
while True:
    print("\nTo-Do List Program:")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Quit")
    
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        display_tasks()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
