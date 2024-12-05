from collections import Counter

def read_input(file_path):
    with open(file_path, 'r') as f:
        file_contents = f.readlines()
        return_list = [[int(x) for x in line.strip().split(' ')] for line in file_contents]
    return return_list

def inc_dec(x1, x2):
    if x1 == x2:
        return 0
    elif x2 > x1:
        return 1
    else:
        return -1

def check_part1_rules(list1):
    check_val = 'Safe'
    # The levels are either all increasing or all decreasing.
    # Any two adjacent levels differ by at least one and at most three.
    for i, (item1, item2) in enumerate(zip(list1, list1[1:])):
        # print(f"i: {i}, item1: {item1}, item2: {item2}")
        check_val = 'Safe'
        
        if not(1 <= abs(item1 - item2) <= 3):
            # print("Failed diff 1 to 3 rule")
            check_val = 'Unsafe'
            break
        
        my_inc_dec = inc_dec(item1, item2)
        if my_inc_dec == 0:
            # print("Failed always inc/dec rule")
            check_val = 'Unsafe'
            break
        
        if i == 0:
            list1_inc_dec = my_inc_dec
        
        if my_inc_dec != list1_inc_dec:
            # print("Failed monotonic rule")
            check_val = 'Unsafe'
            break
        
    return check_val

def count_part1_safe(input_data):
    return sum(check_part1_rules(row) == 'Safe' for row in input_data)
