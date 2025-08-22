# 📋 To-Do List Manager (Python Project)

## 🔹 Overview
This is a *simple console-based To-Do List Manager* built in Python.
It allows the user to:
- Add new tasks
- View all tasks
- Remove tasks
- Exit the program

The project uses *Python basics* like loops, lists, functions, and conditionals, making it great for beginners
## 🔹 Features
1. *Add Task* → Enter a task and store it in a list.
2. *View Tasks* → Display all tasks with numbering.
3. *Remove Task* → Delete a task by choosing its number.
4. *Exit* → Close the program.
## 🔹 Code Explanation
- **List (tasks)** → Stores all tasks.
- **Function (show_tasks)** → Displays tasks using enumerate (for numbering).
- *While Loop* → Keeps program running until user chooses Exit.
- *If-Elif-Else* → Handles different menu options.
- *Input Handling* → Takes user choice and task details.
## 🔹 Example Run (Output)
===== TO-DO LIST MANAGER =====
1. Add Task
2. View Tasks
3. Remove Task
4. Exit
Enter your choice (1-4): 1
Enter a new task: Complete Python project
Task added successfully ✅
===== TO-DO LIST MANAGER =====
1. Add Task
2. View Tasks
3. Remove Task
4. Exit
Enter your choice (1-4): 2
--- Your Tasks ---
1. Complete Python project
If you remove a task:
--- Your Tasks ---
1. Complete Python project
Enter task number to remove: 1
Removed task: Complete Python project
## 🔹 Limitations
- Tasks are *not saved permanently* (lost when program exits).
- No option to *edit tasks*.
- Works only for *one user at a time*.
## 🔹 Future Improvements
- Save tasks to a *file/database* so they remain after closing.
- Add an *edit task* option.
- Add *deadlines and priorities*.
- Create a *GUI version* using Tkinter or PyQt.

    f.write(readme_content)

print("✅ README.md file created successfully!")
