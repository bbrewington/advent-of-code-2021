import re

def read_input(file_path):
    with open(file_path, 'r') as f:
        file_contents = f.readlines()
        return_list = [line.strip() for line in file_contents]
        return_str = ' '.join(return_list)
    return return_str

# def get_valid_muls(x):
#     return re.findall("mul\(\d+,\d+\)", x)

def parse_muls(input_str):
    valid_muls = re.findall("mul\((\d+),(\d+)\)", input_str)
    sum_val = 0
    for mul in valid_muls:
        x, y = [int(x) for x in mul]
        sum_val += x * y
    return sum_val

def part1(x):
    return parse_muls(x)
