"""
This solves the board using backtracking
1. Find an empty space on the board
2. Try all the numbers in the empty space
3. Find a number that is valid
4. Repeat
5. If the soultion is not valid and cannot be valid backtrack
"""

from puzzle import printer as printer





def find_empty_tile(board):
  for i in range (len(board)):
    for j in range(len(board[0])):
      if board[i][j] == 0:
        return (i,j) # Row, Col
  return None

def valid(board, num, pos) -> bool:

  # Check each element in the row, check if its the same as the number we just added in.
  for i in range(len(board[0])):
    # If its the same postion we just added skip it
    if board[pos[0]][i] == num and pos[1] != i:
      return False

  # Check Column
  for i in range(len(board[0])):
  # If its the same postion we just added skip it
    if board[i][pos[1]] == num and pos[0] != i:
      return False

  # Check box
  box_x_pos = pos[1] // 3
  box_y_pos = pos[0] // 3

  # Loop over the box in the puzzle, skip the number we just added
  for i in range(box_y_pos * 3, box_y_pos*3 + 3):
    for j in range(box_x_pos * 3, box_x_pos*3 + 3):
      if board[i][j] == num and (i,j) != pos:
        return False

  return True

def solve(board):
  # If we hit the last tile in the board we have solved it
  find = find_empty_tile(board)
  if not find:
    return True
  else:
    row, col = find
  
  # 1 - 9 are only valid numbers

  for i in range(1,10):
    # Ensure the added number is valid
    if valid(board, i, (row,col)):
      # Add it to the board
      board[row][col] = i

      # If its solved exit the recursive cycle
      if solve(board):
        return True
      
      # Reset the last element to 0
      board[row][col] = 0
  return False
