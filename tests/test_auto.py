from dataclasses import dataclass
from pathlib import Path
from typing import Dict
from typing import List
from typing import Union

import pytest
import yaml

from aoc_python.util import get_function

TEST_DATA_DIR = Path("tests/test_data")
AUTOTEST_FILENAME = "autotest.yaml"


@dataclass
class SingleTestCase:
    year: int
    day: int
    name: str
    input: List[str]
    expected: Union[str, int]

    @classmethod
    def from_dict(
        cls, year: int, day: int, input_dict: Dict, filepath: Path
    ) -> "SingleTestCase":
        input_path = filepath.joinpath(input_dict["input"])
        with input_path.open("r") as test_data:
            return cls(
                year=year,
                day=day,
                name=input_dict["name"],
                input=test_data.read().splitlines(),
                expected=input_dict["expected"],
            )

    @classmethod
    def pytest_parameter_id_friendly(cls, stc: "SingleTestCase") -> str:
        return f"year={stc.year}, day={stc.day}, name={stc.name}"


@dataclass
class AutoTest:
    year: int
    day: int
    tests: List[SingleTestCase]

    @classmethod
    def from_yaml(cls, filepath: Path) -> "AutoTest":
        year = int(filepath.parent.stem)
        day = day = int(filepath.stem[3:])
        with filepath.joinpath(AUTOTEST_FILENAME).open("r") as file:
            yaml_loaded = yaml.full_load(file)
            tests = [
                SingleTestCase.from_dict(
                    year=year, day=day, input_dict=test, filepath=filepath
                )
                for test in yaml_loaded["tests"]
            ]
        return cls(year=year, day=day, tests=tests)


def discover_auto_test_data() -> List[AutoTest]:
    discovered_tests: List[AutoTest] = []
    for year_path in TEST_DATA_DIR.iterdir():
        for day_path in year_path.iterdir():
            if day_path.joinpath(AUTOTEST_FILENAME).exists():
                discovered_tests.append(AutoTest.from_yaml(day_path))
    return discovered_tests


used_testcases = discover_auto_test_data()[0].tests


@pytest.mark.parametrize(
    "testcase", used_testcases, ids=SingleTestCase.pytest_parameter_id_friendly
)
def test_runner(testcase: SingleTestCase):
    tested_function = get_function(testcase.year, testcase.day, testcase.name)
    found_output = tested_function(testcase.input)
    expected_output = testcase.expected
    assert found_output == expected_output
