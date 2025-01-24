import numpy as np


def get_input_data(filepath):
    output_list = []
    with open(filepath, 'r') as f:
        for line in f.readlines():
            output_list.append([int(x) for x in line.strip()])
    return np.array(output_list)


def convert_indices(list_of_lists):
    """
    convert [i_0, j_0], [i_1, j_1], [i_2, j_2] --> [i_0, i_1, i_2], [j_0, j_1, j_2]
    """
    return tuple([x for x in zip(*list_of_lists)])

def get_surrounding_indices(input_data, i, j):
    """
    :param input_data: 2-D integer array
    :param i: row index of input point
    :param j: col index of input point
    :return: surrounding indices in all 4 directions
    """
    above = [i-1, j] if i-1 >= 0 else None
    left = [i, j-1] if j-1 >= 0 else None
    right = [i, j+1] if j+1 <= input_data.shape[1]-1 else None
    below = [i+1, j] if i+1 <= input_data.shape[0]-1 else None

    return above, left, right, below


def get_local_minima(input_data):
    """
    :param input_data: 2-D integer array
    :return: dict: {(i, j): x_ij}
        (i, j) is index of local minimum; x_ij is value at that point
    """
    output = {}

    # for each i, j in input_data:
    for i in range(input_data.shape[0]):
        for j in range(input_data.shape[1]):
            above, left, right, below = get_surrounding_indices(input_data, i, j)
            x_ij = int(input_data[i, j])
            # get surrounding points (filter out if invalid point, i.e. None)
            surrounding_points = input_data[convert_indices([x for x in [above, left, right, below] if x is not None])]
            # check if all surrounding points are greater than x_ij
            if all(surrounding_points > x_ij):
                # if yes, add point to output dict
                output.update({(i, j): x_ij})
    return output

def part_1(filepath):
    """
    The risk level of a low point is 1 plus its height.
    Find all of the low points on your heightmap.
    What is the sum of the risk levels of all low points on your heightmap?
    """
    input_data = get_input_data(filepath)
    local_minima = get_local_minima(input_data)
    return sum([x+1 for x in local_minima.values()])

def get_surr_indices_not9(input_data, i, j):
    """
    :param input_data: 2-D integer array
    :param i: row index of input_data
    :param j: column index of input_data
    :return: tuple of tuples of surrounding indices (except for 9 values in input_data)
    """
    return tuple([tuple(x) for x in get_surrounding_indices(input_data, i, j) if x is not None and input_data[tuple(x)] != 9])

def traverse_basin(input_data, index_of_min):
    """
    :param input_data: 2-D integer array
    :param index_of_min: tuple (i, j) of index of local minima
    :return: visited, a set of tuples of indices of visited locations
    """
    visited = set()
    to_visit = set()
    i = 1
    while i <= 10000:
        if i == 1:
            current_index = index_of_min
        visited.add(current_index)
        surrounding_indices = get_surr_indices_not9(input_data, *current_index)
        for x in surrounding_indices:
            to_visit.add(x)
        queue = to_visit - visited
        if len(queue) == 0:
            break
        else:
            current_index = list(queue)[0]
        i += 1

    return visited

def part_2(filepath):
    """
    What do you get if you multiply together the sizes of the three largest basins?
    """
    input_data = get_input_data(filepath)
    local_minima = get_local_minima(input_data)

    basin_sizes = []
    # loop through local minima
    for index_of_min in local_minima:
        basin_sizes.append(len(traverse_basin(input_data, index_of_min)))
    basin_sizes.sort(reverse=True)
    basin_size_mult = 1
    for b in basin_sizes[0:3]:
        basin_size_mult *= b
    return basin_size_mult


print(f"part 1 answer: {part_1('input_data.txt')}")
print(f"part 2 answer: {part_2('input_data.txt')}")