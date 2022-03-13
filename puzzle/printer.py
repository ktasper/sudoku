def print_board_basic(grid):
  # Format the grid
  grid = [["?" if i == 0 else i for i in row] for row in grid]
  # print the lists as strings with a space between each number
  for row in grid:
    line = (" ".join([str(i) for i in row]))
    print(line)