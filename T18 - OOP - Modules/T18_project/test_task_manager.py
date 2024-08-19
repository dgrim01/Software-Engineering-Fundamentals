import unittest
from task_controller import TaskController


class TestTaskController(unittest.TestCase):

    def setUp(self):
        """Arrange: Set up the test environment"""
        self.controller = TaskController()
        self.controller.file_name = "test_tasks.txt"

    def test_create_task(self):
        """Test creating a new task"""
        # Arrange
        new_task = self.controller.create_task('1', 'Task1', 'Description1',
                                               'Status1')
        # Assert
        self.assertEqual(new_task.task_id, '1')
        self.assertEqual(new_task.description, 'Description1')
        self.assertEqual(new_task.title, 'Task1')

    def test_delete_task(self):
        """Test deleting a task"""
        # Arrange
        tasks = [
            {"task_id": 1, "title": "Task 1", "description": "Description 1"},
            {"task_id": 2, "title": "Task 2", "description": "Description 2"},
            {"task_id": 3, "title": "Task 3", "description": "Description 3"}
        ]
        task_id_to_find = 2
        expected_task = {"task_id": 2, "title": "Task 2",
                         "description": "Description 2"}

        # Act
        actual_task = TaskController.delete_task(task_id_to_find, tasks)

        # Assert
        self.assertNotEqual(actual_task, expected_task)

    def test_update_task(self):
        """Test updating a task with a valid task ID"""
        # Arrange
        tasks = [{"title": "Task 1", "description": "Description 1"},
                 {"title": "Task 2", "description": "Description 2"}]
        task_id = 0
        updated_title = "Updated Task 1"
        updated_description = "Updated Description 1"
        # Act
        TaskController.update_task(task_id, updated_title,
                                   updated_description, tasks)
        # Assert
        self.assertEqual(tasks[task_id]["title"], updated_title)
        self.assertEqual(tasks[task_id]["description"], updated_description)

    def test_get_task(self):
        """Test retrieving a single task"""
        # Arrange
        tasks = [
            {"task_id": 1, "title": "Task 1", "description": "Description 1"},
            {"task_id": 2, "title": "Task 2", "description": "Description 2"},
            {"task_id": 3, "title": "Task 3", "description": "Description 3"}
        ]
        task_id_to_find = 2
        expected_task = {"task_id": 2, "description": "Task 2"}

        # Act
        actual_task = TaskController.get_task(task_id_to_find, tasks)

        # Assert
        self.assertEqual(actual_task, expected_task)


if __name__ == '__main__':
    unittest.main()
