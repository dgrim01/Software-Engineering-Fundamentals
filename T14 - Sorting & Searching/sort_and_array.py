"""
As the elements in the list are not in order so the searching algorithm that should be used is a linear search.

ex. lst_num = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]


"""

def linear_search_num(arr, item):
    # If item is not found return found, return None
    #
    #
    for i in range(len(arr)):
        if arr[i] == item:
            return i
        
# Example usage
lst_num = [27, -3, 4, 5, 35, 2, 1, -40, 7, 18, 9, -1, 16, 100]
target_number = 9

index = linear_search_num(lst_num, target_number)

if index != -1:
    print(f"The target element {target_number} was found at index {index}.")
else:
    print(f"The target element {target_number} was not found in the list.")

# Insertion Sort
def insertion_sort_lst_num(lst):
    # Loop through the array starting from the second element
    for i in range(1, len(lst)):
        # Store the current element in a variable 'key'
        key = lst[i]
        # Initialize a variable 'j' to point to the element before the current one
        j = i - 1

        # Move elements of 'lst[0..i-1]', that are greater than 'key', to one position ahead of their current position
        while j >= 0 and lst[j] >= key:

            lst[j + 1] = lst[j]
            j = j - 1

        # Place 'key' into its correct position in the sorted subarray
        lst[j + 1] = key

    return lst

index_2 = insertion_sort_lst_num(lst_num)
print(f"Sorted list: {index_2}")

"""
You might use a Binary search on a school register as the students would be
in alphabetical order, meaning it is ordered over a unordered list where you'd
want to use a linear search.

"""
def binary_search(lst, key):
    # Initialises left pointer of the list
    left = 0
    # Initialises right pointer of the list
    right = len(lst) -1
    # Loop until left pointer is less than right pointer
    while left <= right:
        # Calculates the middle index.
        mid = (left + right) // 2
        # If the middle element is equal to the key, return its index
        if lst[mid] == key:

            return mid
        # If the middle element is less than the key, update left pointer to search the right half.
        elif lst[mid] < key:

            left = mid + 1
        # If the middle element is greater than the key, update right pointer to search the left half.
        else:

            right = mid - 1
    # If the key is not found in the list, return -1.
    return -1

find_9 = binary_search(index_2, target_number)

if find_9 != -1:
    print(f"The target element {target_number} was found at index {index}.")
else:
    print(f"The target element {target_number} was not found in the list.")


