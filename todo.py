print("""
---------
TODO LIST
---------
""")

tasks = []
def display_menu():
    print("TODO TASK LIST")
    print("\n Add Task")
    print("\n Description")
    print("\n View Task")
    print("\n Mark as Completed")
    print("\nQuit")

def add_task():
    description = input("Enter Your Description")
    due_date = input("Enter due date (YYYY-MM-DD):")
    task = {"Description": description, "Due_date": due_date, "completed": False }
    tasks.append(task)
    print("Task Added Succesfully")

def view_task():
    if not tasks:
        print("There is no task")
    else:
        print("\nTask List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

while True:
    display_menu()
    choice = input("Enter Your Choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        print("Good by")
        break
    else:
        print("Invalid Choice, Please Enter a Valid Choice")






