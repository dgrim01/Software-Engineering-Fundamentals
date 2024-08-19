""" 
Module providing a framework for writing and running unit tests in Python.
"""
import unittest

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
    else:
        # returns the sum of the list adding the numbers upto
        # the specified index
        # this line returns the sum of the list specified index decrementing by
        # 1 to reach the base case of the index 0 

        return arr[index] + add_up_to(arr, index - 1)
# Example usage
print(add_up_to([1,4,5,3,12,16], 4)) # Output will be 25

print(add_up_to([4, 3, 1, 5], 1)) # Output will be 7

# Testing sum_recursion.py
class TestSumRecursion(unittest.TestCase):
    """ Class testing the function sum_recursion"""

    def test_list_with_one_number_and_valid_index(self):
        """ Function to test Sum Recursion with one number in the list"""
        # Arrange
        arr = [5]
        index = 0
        # Act
        result = add_up_to(arr, index)
        # Assert
        self.assertEqual(result, 5)

    def test_valid_index(self):
        """ Function to Sum Recursion with valid index """
        # Arrange
        arr = [1, 2, 3, 5, 10, 15]
        index = 4
        # Act
        result = add_up_to(arr, index)
        # Assert
        self.assertEqual(result, 21)

    def test_index_zero(self):
        """ Function to Sum Recursion with index of zero """
        # Arrange
        arr = [1, 2, 3, 5, 10, 15]
        index = 0
        # Act
        result = add_up_to(arr, index)
        # Assert
        self.assertEqual(result, 1)

    def test_index_out_of_range(self):
        """ Function to Sum Recursion with index out of range """
        # Arrange
        arr = [1, 2, 3, 5, 10, 15]
        index = -1
        # Act
        result = add_up_to(arr, index)
        # Assert
        self.assertEqual(result, 0)

    def test_empty_list(self):
        """ Function to Sum Recursion with empty list """
        # Arrange
        arr = []
        index = 0
        # Act
        result = add_up_to(arr, index)
        # Assert
        self.assertEqual(result, 0)

    def test_negative_numbers(self):
        """ Function tests when the list contains negative numbers """
        # Arrange
        arr = [-10, -3, -8, -2, -5]
        index = 3
        # Act
        result = add_up_to(arr, index)
        # Assert
        self.assertEqual(result, -23)

if __name__ == '__main__':
    unittest.main()
