from day_02 import read_input, check_part1_rules, count_part1_safe, part2_by_row

input_example = read_input('input_example.txt')

assert input_example[0] == [7, 6, 4, 2, 1], "Issue with reading input data"

for line, expected in zip(input_example, ['Safe', 'Unsafe', 'Unsafe', 'Unsafe', 'Unsafe', 'Safe']):
    actual = check_part1_rules(line)
    assert actual == expected, f"Failed check - line: {line}, expected: {expected}, actual: {actual}"

assert count_part1_safe(input_example) == 2

input_final = read_input('input_final.txt')

part1_result = count_part1_safe(input_final)

for line, expected in zip(input_example, ['Safe', 'Unsafe', 'Unsafe', 'Safe', 'Safe', 'Safe']):
    actual = part2_by_row(line)
    assert actual == expected, f"Failed check - line: {line}, expected: {expected}, actual: {actual}"

part2_result = sum(part2_by_row(line) == 'Safe' for line in input_final)
