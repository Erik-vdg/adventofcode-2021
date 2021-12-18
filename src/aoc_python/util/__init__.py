"""
This module provides a sample entry-point for your aocd "plugin".
advent-of-code-data runner will repeatedly call your entry point
with varying year (2015+), day (1-25) and input data. The only
requirement is: your entry-point should be a callable which must
return a tuple of two values.
Note: On Dec 25 there is only one puzzle, but you should return
a tuple of 2 values anyway, e.g. (part_a_answer, None) the
second value of the tuple will not be used regardless.
Do whatever you want in your entry-point - you can import other
modules, call a function, run a script or a subprocess, etc.
If your existing code reads in data from a file, you could even
write out a scratch file from this entry-point.
For example, a sensible pattern might be something like:
    def mysolve(year, day, data):
        mod_name = "mypackage.aoc{}.day{}".format(year, day)
        mod = importlib.import_module(mod_name)
        a = mod.part_a(data)
        b = mod.part_b(data)
        return a, b
Or you could leave answers in the module namespace:
    mod = importlib.import_module(mod_name)
    return mod.a, mod.b
Or you could even just get them from a .py script print output:
    answers = io.StringIO()
    with redirect_stdout(answers):
        mod = importlib.import_module(mod_name)
    a, b = answers.getvalue().splitlines()
The AOC_SESSION is set before invoking your entry-point, which
means you can continue to use `from aocd import data` if you
want - it's not strictly necessary to define worker functions
which accept the input data as an argument (although, this is
usually a good practice, so that you can easily check your code
provides correct answers for each of the puzzle test cases!)
"""
import importlib
from typing import Callable
from typing import List
from typing import Tuple
from typing import Union

AocSolution = Callable[[List[str]], Union[str, int]]


def mysolve(
    year: str, day: str, data: str
) -> Tuple[Union[str, int], Union[str, int]]:  # pragma: nocover
    data_list = data.splitlines()
    a = get_function(year, day, "part_a")(data_list)
    b = get_function(year, day, "part_b")(data_list)
    return a, b


def get_function(year: str, day: str, function_name: str) -> AocSolution:
    mod_name = "aoc_python.{}.day{}".format(year, day)
    mod = importlib.import_module(mod_name)
    found_func: AocSolution = getattr(mod, function_name)
    return found_func
