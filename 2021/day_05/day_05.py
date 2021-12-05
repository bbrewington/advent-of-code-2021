import numpy as np


def get_input_data(filepath):
    with open(filepath, 'r') as f:
        input_data = [x.strip() for x in f.readlines()]

    input_matrix = []
    for line in input_data:
        line_parsed1 = [int(x) for x in line.replace(' -> ', ',').split(',')]
        input_matrix.append(line_parsed1)

    return np.matrix(input_matrix)


def part_1(filepath):
    input_matrix = get_input_data(filepath)
    max_x = input_matrix[:,[0,2]].max()
    max_y = input_matrix[:,[1,3]].max()

    output_matrix = np.zeros(shape=(max_x+1, max_y+1), dtype=np.int8)

    for im in input_matrix:
        x1, y1, x2, y2 = im.tolist()[0]
        x1_temp, y1_temp, x2_temp, y2_temp = x1, y1, x2, y2

        if x1 > x2:
            x1 = x2_temp
            x2 = x1_temp
        elif y1 > y2:
            y1 = y2_temp
            y2 = y1_temp

        if x1 != x2 and y1 != y2:
            pass
        elif x1 == x2 or y1 == y2:
            output_matrix[y1:y2+1, x1:x2+1] += 1

    return (output_matrix > 1).sum()


print(f"part 1 answer: {part_1('input_data.txt')}")
