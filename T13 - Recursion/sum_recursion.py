def add_up_to(arr, index):
    """
    This function takes the list of integer (arr) and single integer index (index) and
    adds all the numbers in the list list up until the specified index

    a real-life application for this function without the specified index
    could be a total of a persons shopping at the checkout and shown on their
    recipt.

    """
    if index < 0 or index >= len(arr):
        # if the index is smaller than the minimum index
        # of the list or exceeds the maximum index of the list it return 0
        return 0
    
    elif index == 0:
        # if the index is 0 it then return the first number in the list
        # as the first index in a list is 0 ex. with the first example usage output is 1
        return arr[0]
    # 
    else:
        """
        returns the sum of the list adding the numbers upto the specified index
        this line returns the sum of the list specified index decrementing by 1 to reach
        the base case of the index 0 

        """
         
        return arr[index] + add_up_to(arr, index - 1)
    
# Example usage
print(add_up_to([1,4,5,3,12,16], 4)) # Output will be 25

print(add_up_to([4, 3, 1, 5], 1)) # Output will be 7