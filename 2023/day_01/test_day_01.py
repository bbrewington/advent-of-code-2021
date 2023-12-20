import pytest
from day_01.day_01 import get_first_last_digit_part1, get_first_last_digit_part2

def test_get_first_last_digit_part1():
    assert get_first_last_digit_part1('one2three') == 22

@pytest.mark.parametrize("input,expected",
                         [('one2three', 13), ('two1nine', 29), ('eightwothree', 83), ('abcone2threexyz', 13),
                          ('xtwone3four', 24), ('4nineeightseven2', 42), ('zoneight234', 14), ('7pqrstsixteen', 76)])
def test_get_first_last_digit_part2(input, expected):
    actual = get_first_last_digit_part2(input)
    assert actual == expected, f'Failed: {input=}, {expected=}, {actual=}'
