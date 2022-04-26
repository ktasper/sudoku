# Using https://qqwing.com/generate.html as a reference
# Take in the file format as OneLine



def type_one_line(puzzle_string) -> list:
    """
    Parse the input file and return a list of lists that form a sudoku puzzle
    """
    # Ensure that the format of the passed in string is correct
    grid = []
    if len(puzzle_string) != 81:
        raise ValueError("The puzzle string must be 81 characters long")
    # If a char in the string is not a digit, set it to 0
    for i in range(len(puzzle_string)):
        if puzzle_string[i] not in "123456789":
            puzzle_string = puzzle_string[:i] + "0" + puzzle_string[i + 1:]
    # Convert the string to ints
    grid = [int(i) for i in puzzle_string]
    # Convert the list to a list of lists
    grid = [grid[i:i + 9] for i in range(0, len(grid), 9)]
    return grid
