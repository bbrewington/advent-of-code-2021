with open('input_data.txt', 'r') as f:
    input_data = f.readline()


def part_1():
    return input_data.count('(') - input_data.count(')')


print(f'answer for part 1: {part_1()}')


def part_2():
    current_floor = 0
    for i, x in enumerate(input_data):
        current_floor += (1 if x == '(' else -1)
        if current_floor < 0:
            return i+1 # note: in the instructions, they 1-index


print(f'answer for part 2: {part_2()}')
