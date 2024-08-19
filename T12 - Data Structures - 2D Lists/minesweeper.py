"""
    In the file 'minesweeper.py', the function 'count_adjacent mines'loops through
    the 2D list based on the direction of x and y indices which is calculate from 
    the original x and y indices. When it loops the the new indices it then checks
    if it contain a mine '#' then adds and returns it to the count.

    The function 'mine_sweeper' loops through each row and column on the 2D list,
    when a "-" in found in the list it then replaces it by a digit when then indicates
    the number of mines adjacent to that element in the list. This is done when the 
    'count_adjacent mines' function is called to then replace the '-' with count of mines
    which is then convert to a string and updates the mine field.
 
"""
def count_adjacent_mines(minefield, row, col):
    """
    This function takes the 2D list 'minefield', row and col indicating the row and column
    of the cells to ouput the adjacent number of mines. It does this initialising a count 
    then loops through to calculate new indices and checks for mines.

    Once each mine is found it then adds to and returns the count.

    """
    # Initialises the count of the mines
    count = 0
    # Defines a list of directions to check through each cell by x and y indices
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    # loops through each of the directions
    for dx, dy in directions:
        # Calculates the new_row adding the row and x indice
        # Then calculates the new_col indice by adding the col and y indice
        new_row, new_col = row + dx, col + dy
        # loops the minefield with the new indices to see if they contain a mine '#'
        if 0 <= new_row < len(mine_field) and 0 <= new_col < len(mine_field[0]) and mine_field[new_row][new_col] == "#":
            # If an element contains a mine it adds to the count
            count += 1
    # Returns the total count of the mines
    return count

def mine_sweeper(mine_field):
    """
    This functions through and updates and the inputted minefield where
    a '-' it the updates it by calling the 'count_adjacent mines' function
    that counts the mines which then replaces the '-' with the count that has been
    converted to a string then returns it to a list.

    """
    # Loops through each row in the 2D list 
    for row in range(len(mine_field)):
        # Loops through each column in the 2D list 
        for col in range(len(mine_field[row])):
            # When looping through 2D when looping through item in the rows and columns if a "-" is found then replaces it with a digit
            if mine_field[row][col] == "-":
                mine_field[row][col] = str(count_adjacent_mines(mine_field, row, col))
    # Returns the minefield with the cells that contained '-' with the count of adjacent mines
    return mine_field

# Input 2D list
mine_field = [ ["-", "-", "-", "#", "#"],
               ["-", "#", "-", "-", "-"],
               ["-", "-", "#", "-", "-"],
               ["-", "#", "#", "-", "-"],
               ["-", "-", "-", "-", "-"] 
]

# Prints each column and row and Displays a digit where "-" previously was
mine_field_with_digits = mine_sweeper(mine_field) 
# Prints the list with each row of on a new line
# Making it look more like rows and columns rather than just a long line of rows
for row in mine_field_with_digits:
    print(row)

        
   


