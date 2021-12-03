with open('input_data.txt', 'r') as f:
    input_data = [a.strip() for a in f.readlines()][0]


def parse_movement(a):
    x_shift, y_shift = 0, 0
    if a == 'v':
        y_shift = -1
    elif a == '^':
        y_shift = 1
    elif a == '<':
        x_shift = -1
    elif a == '>':
        x_shift = 1

    return x_shift, y_shift


def num_unique_val(list_input):
    return len([list(x) for x in set(tuple(x) for x in list_input)])


def part_1():
    x = 0
    y = 0
    all_positions = [[x, y]]

    for a in input_data:
        x_shift, y_shift = parse_movement(a)
        x += x_shift
        y += y_shift
        all_positions.append([x, y])

    return num_unique_val(all_positions)


print(f'part 1 answer: {part_1()}')

def part_2():
    positions = {
        'santa': [[0,0]],
        'robo_santa': [[0,0]]
    }

    instructions = {
        'santa': input_data[::2],
        'robo_santa': input_data[1::2]
    }

    for key, val in instructions.items():
        x = 0
        y = 0

        for a in val:
            x_shift, y_shift = parse_movement(a)
            x += x_shift
            y += y_shift
            positions[key].append([x, y])

    return num_unique_val(positions['santa'] + positions['robo_santa'])


print(f'part 2 answer: {part_2()}')