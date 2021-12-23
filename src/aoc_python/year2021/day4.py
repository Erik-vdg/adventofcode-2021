"""Day 4: Giant Squid"""
from typing import Dict
from typing import List
from typing import Sequence
from typing import Set
from typing import Tuple

from aoc_python.util.common import Coordinate
from aoc_python.util.common import split_groups


class BingoBoard:
    _value_map: Dict[int, Coordinate]
    _drawn_values: Set[int]
    BOARD_SIZE = 5

    @classmethod
    def from_input_rows(cls, raw_input: Sequence[str]) -> "BingoBoard":
        ret = cls()
        ret._value_map = dict()
        ret._drawn_values = set()
        for row, line in enumerate(raw_input[1:]):
            for col, val in enumerate(line.split()):
                ret._value_map[int(val)] = Coordinate(col, row)
        return ret

    @property
    def wins(self) -> bool:
        # Use the _drawn_values set to find our drawn coordinates in a set
        drawn_coords = {self._value_map[val] for val in self._drawn_values}
        # Check for rows and columns
        for i in range(self.BOARD_SIZE):
            if (
                len(list(filter(lambda coord: coord.x == i, drawn_coords)))
                == self.BOARD_SIZE
                or len(list(filter(lambda coord: coord.y == i, drawn_coords)))
                == self.BOARD_SIZE
            ):
                return True

        # Otherwise we don't have any solutions
        return False

    @property
    def board_score(self) -> int:
        unchosen = set(self._value_map.keys()).difference(self._drawn_values)
        return sum(unchosen)

    def draw_number(self, value: int) -> None:
        if value in self._value_map:
            self._drawn_values.add(value)


def parse_input(data: List[str]) -> Tuple[List[int], List[BingoBoard]]:
    # First line is a comma-seperated list of ints:
    values = [int(val) for val in data[0].split(",")]
    # Next bunches of 5 lines at a time are raw bingo boards
    boards = [
        BingoBoard.from_input_rows(raw_board) for raw_board in split_groups(data[1:], 6)
    ]
    return values, boards


def bingo_drawing(values: List[int], boards: List[BingoBoard]) -> int:
    for value in values:
        for board in boards:
            board.draw_number(value)
            if board.wins:
                return board.board_score * value
    raise ValueError("No board achieved a win in our list of values!")


def bingo_drawing_loser(values: List[int], boards: List[BingoBoard]) -> int:

    for value in values:
        elligible_boards = list()
        for board in boards:
            board.draw_number(value)
            if board.wins:
                if len(boards) == 1:
                    return board.board_score * value
            else:
                elligible_boards.append(board)
        boards = elligible_boards.copy()
    raise ValueError("No board achieved a win in our list of values!")


def part_a(data: List[str]) -> int:
    values, boards = parse_input(data)
    return bingo_drawing(values, boards)


def part_b(data: List[str]) -> int:
    values, boards = parse_input(data)
    return bingo_drawing_loser(values, boards)
