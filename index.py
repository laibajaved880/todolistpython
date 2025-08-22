tasks = []

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("\n--- Your Tasks ---")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

while True:
    print("\n===== TO-DO LIST MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added successfully ✅")

    elif choice == "2":
        show_tasks()

    elif choice == "3":
        show_tasks()
        if tasks:
            num = int(input("Enter task number to remove: "))
            if 1 <= num <= len(tasks):
                removed = tasks.pop(num-1)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number ❌")

    elif choice == "4":
        print("Goodbye! 👋")
        break

    else:
        print("Invalid choice! Please select 1–4.")