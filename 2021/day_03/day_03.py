import numpy as np
from collections import Counter


def get_input_data(filepath):
    with open(filepath, 'r') as f:
        return [x.strip() for x in f.readlines()]


def format_input_array(list_of_binary):
    return np.array([[int(a) for a in list(x)] for x in list_of_binary])

##########
# Part 1 #
##########

def get_power_consumption(filepath):
    list_of_binary = get_input_data(filepath)
    input_array = format_input_array(list_of_binary)

    gamma_rate = ''
    epsilon_rate = ''

    # loop through each character (assume all are same length)
    for i in range(len(list_of_binary[0])):
        # get most common 0/1 value for each character
        digit = str(np.bincount(input_array[:,i]).argmax())
        gamma_rate += digit
        epsilon_rate += '1' if digit == '0' else '0'

    return int(gamma_rate, 2) * int(epsilon_rate, 2)

##########
# Part 2 #
##########
# Ran into some issues with np.bincount, so decided to do this part w/ lists


def get_binary_value_by_mode(filepath, mode):
    assert mode in ['oxygen', 'co2'], 'Error: mode must be one of oxygen, co2'

    input_data = get_input_data(filepath)
    input_data_filtered = input_data.copy()
    # loop through bit positions
    for i in range(len(input_data_filtered[0])):
        # get values in current bit position
        values_current_pos = [x[i] for x in input_data_filtered]

        # find most/least common value in current bit position
        count_values = Counter(values_current_pos)

        if count_values['0'] == count_values['1']:
            most_least_common = '1' if mode == 'oxygen' else '0'
        else:
            # get key of dict count_values that has max value
            # taken from: https://stackoverflow.com/a/268285
            if mode == 'oxygen':
                most_least_common = max(count_values, key=lambda key: count_values[key])
            elif mode == 'co2':
                most_least_common = min(count_values, key=lambda key: count_values[key])

        # keep only numbers with that bit in that position
        input_data_filtered = [x for x in input_data_filtered if x[i] == most_least_common]

        # exit loop if single entry remaining
        if len(input_data_filtered) == 1:
            break

    assert len(input_data_filtered) == 1, 'Error: Must return 1 value'

    return int(input_data_filtered[0], 2)


def get_life_support_rating(filepath):
    return get_binary_value_by_mode(filepath, 'oxygen') * get_binary_value_by_mode(filepath, 'co2')


if __name__ == '__main__':
    print(f"part 1 answer: {get_power_consumption('input_data.txt')}")
    print(f"part 2 answer: {get_life_support_rating('input_data.txt')}")
