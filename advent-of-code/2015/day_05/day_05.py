import re
import numpy as np

def get_input_data(filepath):
    with open(filepath, 'r') as f:
        return [x.strip() for x in f.readlines()]

def check_vowel_count(s, num_vowels):
    vowel_pattern = re.compile('[aeiou]')
    return len(vowel_pattern.findall(s)) >= num_vowels

def check_repeated_char(input_str):
    for s1, s2 in zip(input_str, input_str[1:]):
        if s1 == s2:
            return True
    return False

def check_specific_strings(input_str, specific_strings_list=['ab', 'cd', 'pq', 'xy']):
    pattern = re.compile('|'.join(specific_strings_list))
    return len(pattern.findall(input_str)) == 0

def check_pair_twice(input_str):
    # It contains a pair of any two letters that appears at least twice in the
    # string without overlapping, like xyxy (xy) or aabcdefgaa (aa),
    # but not like aaa (aa, but it overlaps).
    
    for i in range(len(input_str) - 1):
        traveler = input_str[i:(i+2)]
        if input_str.count(traveler) >= 2:
            return True

    return False

def check_letter_repeat_between(input_str):
    # It contains at least one letter which repeats with exactly one letter
    # between them, like xyx, abcdefeghi (efe), or even aaa.
    total_count = 0
    for i in range(len(input_str) - 2):
        traveler = input_str[i:(i+3)]
        if traveler[0] == traveler[2]:
            total_count = total_count + 1
    return total_count > 0

def part_1(filepath):
    input_data = get_input_data(filepath)
    check_array = np.array(
        [[check_vowel_count(x, 3) for x in input_data]] + \
        [[check_repeated_char(x) for x in input_data]] + \
        [[check_specific_strings(x) for x in input_data]])
    num_checks_passed = check_array.sum(axis=0)

    return len(num_checks_passed[num_checks_passed == check_array.shape[0]])

print(part_1('input_data.txt'))

def part_2(filepath):
    input_data = get_input_data(filepath)
    check_array = np.array(
        [[check_pair_twice(x) for x in input_data]] + \
        [[check_letter_repeat_between(x) for x in input_data]]
    )
    num_checks_passed = check_array.sum(axis=0)

    return len(num_checks_passed[num_checks_passed == check_array.shape[0]])

print(part_2('input_data_part2_test.txt'))