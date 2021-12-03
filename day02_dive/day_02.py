with open('input_data.txt', 'r') as f:
    input_data = [x.strip() for x in f.readlines()]


def part_1():
    position = {'horiz': 0, 'depth': 0}

    def move(instruction):
        instr_dir = instruction.split(' ')[0]
        instr_num = int(instruction.split(' ')[1])

        if instr_dir == 'forward':
            position['horiz'] += instr_num
        elif instr_dir == 'down':
            position['depth'] += instr_num
        elif instr_dir == 'up':
            position['depth'] -= instr_num

    for instr in input_data:
        move(instr)

    print(position)

    print(f"part 1 answer: {position['horiz'] * position['depth']}")


part_1()


def part_2():
    position = {'horiz': 0, 'depth': 0, 'aim': 0}

    def move(instruction):
        instr_dir = instruction.split(' ')[0]
        instr_num = int(instruction.split(' ')[1])

        if instr_dir == 'forward':
            position['horiz'] += instr_num
            position['depth'] += position['aim'] * instr_num
        elif instr_dir == 'down':
            position['aim'] += instr_num
        elif instr_dir == 'up':
            position['aim'] -= instr_num

    for instr in input_data:
        move(instr)

    print(position)

    print(f"part 2 answer: {position['horiz'] * position['depth']}")


part_2()
