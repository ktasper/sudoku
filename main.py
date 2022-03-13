import puzzle.parsers as parsers
import puzzle.printer as printer


def main():
  puzzle_string = ".7..39.52...5...9.......6.7.1.94..2.3..6....5..9.23.16.3.........2......74..1...."
  # Generate a puzzle
  printer.print_board_basic(parsers.type_one_line(puzzle_string))


if __name__ == '__main__':
    main()