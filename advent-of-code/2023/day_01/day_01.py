from argparse import ArgumentParser

def get_newline_delim(filepath, remove_trailing_newline=True):
    with open(filepath, 'r') as f:
        lines = f.read().split('\n')
        if remove_trailing_newline:
            if lines[-1] == '':
                lines.pop()
    return lines

def get_first_last_digit_part1(input_string):
    digits_dict = {} # {position: digit} (e.g. {3: 1})
    
    for i, x in enumerate(input_string):
        if x.isnumeric():
            digits_dict[i] = int(x)
    
    first_digit = digits_dict[min(digits_dict.keys())]
    last_digit = digits_dict[max(digits_dict.keys())]
    
    return first_digit*10 + last_digit

def str_digit_pos(input_string, digits_str=['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
    result = {} # {digit: pos}
    for d in digits_str:
        if d in input_string:
            result[d].append()
    min_pos = min([input_string.find(s) for s in digits_str if s in input_string])
    max_pos = max([input_string[::-1].rfind(s[::-1]) for s in digits_str if s in input_string])
    return min_pos, max_pos
    
def get_first_last_digit_part2(input_string):
    digits_int = [x for x in '1234567890']
    digits_str = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    digits = [{'str': k, 'str_len': len(k), 'int': v, 'locs': []} for k, v in dict(zip(digits_str, digits_int)).items()]
    for digit_key, x in enumerate(digits):
        for string_pos in range(len(input_string)):
            if input_string[string_pos:string_pos+x['str_len']] == x['str'] or input_string[string_pos] == x['int']:
                digits[digit_key]['locs'].append(string_pos)
    
    all_string_pos = []
    for x in digits:
        all_string_pos.extend(x['locs'])
    
    min_string_pos, max_string_pos = min(all_string_pos), max(all_string_pos)
    
    first_digit = None
    last_digit = None
    for x in digits:
        first_digit = int(x['int']) if min_string_pos in x['locs'] else first_digit
        last_digit = int(x['int']) if max_string_pos in x['locs'] else last_digit
    
    return first_digit*10 + last_digit

def parse_input_data(input_data, question_part):
    # print(input_data)
    result_list = []
    for _, x in enumerate(input_data):
        # print(i, x)
        if question_part == 1:
            result_list.append(get_first_last_digit_part1(x))
        elif question_part == 2:
            result_list.append(get_first_last_digit_part2(x))
    return result_list

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--run-full', type=str, choices=['yes', 'no'])
    parser.add_argument('--part', type=int)
    args = parser.parse_args()
    
    input_data_test = get_newline_delim(f'input_data_test_part{args.part}.txt')
    print(f'Test Data: Part {args.part}')
    print(sum(parse_input_data(input_data_test, question_part=args.part)))

    if args.run_full == 'yes':
        input_data = get_newline_delim('input_data.txt')
        print(sum(parse_input_data(input_data, question_part=args.part)))
