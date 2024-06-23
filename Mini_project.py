def display_menu():
    print("\nWelcome to the To-Do List App!")
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' is added to the list.")

def view_tasks(tasks):
    if not tasks:
        print("The task list is empty.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def mark_task_complete(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task is completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1] += " [X]"
            print(f"Task {task_num} marked as complete.")
        else:
            print("Invalid input.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the number of the task to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted_task = tasks.pop(task_num - 1)
            print(f"Task '{deleted_task}' deleted from the list.")
        else:
            print("Invalid input.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        try:
            choice = int(input("Choose an option(1,2,3,4,5): "))
            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                view_tasks(tasks)
            elif choice == 3:
                mark_task_complete(tasks)
            elif choice == 4:
                delete_task(tasks)
            elif choice == 5:
                print("Quit the application. Bye!")
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
