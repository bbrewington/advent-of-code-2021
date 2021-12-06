def get_input_data(filepath):
    with open(filepath, 'r') as f:
        return [int(x) for x in f.readline().strip().split(',')]

def part_1(filepath, max_days):
    input_data = get_input_data(filepath)
    L = input_data.copy()

    for i in range(1, max_days+1):
        L = [x - 1 for x in L]
        num_negative = L.count(-1)
        L = L + [8] * num_negative
        L = list(map(lambda x: 6 if x<0 else x, L))

    return len(L)

# for part 2 had to re-design without all the for loops
def part_2(filepath, max_days):

    input_data = get_input_data(filepath)

    f = [input_data.count(i) for i in range(9)]
    for i in range(max_days):
        f.append(f.pop(0))
        f[6] += f[8]

    return(sum(f))

print(f"part 1 answer: {part_1('input_data.txt', 80)}")
print(f"part 2 answer: {part_2('input_data.txt', 256)}")