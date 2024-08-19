"""
Task Controller Module

Defines TaskController module for managing user requests in the task system.

"""

from task_model import Task
from task_model import Status


class TaskController:
    """
    TaskController class for managing tasks.

    This class provides methods to create, read, update, and delete for tasks
    within a task manager.

    """

    def __init__(self, task_model):
        """
        This method allows other methods to be able to use the text file as an
        argument when required.

        Arg:
        - file_name stores the text file to be used as an argument.
        - task_id(int): Represents the unique identifier for the task.
        - title(string): Provides precise description of what the task is.
        - description(string): Provides a more indepth description of the task.
        - status_id(int): Is the forgein key to link the task with progress of
            the task itself.
        """
        self.file_name = "tasks.txt"
        self.task_model = task_model

    def read_tasks(file_name):
        """
        Reads the list of tasks within the file

        Args:
        - file_name: this allows the method to be able to write to the
            text file.
        """
        tasks = []
        with open(file_name, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 4:  # Empty line indicates end of task details
                    task_id, title, description, status_id = parts
                    tasks.append(Task(task_id, title, description, status_id))
        return tasks

    def write_to_file(self, tasks):
        """
        Writes task to the file

        Args:
        - tasks(dict): stores the tasks to be able to be written to the text
        file.
        """
        with open(self.file_name, "a", encoding='utf-8') as file:
            for task in tasks:
                file.write(
                    f"{task.task_id}, {task.title}, "
                    f"{task.description},{task.status_id}\n"
                )

    def create_task(self, task_id, title, description, status_id):
        """
        Creates new task and writes it to the end of the list of existing
        tasks.

        Args:
        - task_id(int): Represents the unique identifier for the task.
        - title(string): Provides precise description of what the task is.
        - description(string): Provides a more indepth description of the task.
        - status_id(int): Is the forgein key to link the task with progress of
            the task itself.
        """
        try:
            new_task = Task(task_id, title, description, status_id)
            return new_task
        except ValueError:
            print("Invalid input. Please enter correct values")

    def delete_task(task_id, tasks):
        """
        Deletes task from the list of stored tasks

        Args:
        - task_id(int): takes task_id from the task model to be able to
        retrieve a specific task.
        - tasks: stores the list of tasks it needs to retrieve the task from
        matching the specific task_id.
        """
        try:
            for task in tasks:
                # Check if the current task's id matches the given task_id
                if task.pop("task_id") == task_id:
                    # If a task is found with the matching task_id,
                    # it deletes the task
                    return True
            # If a matching task_id is not found it returns nothing
            return None
        except ValueError:
            print("Invalid input. Please enter correct values")

    def update_task(task_id, updated_title, updated_description, tasks):
        """
        Updates a task from the list of stored tasks

        Args:
        - task_id: Used to identify which task is to be updated
        - updated_title: used to take in the new title provided by the user if
        updated.
        - updated_description: used to take in the new description provided by
        the user if updated.
        - tasks: stores the list of tasks it needs to retrieve the task from
        matching the specific task_id to then be updated by the user.
        """
        try:
            if 0 <= task_id < len(tasks):
                tasks[task_id]["title"] = updated_title
                tasks[task_id]["description"] = updated_description
        except ValueError:
            print("Invalid input. Please enter correct values")

    def get_task(task_id, tasks):
        """
        Retrieves a task from the list of stored tasks by its id

        Args:
        - task_id(int): takes task_id from the task model to be able to
        retrieve a specific task.
        - tasks: stores the list of tasks it needs to retrieve the task from
        matching the specific task_id.
        """
        try:
            for task in tasks:
                # Check if the current task's id matches the given task_id
                if task.get("task_id") == task_id:
                    # If a task is found with the matching task_id,
                    # it returns the task
                    return task
            # If a matching task_id is not found it returns nothing
            return None
        except ValueError:
            print("Invalid input. Please enter correct values")


class StatusController:
    """
    StatusController class for managing status of tasks.

    This class provides methods to create, read, update, and delete for
    statuses within a task manager.

    Args:
        - status_id(int): Represents the unique identifier for the Status.
        - mark_as_complete(string): Provides a way to show whether the task is
        complete or not.
        - assigned_to(string): Provides the name of the user completing the
        task.
        - last_modified(string): Provides a date of when the task was either
        created or details where added or changed to assist the task in
        meeting current requirments.
    """
    def __init__(self):
        self.file_name = "statuses.txt"

    def read_status_from_file(self):
        """ Reads the list of task status within the file"""
        status_list = []
        with open(self.file_name, "r", encoding='utf-8') as file:
            for line in file:
                status_id, mark_as_complete, assigned_to, last_modified = (
                    line.strip().split(",")
                )
                status = Status(status_id, mark_as_complete, assigned_to,
                                last_modified)
                status_list.append(status)
        return status_list

    def write_status_to_file(self, status_list):
        """
        Writes status to the file
        """
        with open(self.file_name, "w", encoding='utf-8') as file:
            for status in status_list:
                file.write(
                    f"{status.status_id}, {status.mark_as_complete}, "
                    f"{status.description},{status.last_modified}\n"
                )

    def create_status(self, status_id, mark_as_complete, assigned_to,
                      last_modified):
        """
        Creates new task and writes it to the end of the list of existing
        tasks.

        Args:
        - status_id(int): Represents the unique identifier for the Status.
        - mark_as_complete(string): Provides a way to show whether the task is
        complete or not.
        - assigned_to(string): Provides the name of the user completing the
        task.
        - last_modified(string): Provides a date of when the task was either
        created or details where added or changed to assist the task in
        meeting current requirments.
        """
        new_status = Status(status_id, mark_as_complete, assigned_to,
                            last_modified)
        status_list = self.read_status_from_file()
        status_list.append(new_status)
        self.write_status_to_file(status_list)
        return new_status

    def get_status(self, status_id):
        """Retrieves all the tasks from the list of stored tasks"""
        status_list = self.read_status_from_file()
        for status in status_list:
            if status.status_id == status_id:
                return status
        return None

    def update_status(
        self,
        status_id,
        updated_mark_as_complete=None,
        updated_assigned_to=None,
        update_last_modified=None,
    ):
        """
        Updates a status from the stored status_list

        Args:
        - status_id(int): Represents the unique identifier for the Status.
        - updated_mark_as_complete(string): Provides a way to mark the task as
        complete once completed.
        - updated_assigned_to(string): Provides the name of the user
        completing the task if handed over to another user.
        - updated_last_modified(string): if the task is modified they are able
        to provide the date they made the updated.
        """
        status_list = self.read_status_from_file()
        for status in status_list:
            if status.status_id == status_id:
                if updated_mark_as_complete is not None:
                    status.mark_as_complete = updated_mark_as_complete
                if updated_assigned_to is not None:
                    status.assigned_to = updated_assigned_to
                if update_last_modified is not None:
                    status.last_modified = update_last_modified
                self.write_status_to_file(status_list)
                return True  # Task updated successfully
        return False  # Task not found

    def get_status_list(self):
        """Retrieves all the status from the stored status_list"""
        return self.read_status_from_file()

    def delete_status(self, status_id):
        """
        Deletes task from the list of stored tasks
        Args:
        - status_id(int): Represents the unique identifier for the Status.
        """
        status_list = self.read_status_from_file()
        for status in status_list:
            if status.status_id == status_id:
                status_list.remove(status)
                self.write_status_to_file(status_list)
                return True  # Task deleted successfully
        return False  # Task not found
