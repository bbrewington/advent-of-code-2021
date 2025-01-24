import re
from argparse import ArgumentParser

CHAR_TYPES =  {'blank': '.', 'digit': '#', 'symbol': '$'}

def classify_char(x):
    if x == CHAR_TYPES['blank']:
        return CHAR_TYPES['blank']
    elif x in '0123456789':
        return CHAR_TYPES['digit']
    else:
        return CHAR_TYPES['symbol']

class TargetNum:
    def __init__(self, line_id, label, start, end):
        self.line_id = line_id
        self.label = label
        self.start = start
        self.end = end
        
        self.is_partnum = False
        
    def __repr__(self):
        elements = f"'{self.label}', L{self.line_id}, [{self.start}, {self.end}]"
        if self.is_partnum:
            elements += ' **PN**'
        
        return_val_base = f"TargetNum({elements})"
        
        return return_val_base

def get_surrounding(lines, target_num):
    cols_slicer = slice(max(0, (target_num.start - 1)), min(len(lines[target_num.line_id])-1, (target_num.end + 1)))
    
    if target_num.line_id == 0:
        row_0 = '.' * len(target_num.label)
    else:
        row_0 = lines[max(0, target_num.line_id-1)][cols_slicer]

    row_1 = lines[target_num.line_id][cols_slicer]
    
    if target_num.line_id == len(lines)-1:
        row_2 = '.' * len(target_num.label)
    else:
        row_2 = lines[min(len(lines)-1, target_num.line_id+1)][cols_slicer]
    
    return ''.join((row_0, row_1, row_2))

def parse_numbers(lines):
    numbers = []
    for i, line in enumerate(lines):
        for matchobj in re.finditer('[0-9]+', line):
            match_num = {}
            target_num = TargetNum(
                line_id=i,
                label=matchobj.group(),
                start=matchobj.start(),
                end=matchobj.end())
            match_num['num'] = target_num
            match_num['surrounding'] = get_surrounding(lines, target_num)
            numbers.append(match_num)
    return numbers

def flag_partnumber(input_dict):
    output_dict = input_dict
    
    for num in input_dict:
        classified = ''.join([classify_char(x) for x in num['surrounding']])
        num['num'].is_partnum = CHAR_TYPES['symbol'] in classified
    
    return output_dict

# print(flag_partnumber(numbers))

def sum_of_non_partnumbers(numbers):
    non_partnumbers = [x for x in numbers if not x.is_partnumber]
    return sum(non_partnumbers)

def get_input(filepath):
    with open(filepath, 'r') as f:
        return [x.strip() for x in f.readlines()]

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--filepath')
    args = parser.parse_args()
    
    lines = get_input(args.filepath)

    # filepath = 'schematic_final.txt'