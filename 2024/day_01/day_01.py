def read_input(file):
    list1, list2 = [], []
    with open(file, 'r') as f:
        file_contents = f.readlines()
        for line in file_contents:
            line_split = line.strip().split(' ')
            list1.append(int(line_split[0]))
            list2.append(int(line_split[-1]))
    return sorted(list1), sorted(list2)

def get_list_sum_diff(list1, list2):
    assert len(list1) == len(list2), "lists have different length"
    return sum(abs(list2[i] - list1[i]) for i in range(len(list1)))
