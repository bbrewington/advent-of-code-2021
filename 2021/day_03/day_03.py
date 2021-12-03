import numpy as np

with open('input_data.txt', 'r') as f:
    input_data = [x.strip() for x in f.readlines()]


def get_power_consumption(input_data):
    input_matrix = np.array([[int(a) for a in list(x)] for x in input_data])
    gamma_rate = ''
    epsilon_rate = ''

    for i in range(len(input_data[0])):
        digit = str(np.bincount(input_matrix[:,i]).argmax())
        gamma_rate += digit
        epsilon_rate += '1' if digit == '0' else '0'

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


print(f'part 1 answer: {get_power_consumption(input_data)}')
