for x in range(1,6): #this means it will only print the number of times inclusive of the range so at max 5 times as 6 is exclusive as to stop the sequence before 6
    if x <= 5: #if the squence is 5 or less is displays an *. Being just < 5 would make it so that it could only reach 4 astrixes
        print('*' * x) #displays an astrix equal to the number in the sequence
    else:
        print('*' * (5 - x)) 

for x in range(4, 0, -1): #the squence starts at printing four atrixes and prints them in reverse order of the sequence
    if x <= 5: #checks at what point in the sequence it is
        print('*' * x) #displays the number of astrixes in each point in the squence
    else:
        print('*' * (5 - x ))