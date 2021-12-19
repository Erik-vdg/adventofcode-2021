from dataclasses import dataclass


@dataclass
class Coordinate:
    x: int
    y: int

    def move(self, x: int = 0, y: int = 0) -> "Coordinate":
        return Coordinate(self.x + x, self.y + y)

    def __add__(self, other: "Coordinate") -> "Coordinate":
        return Coordinate(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Coordinate") -> "Coordinate":
        return Coordinate(self.x - other.x, self.y - other.y)
