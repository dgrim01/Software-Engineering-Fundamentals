# provides access to the module that contains the function to exit the application
import sys

class Email:

    # stores the emails in a list called inbox
    inbox = []

    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address # the email address of the sender
        self.subject_line = subject_line # the subject line of the email
        self.email_content = email_content # the contents of the email
        self.has_been_read = False
        Email.inbox.append(self) #adds email object to the inbox list
        

    # Call this method when an email has been read, setting the variable called has_been_read to true indicatates the email has been read.
    def mark_as_read(self):

        self.has_been_read = True

    # In this method cls refers to the email class itself. 
    @classmethod
    def populate_inbox(cls, email_address, subject_line, email_content):
        
        # stores each element of the email as variable called email
        email = cls(email_address, subject_line, email_content)

        return email
    
    # a function that loops through the inbox and prints each emails subject_line and its corresponding index number
    @classmethod 
    def list_emails(cls):
        for idx, email in enumerate(cls.inbox):
            print(f"{idx} {email.subject_line}")

    @classmethod
    def read_email(cls):
        # if the user enters a valid index it then searches the for corresponding email;
        # it provides the user with sender of the email, the subject and the content of the email.
        try:
            selected_email = int(input("Enter the index of the email you want to read: "))
            email = cls.inbox[selected_email]
            print(f"From: {email.email_address}\nSubject: {email.subject_line}\nContent: {email.email_content}")
            print("Email has been marked as read")
            email.mark_as_read()
        # if the user inputs a value that cannot be converted to an integer causing a value error or an index out of range causing a index error
        # then prints the following statement "Invalid index, email not found."
        except (ValueError, IndexError): 
            print("Invalid index, email not found.")

# when this function is called, it terminates the program
def Quit_Application():
    print("Quitting the email application...")
    sys.exit()

# instances of the email that would be stored in the inbox
email_1 = Email.populate_inbox("dgrimley2001@gmail.com", "Welcome To HyperionDev", "Welcome and Happy Coding")
email_2 = Email.populate_inbox("cogrammar@email.com", "Great work on the bootcamp", "Good job 10/10")
email_3= Email.populate_inbox("demonfort@university.com", "Greetings new student", "Hello Dominic")

# allows the user to choose whether they'd like to from Read email, View Unread emails and Quit Application
def email_menu():
    while True:
        user_choice = input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: ''')
        if user_choice == '1':
            # calls the method to allow the user to select the email they would like it read
            Email.read_email()
        elif user_choice == '2':
            # calls the method to display the list of emails
            Email.list_emails()
        elif user_choice == '3':
            # calls the function to quit the application
            Quit_Application()
            break
        else:
            # prints the statement that tells the user the option they selected
            # does not exist and prompts them to select from the available options.
            print("Option does not exist. Please enter 1, 2 or 3")

#calls the function to start the application
email_menu()

