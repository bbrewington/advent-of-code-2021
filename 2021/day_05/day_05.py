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


def get_input_data_part2(filepath):
    with open(filepath, 'r') as f:
        input_data = [x.strip() for x in f.readlines()]

    input_matrix = []
    for line in input_data:
        line_parsed1 = [int(x) for x in line.replace(' -> ', ',').split(',')]
        input_matrix.append(line_parsed1)
    input_matrix = np.matrix(input_matrix)
    max_x = input_matrix[:,[0,2]].max()
    max_y = input_matrix[:,[1,3]].max()
    max_dim = max(max_x, max_y)
    output_matrix = np.zeros(shape=(max_dim+1, max_dim+1), dtype=np.int8)

    return np.matrix(input_matrix), output_matrix


def part_2(filepath):
    input_matrix, output_matrix = get_input_data_part2(filepath)

    for im in input_matrix:
        x1, y1, x2, y2 = im.tolist()[0]

        # could probably combine these chunks better, but they work for now
        if x1 != x2:
            x_dir = int((x2 - x1) / abs(x2 - x1))
            x_iter = [a for a in range(x1, x2+x_dir, x_dir)]
        else:
            x_iter = [x1]

        if y1 != y2:
            y_dir = int((y2 - y1) / abs(y2 - y1))
            y_iter = [a for a in range(y1, y2+y_dir, y_dir)]
        else:
            y_iter = [y1]

        if x1 != x2:
            for x_i, x in enumerate(x_iter):
                y = y_iter[x_i] if y1 != y2 else y1
                output_matrix[y, x] += 1
        elif y1 != y2:
            for y_i, y in enumerate(y_iter):
                x = x1
                output_matrix[y, x] += 1

    return len(output_matrix[output_matrix > 1])


print(f"part 1 answer: {part_1('input_data.txt')}")
print(f"part 2 answer: {part_2('input_data.txt')}")