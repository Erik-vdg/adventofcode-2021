"""Day 1: Sonar Sweep"""
from typing import List


def part_a(data: List[str]) -> int:
    ns = [int(n) for n in data]
    return sum(n2 > n1 for n1, n2 in zip(ns, ns[1:]))


def part_b(data: List[str]) -> int:
    ns = [int(n) for n in data]
    return sum(n2 > n1 for n1, n2 in zip(ns, ns[3:]))
