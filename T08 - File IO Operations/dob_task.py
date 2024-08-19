#Opens the file in reading mode
with open('./Input Code Files/Task file/DOB.txt', 'r') as file:
    lines = file.readlines()

name_list = []
dob_list = []

# Loops through each line in the file
for line in lines:
    # Split the line into indiviual strings
    split_string = line.strip().split(' ')
    # since the lines have been split into individual strings it then joins the first and last name together.
    #stored in the variable called name
    name = ' '.join(split_string[0:2])
    # joins the day, month and year together storing it in the variable called dob (Date of Birth)
    dob = ' '.join(split_string[2:5])
    #adds the names and dates of birth to there there corresponding lists
    name_list.append(name)
    dob_list.append(dob)
#Display the names list with the heading "Name"
print("\nName ")
for name in name_list:
    print(name)
#Displays the DOB with the heading "Date of Birth"
print("\nDate of Birth ")
for dob in dob_list:
    print(dob)
    
    
    
    
    
    

