import puzzle.parsers as parsers
import puzzle.printer as printer
import puzzle.solver as solver
from halo import Halo

def main():
    """
    Main function, runs the program.
    """
    puzzle_string = "..9...3.....5.9...4.......29..6.8..783.4.2.51.5.....6.5...9...4..2.1.7..........."
    # Generate a puzzle
    board = parsers.type_one_line(puzzle_string)
    print("Puzzle:")
    printer.print_board(board)
    print(" ")
    spinner = Halo(text='Solving Puzzle',spinner='dots',color='blue')
    spinner.start()
    solver.solve(board)
    spinner.succeed('Sovled!')
    printer.print_board(board)



if __name__ == '__main__':
    main()
