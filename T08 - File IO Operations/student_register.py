# Request user to enter the number of students they want to register
max_num_students = int(input("How many students are registering: "))

# stores the number of users that have been registered
students_registered = 0


# Opens the file 'output.txt'
with open('output.txt', 'a+') as f:
    # each time the loop runs it requests the user to enter a student ID
    for student in range(max_num_students):

        # requests user to enter student number
        user_input = input(f"Enter the student number for student {students_registered + 1}: ")

        # if the users input is blank or a string it the prompt the user to enter a valid student number
        # as either input would be invalid
        while user_input.strip() == '' or not user_input.strip().isdigit():
            print("Error: Please enter a valid student number.")
            user_input = input(f"Enter the student number for student {students_registered + 1}: ")

        # adds to the counter of the number of students registered
        students_registered += 1

        # Write each student ID number to the text file called reg_form.txt
        
        f.write(user_input + " .................\n")

# lets the user know when all students have been registered
if students_registered == max_num_students:
    print("All Students have now been registered.")
