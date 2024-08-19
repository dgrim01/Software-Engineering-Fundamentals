#asks user to enter a sentence
str_manip = input("Please Enter a Sentence here: ")
#Calculates and display the length of str_manip
print(len(str_manip))
#finds and store the last letter as a variable called last_letter
last_letter = str_manip[-1]
#replaces the letter identified
new_strmanip = str_manip.replace(last_letter, '@')
#displays the new string with the replaced letters
print(new_strmanip)
#extracts and store the last 3 letter of str_manip in a variable
last_3_letters = str_manip[-3:]
# Displays the last 3 letters of str_manip in resverse order
print(last_3_letters[::-1])
#extracts the first 3 letters of str_manip and store it in first_3_letters
first_3_letters = str_manip[0:3]
#extracts the last 2 letters of str_manip and store it in last_2_letters
last_2_letters = str_manip[-2:]
#Displays the first_3_letters and last_2_letters togehter to make one word
print(first_3_letters + last_2_letters)