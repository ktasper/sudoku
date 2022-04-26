def print_board(board) -> None:
    """Prints the board in a nice format."""
    board = [["`" if i == 0 else i for i in row] for row in board]
    print("- - - - - - - - - - - - ")
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
