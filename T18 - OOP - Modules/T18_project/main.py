# main.py
from task_model import Task
from task_model import User
from task_controller import TaskController


def menu():
    """
    This function called Menu serves as an interface for the user.

    It displays to the user the options that are avaiable with a corresponding
    number. The options include creating, reading, updating and deleting a
    task.
    """
    print("Welcome to the Task Manager Menu")
    print("1. Option 1: Create Task")
    print("2. Option 2: Read Task")
    print("3. Option 3: Update Task")
    print("4. Option 4: Delete Task")
    print("\nPlease chose an option (1-4):", end=" ")


def main(task_controller):
    """
    This function called main allows the user to input there option,
    for it then to be called upon and executed.

    This includes 1: creating, 2: reading, 3: updating and 4: deleting a
    task.
    """
    while True:
        menu()
        choice = input().strip()

        if choice == '1':
            task_id = int(input("Enter task ID: "))
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            status_id = int(input("Enter status ID: "))
            new_task = TaskController.create_task(task_id, title, description,
                                                  status_id)
            print(f"Created task: {new_task}")

        elif choice == '2':
            task_id = int(input("Enter task ID to read: "))
            task = TaskController.get_task(task_id, 'tasks')
            print(f"Task: {task}")

        elif choice == '3':
            task_id = int(input("Enter task ID to update: "))
            updated_title = input("Enter updated task title: ")
            updated_description = input("Enter updated task description: ")
            updated_task = TaskController.update_task(task_id, updated_title,
                                                      updated_description,
                                                      'tasks')
            print(f"Updated task: {updated_task}")

        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            TaskController.delete_task(task_id, 'tasks')
            print("Task deleted.")
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    # Initialize Models, Controllers
    task_model = Task("task_id", "title", "description", "status_id")
    user_model = User("user_id", "username", "password", "profile_id")
    task_controller = TaskController()
    main(task_controller)
