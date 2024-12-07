import pytest
from day_03 import read_input, part1, do_dont_mask, use_do_dont_mask, part2

ex_p1 = read_input("input_example_part1.txt")
assert part1(ex_p1) == 161

input_final = read_input("input_final.txt")
part1_result = part1(input_final)

ex_p2 = read_input("input_example_part2.txt")

@pytest.mark.parametrize("test_input,expected", [
    ("adon't()b", "100000000"),
    ("ado()b", "100001"),
    ("aado()bbdon't()ccdo()dddon't()ee", "11000011000000000000011000000000")
])
def test_do_dont_mask(test_input, expected):
    assert do_dont_mask(test_input) == expected

def test_use_do_dont_mask():
    assert use_do_dont_mask("aado()bbdon't()ccdo()dddon't()ee") == "aabbdd"

ex_p3 = read_input("input_final.txt")

def test_part2():
    assert part2("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))") == 48
