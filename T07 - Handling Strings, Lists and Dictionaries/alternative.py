alternate_string = str(input("Enter a short sentence or phrase: "))

#makes every other letter uppercase
def alternate_letter_uppercase(alternate_string):
    new_string = ""
    for i in range(len(alternate_string)): #turns each letter in the string into a sequence of integer with range, len takes the length of the string
        if i % 2 == 0: #for each corresponding letter in the range that is divisible by 2 becomes uppercase
            new_string += alternate_string[i].upper()
        else: #for each corresponding letter in the range that is NOT divisible by 2 becomes uppercase
            new_string += alternate_string[i].lower()
    return new_string

output_string = alternate_letter_uppercase(alternate_string)
print(output_string)

#makes every other word uppercase
def alternate_word_uppercase(alternate_string):
    words = alternate_string.split() #turns the string into a list with each element 
    new_string2 = ""
    for i in range(len(words)): #turns each word in the string into a sequence of integer with range, len takes the length of the string
        if i % 2 == 0:
            new_string2 += words[i].upper() #makes each word in the list that is divisible by 2 into uppercase
        else:
            new_string2 += words[i]
        new_string2 += " " #adds space between the words
    return new_string2 


output_string2 = alternate_word_uppercase(alternate_string) #stores the ouput of alternate_word_uppercase function as variable
print(output_string2) #displays the ouput of the alternate_word_uppercase function
