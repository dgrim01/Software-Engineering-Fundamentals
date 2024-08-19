"""
Task: 
------------------
1. Add another method in the Course class that prints the head office location: Cape Town
2. Create a subclass of the Course class named OOPCourse
3. Create a constructor that initialises the following attributes and assigns these values:
    --- "description" with a value "OOP Fundamentals"
    --- "trainer" with a value "Mr Anon A. Mouse"
4. Create a method in the subclass named "trainer_details" that prints what the 
   course is about and the name of the trainer by using the description and trainer attributes.
5. Create a method in the subclass named "show_course_id" that prints the ID number of the course: #12345
6. Create an object of the subclass called course_1 and call the following methods
   contact_details
   trainer_details
   show_course_id
   These methods should all print out the correct information to the terminal

Note: this task covers single inheritance. Multiple inheritance is also possible in Python and 
we encourage you to do some research on multiple inheritance when you have finished this course.
"""
class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"
    head_office_location = "Cape Town"
# Method when called displays the course contact details
    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)
# Method when called displays the location of the head office
    def head_office_location(self):
        print("The head office location: ", self.head_office_location)

class OOP_Course(Course):
# Attributes that store the details of the course
    def __init__(self):
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"
        self.id_number = "#12345"
# Method that when called then displays what the course is about and the trainer of the course
    def trainer_details(self):
        print("The course is about: ", self.description)
        print("The trainers name is: ", self.trainer)
# Method that when called then displays the ID number of the course
    def show_class_id(self):
        print("ID number of the course: ", self.id_number)

# Creates an instance of the subclass called 'OOP_Fundamentals'
course_1 = OOP_Course()
# Calls methods from the class ' Course' and subclass 'OOP_Fundamentals'
course_1.contact_details()
course_1.trainer_details()
course_1.show_class_id()

