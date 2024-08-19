def merge_sort(items):
    n = len(items)
    temporary_storage = [None] * n
    size_of_subsections = 1

    while size_of_subsections < n:
        for i in range(0, n, size_of_subsections * 2):
            i1_start, i1_end = i, min(i + size_of_subsections, n)
            i2_start, i2_end = i1_end, min(i1_end + size_of_subsections, n)
            sections = (i1_start, i1_end), (i2_start, i2_end)
            merge(items, sections, temporary_storage)
        size_of_subsections *= 2

    return items

def merge(items, sections, temporary_storage):
    # Unpack the sections into start and end indices for both halves
    (start_1, end_1), (start_2, end_2) = sections
    # Initialize indices for the first half, second half, and temporary storage
    i_1 = start_1
    i_2 = start_2
    i_t = 0
    # Merge elements from both halves until one of the halves is exhausted
    while i_1 < end_1 and i_2 < end_2:
        # Compare the lengths of the strings at current indices
        if len(items[i_1]) >= len(items[i_2]):
            # If the string in the first half is longer or equal,
            # copy it to the temporary storage and move to the next index in the first half
            temporary_storage[i_t] = items[i_1]
            i_1 += 1
        else:
            # If the string in the second half is longer,
            # copy it to the temporary storage and move to the next index in the second half
            temporary_storage[i_t] = items[i_2]
            i_2 += 1
            # Move to the next index in the temporary storage
        i_t += 1

    # Copy any remaining elements from the first half
    if i_1 < end_1:
        for i in range(i_1, end_1):
            temporary_storage[i_t] = items[i]
            i_t += 1
    # Copy any remaining elements from the second half
    elif i_2 < end_2:
        for i in range(i_2, end_2):
            temporary_storage[i_t] = items[i]
            i_t += 1

    # Copy merged elements back to the original list
    for i in range(i_t):
        items[start_1 + i] = temporary_storage[i]



# Example Usage
unsorted_strings_1 = ["apple", "banana", "orange", "grape", "kiwi", "mango", "pineapple", "peach", "pear", "cherry"]
unsorted_strings_2 = ["carrot", "pepper", "broccoli", "lettuce", "radish", "tomato", "cucumber", "spinach", "onion", "cauliflower"]
unsorted_strings_3 = ["dog", "cat", "elephant", "sheep", "mouse", "wolf", "raven", "bear", "fox", "spider"]

# Merge Sorts list "unsorted_strings_1" and displays the result
sorted_strings_1 = merge_sort(unsorted_strings_1)
print(sorted_strings_1)
# Merge Sorts list "unsorted_strings_2" and displays the result
sorted_strings_2 = merge_sort(unsorted_strings_2)
print(sorted_strings_2)
# Merge Sorts list "unsorted_strings_3" and displays the result
sorted_strings_3 = merge_sort(unsorted_strings_3)
print(sorted_strings_3)