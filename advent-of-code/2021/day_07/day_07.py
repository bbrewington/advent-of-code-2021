def get_input_data(filepath):
    with open(filepath, 'r') as f:
        return [int(x) for x in f.readline().strip().split(',')]

input_data = get_input_data('input_data.txt')

def sum_of_n(n):
    return int((n * (1 + n)) / 2)

def distance_int_to_list(x, L):
    return sum([abs(x - a) for a in L])

def part_1():
    distances = []
    for x in input_data:
        distances.append(distance_int_to_list(x, input_data))
    return min(distances)

def part_2():
    distances = []
    for x in range(1, len(input_data)):
        # print(x)
        elements = [sum_of_n(abs(x - a)) for a in input_data]
        # print(elements)
        total = sum(elements)
        distances.append(total)
    return min(distances)

print(f"part 1 answer: {part_1()}")
print(f"part 2 answer: {part_2()}")
