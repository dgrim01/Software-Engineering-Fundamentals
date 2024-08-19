def largest_number(my_list):
    """
    This function takes the list of my integers (my_list) compare each element
    in the list to find the largest number.

    if the list on contains one element it returns the first and only element in
    the list. If the list contain multiple elements, it compares each element in 
    the list to find the largest number.

    """
    # if the list only contains one element, it returns the first number in the list
    # as there nothing to compare it to trigger the else.
    if len(my_list) == 1:
        return my_list[0]
    else:
        """
        # Compares the first element in the list with the next element,
        until it finds the maximum/largest number.

        """
        return max(my_list[0], largest_number(my_list[1:]))

# Example Usage:
print (largest_number([1, 4, 5, 3])) # Output should be 5

print (largest_number([3, 1, 6, 8, 2, 4, 5])) # Output should be 8