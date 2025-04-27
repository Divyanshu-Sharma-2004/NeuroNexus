tasks = []

def show_tasks():
    if not tasks:
        print("\n No task in your To-Do List.")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, 1):
            status = "Done" if task['completed'] else "Not Done"
            print(f"{idx}.{task['title']}[{status}]")

def add_task():
    title = input("\nEnter the task title : ").strip()
    task = {'title':title,'completed':False}
    tasks.append(task)
    print("\nTask added succesfully")

def update_task():
    show_tasks()
    if tasks:
        index = int(input("\nEnter the task number to update : ")) - 1
        if 0 <= index < len(tasks):
            new_title = input("\nEnter the new task title : ").strip()
            tasks[index]['title'] = new_title
            print("\nTask Updated successfully")
        else:
            print("\nInvalid task number")

def mark_completed():
    show_tasks()
    if tasks:
        index = int(input("\nEnter the task number to mark as completed: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]['completed'] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

def delete_task():
    show_tasks()
    if tasks:
        index = int(input("\nEnter the task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Task '{removed_task['title']}' deleted successfully!")
        else:
            print("Invalid task number.")

def main():
    """Main function to run the to-do list application."""
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Delete Task")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            mark_completed()
        elif choice == '5':
            delete_task()
        elif choice == '6':
            print("\nThank you for using the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()