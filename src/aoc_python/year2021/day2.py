"""Day 2: Dive!"""
from dataclasses import dataclass
from enum import Enum
from typing import List

from typing_extensions import Literal

from aoc_python.util.common import Coordinate


class BearingEnum(Enum):
    FORWARD: Literal["forward"] = "forward"
    DOWN: Literal["down"] = "down"
    UP: Literal["up"] = "up"


@dataclass
class Command:
    bearing: BearingEnum
    magnitude: int

    @classmethod
    def from_str(cls, raw_command: str) -> "Command":
        parts = raw_command.split()
        command_str = BearingEnum(parts[0])
        return cls(
            bearing=command_str,
            magnitude=int(parts[1]),
        )

    def coordinate_delta(self) -> Coordinate:
        if self.bearing is BearingEnum.FORWARD:
            return Coordinate(self.magnitude, 0)
        elif self.bearing is BearingEnum.UP:
            return Coordinate(0, -1 * self.magnitude)
        elif self.bearing is BearingEnum.DOWN:
            return Coordinate(0, self.magnitude)


class AimedSubmarine:
    position: Coordinate
    aim: int

    def __init__(self) -> None:
        self.position = Coordinate(0, 0)
        self.aim = 0

    def handle_command(self, command: Command) -> None:
        if command.bearing is BearingEnum.DOWN:
            self.aim += command.magnitude
        elif command.bearing is BearingEnum.UP:
            self.aim -= command.magnitude
        elif command.bearing is BearingEnum.FORWARD:
            delta = Coordinate(command.magnitude, self.aim * command.magnitude)
            self.position += delta


def part_a(data: List[str]) -> int:
    coordinate_deltas = [Command.from_str(n).coordinate_delta() for n in data]
    final_coordinate = sum(coordinate_deltas, Coordinate(0, 0))
    return final_coordinate.x * final_coordinate.y


def part_b(data: List[str]) -> int:
    commands = [Command.from_str(n) for n in data]
    sub = AimedSubmarine()
    for command in commands:
        sub.handle_command(command)
    return sub.position.x * sub.position.y
