"""
Task Model Module:
Defines module for managing tasks, statuses, users,
and user profiles within the task management system.
"""


class Task:
    """
    Represents a task within the task management system

    Args:
    - task_id(int): Represents the unique identifier for the task.
    - title(string): Provides precise description of what the task is.
    - description(string): Provides a more indepth description of the task.
    - status_id(int): Is the forgein key to link the task with progress of
        the task itself.
    """
    def __init__(self, task_id, title, description, status_id):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status_id = status_id

    def __repr__(self):
        return ("Task(task_id='{self.task_id}', "
                "title='{self.title}', "
                "description='{self.description}', "
                "status_id='{self.status_id}')")


class Status:
    """
    Represents a tasks status within the task management system

    Args:
    - status_id(int): Represents the unique identifier for the Status.
    - mark_as_complete(string): Provides a way to show whether the task is
        complete or not.
    - assigned_to(string): Provides the name of the user completing the task.
    - description(string): Provides a date of when the task was either created
        or details where added or changed to assist the task in meeting current
        requirments.
    """
    def __init__(self, status_id, mark_as_complete, assigned_to,
                 last_modified):
        self.status_id = status_id
        self.mark_as_complete = mark_as_complete
        self.assigned_to = assigned_to
        self.last_modified = last_modified


class User:
    """
    Represents a user within the task management system

    Args:
    - user_id(int): Represents the unique identifier for the user.
    - username(string): Provides a way to uniquely identify a user as it is
        possible for two or more people to have the samename.
    - password(string): Provides a way to authorise a user accessing the system
        or inpersonating a user of the system.
    - profile_id(int): Forgein key that links the user with there profile which
        provides information about the user that is not required for actively
        using the system.
    """
    def __init__(self, user_id, username, password, profile_id):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.profile_id = profile_id

    @classmethod
    def create_user(cls, user_id, username, password):
        # Instance of a new user
        new_user = cls(user_id, username, password)
        return new_user

    @classmethod
    def get_user(cls, user_id):
        return user_id

    def update_user(self, username=None, password=None, user_profile=None):
        if username:
            self.username = username
        if password:
            self.password = password
        if user_profile:
            self.user_profile = user_profile

    def delete(self):
        # Here you would typically delete the user from the database
        pass


class UserProfile:
    """
    Represents a user's profile within the task management system

    Args:
    - profile_id(int): Represents the unique identifier for UserProfile.
    - user_type(string): Provides what type of user they are; for example your
        regular user which would be just user or admin being a user that has
        administrative rights/access to the system.
    - first_name(string): The first name of the user
    - last_name(string): The surname of the user.
    """
    def __init__(self, profile_id, user_type, first_name, last_name):
        self.profile_id = profile_id
        self.user_type = user_type
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def create_user_profile(cls, profile_id, user_type, first_name, last_name):
        """
        Allows the user to creat a userprofile which provides more information
        about that links to the user profile
        """
        # Instance of a new user
        new_user = cls(profile_id, user_type, first_name, last_name)
        return new_user

    @classmethod
    def get_user_profile(cls, profile_id):
        """
        Allows the user to be able to retrieve and read the user profile
        """
        # Returns the intance of an existing user profile
        return profile_id

    def update_user(self, user_type=None, first_name=None,
                    last_name=None):
        """
        Allows the user to be able to edit any information about the user which
        may have been previously incorrect.
        """
        if user_type:
            self.user_type = user_type
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name

    def delete(self):
        # Here you would typically delete the user profile from the database
        pass
