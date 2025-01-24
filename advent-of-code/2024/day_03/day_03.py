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
    valid_muls = re.findall(r"mul\((\d+),(\d+)\)", input_str)
    sum_val = 0
    for mul in valid_muls:
        x, y = [int(x) for x in mul]
        sum_val += x * y
    return sum_val

def part1(x):
    return parse_muls(x)

def do_dont_mask(input):
    do_spans = [x.span() for x in re.finditer(r'do\(\)', input)]
    dont_spans = [x.span() for x in re.finditer(r"don't\(\)", input)]
    do_to_dont_spans = [x.span() for x in re.finditer(r"(?<=do\(\)).+?(?=don't\(\))", input)]
    dont_to_do_spans = [x.span() for x in re.finditer(r"(?=don't\(\)).+?(?<=do\(\))", input)]
    mask = ['1'] * len(input)
    for do_span in do_spans:
        if do_span:
            start, end = do_span
            mask[start:end] = ["0"] * (end - start)
    for dont_span in dont_spans:
        if dont_span:
            start, end = dont_span
            mask[start:end] = ["0"] * (end - start)
    for do_to_dont_span in do_to_dont_spans:
        if do_to_dont_span:
            start, end = do_to_dont_span
            mask[start:end] = ["1"] * (end - start)
    for dont_to_do_span in dont_to_do_spans:
        if dont_to_do_span:
            start, end = dont_to_do_span
            mask[start:end] = ["0"] * (end - start)
    # If last one is a dont (or if that's all there is), mark from there to end of file as 0
    if (len(do_spans) > 0 and len(dont_spans) > 0):
        if dont_spans[-1][-1] > do_spans[-1][-1]:
            mask[dont_spans[-1][-1]:] = ["0"] * len(mask[dont_spans[-1][-1]:])
    elif (len(do_spans) == 0 and len(dont_spans) > 0):
        mask[dont_spans[-1][-1]:] = ["0"] * len(mask[dont_spans[-1][-1]:])
    
    return ''.join(mask)

def use_do_dont_mask(input):
    mask = do_dont_mask(input)
    new_str = ''
    for i, m in enumerate(mask):
        if m == '1':
            new_str += input[i]
    return new_str

def part2(input):
    return parse_muls(use_do_dont_mask(input))
