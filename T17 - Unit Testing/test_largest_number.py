""" 
Module providing a framework for writing and running unit tests in Python.
"""
import unittest

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
    elif len(my_list) == 0:
        return None
    else:
        # Compares the first element in the list with the next element,
        # until it finds the maximum/largest number.
        return max(my_list[0], largest_number(my_list[1:]))

# Example Usage:
print (largest_number([1, 4, 5, 3])) # Output should be 5

print (largest_number([3, 1, 6, 8, 2, 4, 5])) # Output should be 8

# Testing largest_number.py


class TestLargestNumber(unittest.TestCase):
    """ Class testing the function largest_number """

    def test_list_with_one_number(self):
        """ Function to test largest_number with one number in the list """
        # Arrange
        my_list = [5]
        # Act
        result = largest_number(my_list)
        # Assert
        self.assertEqual(result, 5)

    def test_list_with_two_numbers(self):
        """ Function to test largest_number with two numbers in the list """
        # Arrange
        my_list = [5, 10]
        # Act
        result = largest_number(my_list)
        # Assert
        self.assertEqual(result, 10)

    def test_list_with_three_numbers(self):
        """ Function to test largest_number with three numbers in the list """
        # Arrange
        my_list = [5, 10, 21]
        # Act
        result = largest_number(my_list)
        # Assert
        self.assertEqual(result, 21)
       
    def test_list_with_five_numbers(self):
        """ Function to test largest_number with five number in the list """
        # Arrange
        my_list = [5, 10, 21, 2, 30]
        # Act
        result = largest_number(my_list)
        # Assert
        self.assertEqual(result, 30)

    def test_negative_numbers(self):
        """ Function tests when the list contains negative numbers """
        # Arrange
        my_list = [-10, -3, -8, -2, -5]
        # Act
        result = largest_number(my_list)
        # Assert
        self.assertEqual(result, -2)

    def test_duplicate_largest_number(self):
        """ Function tests when the list contains duplicate largest numbers """
        # Arrange
        my_list = [5, 8, 2, 10, 10, 5]
        # Act
        result = largest_number(my_list)
        # Assert
        self.assertEqual(result, 10)


    def test_empty_list(self):
        """ Function to test largest_number with no numbers in the list """
        # Arrange
        my_list = []
        # Act
        result = largest_number(my_list)
        # Assert
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
