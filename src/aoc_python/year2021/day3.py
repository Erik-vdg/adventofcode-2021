"""Day 3: Binary Diagnostic"""
from typing import List
from typing import Tuple


def calculate_common_value_mask(reports: List[str]) -> Tuple[str, str]:
    transpose_reports = ["".join(c) for c in zip(*reports)]
    number_diagnostics = len(reports) / 2.0

    gamma_mask = [
        sum(int(i) for i in x) > number_diagnostics for x in transpose_reports
    ]
    epsilon_mask = [
        sum(int(i) for i in x) < number_diagnostics for x in transpose_reports
    ]

    gamma = "".join(str(int(x)) for x in gamma_mask)
    epsilon = "".join(str(int(x)) for x in epsilon_mask)

    return (gamma, epsilon)


def filter_reports_by_mask(reports: List[str], tiebreak: str) -> str:
    filtered_reports = reports.copy()
    position = 0
    while len(filtered_reports) > 1:
        filtered_column = [report[position] for report in filtered_reports]
        counts = (filtered_column.count("0"), filtered_column.count("1"))
        if tiebreak == "1" and counts[1] >= counts[0]:
            my_filter = "1"
        elif tiebreak == "1" and counts[1] < counts[0]:
            my_filter = "0"
        elif tiebreak == "0" and counts[0] <= counts[1]:
            my_filter = "0"
        elif tiebreak == "0" and counts[0] > counts[1]:
            my_filter = "1"
        filtered_reports = [
            report for report in filtered_reports if report[position] == my_filter
        ]
        position += 1
    return filtered_reports[0]


def part_a(data: List[str]) -> int:
    gamma, epsilon = calculate_common_value_mask(data)
    return int(gamma, 2) * int(epsilon, 2)


def part_b(data: List[str]) -> int:
    o2 = filter_reports_by_mask(data, "1")
    co2 = filter_reports_by_mask(data, "0")
    return int(o2, 2) * int(co2, 2)
