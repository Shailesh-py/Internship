def display_menu():
    print("To-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")


def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list[task] = False
    print("Task added successfully!")


def view_tasks(todo_list):
    if not todo_list:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for index, task in enumerate(todo_list, start=1):
            status = "Completed" if todo_list[task] else "Pending"
            print(f"{index}. {task} - {status}")


def mark_completed(todo_list):
    view_tasks(todo_list)
    task_index = int(input("Enter the index of the task to mark as completed: ")) - 1
    tasks = list(todo_list.keys())
    if 0 <= task_index < len(tasks):
        task = tasks[task_index]
        todo_list[task] = True
        print(f"Task '{task}' marked as completed.")
    else:
        print("Invalid task index.")


def delete_task(todo_list):
    view_tasks(todo_list)
    task_index = int(input("Enter the index of the task to delete: ")) - 1
    tasks = list(todo_list.keys())
    if 0 <= task_index < len(tasks):
        task = tasks[task_index]
        del todo_list[task]
        print(f"Task '{task}' deleted successfully.")
    else:
        print("Invalid task index.")


def main():
    todo_list = {}
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            view_tasks(todo_list)
        elif choice == '3':
            mark_completed(todo_list)
        elif choice == '4':
            delete_task(todo_list)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
