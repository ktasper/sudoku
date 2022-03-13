import puzzle.parsers as parsers
import pytest

# Assert if we pass in a shorter string than 81 characters we get an error
def test_type_one_line_fails():
    puzzle_string = ".7..39.52...5...9......."
    with pytest.raises(ValueError):
        parsers.type_one_line(puzzle_string)

# Check to ensure we are generating a correct grid
def test_type_one_line_passes():
    puzzle_string = ".7..39.52...5...9.......6.7.1.94..2.3..6....5..9.23.16.3.........2......74..1...."
    assert parsers.type_one_line(puzzle_string) == [
        [0, 7, 0, 0, 3, 9, 0, 5, 2],
        [0, 0, 0, 5, 0, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 7],
        [0, 1, 0, 9, 4, 0, 0, 2, 0],
        [3, 0, 0, 6, 0, 0, 0, 0, 5],
        [0, 0, 9, 0, 2, 3, 0, 1, 6],
        [0, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [7, 4, 0, 0, 1, 0, 0, 0, 0]
    ]