def get_input_data(filepath):
    """
    :param filepath: string
    :return: output_list [ [ [all 9 digits], [outputs] ], ... ]
    """
    output_list = []
    with open(filepath, 'r') as f:
        input_data_raw = f.readlines()
        for a in [x.strip() for x in input_data_raw]:
            b = [x.split(' ') for x in a.split(' | ')]
            output_list.append(b)
    return output_list


def code_parse(code, code_map):
    """
    :param code: string, subset of abcdefg
    :param code_map: dictionary, key is digit (0-9), value is set of segment ID's
    :return: code_map_element
    """
    c = frozenset(code) # converting to set so we can do intersections with it
    e = dict() # this is a dictionary that will be a single element of code_map

    if len(code) == 2:
        e[1] = c
    elif len(code) == 3:
        e[7] = c
    elif len(code) == 7:
        e[8] = c
    elif len(code) == 4:
        e[4] = c
    elif len(code) == 5:
        if len(c.intersection(code_map[1])) == 2:
            e[3] = c
        elif len(c.intersection(code_map[8] - code_map[9])) == 1:
            e[2] = c
        else:
            e[5] = c
    elif len(code) == 6:
        if len(c.intersection(code_map[4])) == 4:
            e[9] = c
        elif len(c.intersection(code_map[1])) == 2 \
                and len(c.intersection(code_map[4])) != 4:
            e[0] = c
        else:
            e[6] = c

    return e


input_data_test = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab'.split(' ')


def create_code_map(input_data_digits):
    """
    :param input_data_digits: list of strings
    :return: dictionary {letters: digit_int}
    """
    code_map = dict()

    # first run: do the easy ones (1-1 mapping via length)
    for a in [x for x in input_data_digits if len(x) in (2,3,4,7)]:
        code_map.update(code_parse(a, code_map))

    # second run: update the length 6's
    for a in [x for x in input_data_digits if len(x) == 6]:
        code_map.update(code_parse(a, code_map))

    # third run: update the length 5's
    for a in [x for x in input_data_digits if len(x) == 5]:
        code_map.update(code_parse(a, code_map))

    # same as code_map, but keys & values flipped, so it's letters: digit
    code_map2 = {v: k for k, v in code_map.items()}

    return code_map2


def part_1(filepath):
    """
    Part 1: In the output values, how many times do digits 1, 4, 7, or 8 appear?
    """
    test = get_input_data(filepath)

    result = []
    for x in test:
        result.append(sum([1 for y in x[1] if len(y) in [2,3,4,7]]))

    return sum(result)


def part_2(filepath):
    """
    Part 2: For each entry, determine all of the wire/segment connections
    and decode the four-digit output values.
    What do you get if you add up all of the output values?
    """
    input_data = get_input_data(filepath)

    output_list = []

    for i, line in enumerate(input_data):
        temp_list = []
        code_map = create_code_map(line[0])
        for digit in line[1]:
            temp_list.append(code_map[frozenset(digit)])
        outputs_converted = int(''.join([str(x) for x in temp_list]))
        output_list.append(outputs_converted)

    return sum(output_list)


print(f"part 1 answer: {part_1('input_data.txt')}")
print(f"part 2 answer: {part_2('input_data.txt')}")
