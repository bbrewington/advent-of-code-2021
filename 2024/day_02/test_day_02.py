from day_02 import read_input, check_part1_rules, count_part1_safe

input_example = read_input('input_example.txt')

assert input_example[0] == [7, 6, 4, 2, 1], "Issue with reading input data"

for line, expected in zip(input_example, ['Safe', 'Unsafe', 'Unsafe', 'Unsafe', 'Unsafe', 'Safe']):
    actual = check_part1_rules(line)
    assert check_part1_rules(line) == expected, f"Failed check - line: {line}, expected: {expected}, actual: {actual}"

assert count_part1_safe(input_example) == 2

input_final = read_input('input_final.txt')
final = count_part1_safe(input_final)
