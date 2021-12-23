from dataclasses import dataclass
from itertools import zip_longest
from typing import Iterable
from typing import Optional
from typing import Sequence
from typing import TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class Coordinate:
    x: int
    y: int

    def move(self, x: int = 0, y: int = 0) -> "Coordinate":
        return Coordinate(self.x + x, self.y + y)

    def __add__(self, other: "Coordinate") -> "Coordinate":
        return Coordinate(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Coordinate") -> "Coordinate":
        return Coordinate(self.x - other.x, self.y - other.y)


def split_groups(
    items: Iterable[T], group_size: int, fillvalue: Optional[T] = None
) -> Iterable[Sequence[T]]:
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(items)] * group_size
    groups = zip_longest(*args, fillvalue=fillvalue)
    return groups
