while True:
    # Requests user to enter a number
    user_input = input("Enter a number: ")

    # Checks if the number is -1
    if user_input == "-1":
        print("loop ended.")
        break
    else:
        #converts the users input from string to an integer
        user_num = int(user_input)
        total = user_num #started a total as the first number has been added
        count = 1 #as the user has already inputed a number the count starts at 1

        while True:
            user_input = input("Enter another number: ")
            if user_input == "-1": #if the user inputs -1 it breaks the loop to be able to calcualte the average
                break
            num = int(user_input) #converts string to integer
            total += num #adds an additional number to the total from the users input
            count += 1 #when the user has entered another number that is not -1 it increases the count by 1
        
        average = total / count #calcuates the average

        print("The average is", average) #displays the average
