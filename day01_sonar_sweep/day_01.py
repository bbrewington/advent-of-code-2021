import pandas as pd

with open('input_data.txt') as f:
    input_data = [int(x.strip()) for x in f.readlines()]


def part_1():
    increased_count = 0

    for i, x_i in enumerate(input_data[:-1]):
        increased_count += 1 if input_data[i+1] > input_data[i] else 0

    return increased_count


print(f'Part 1 Answer: {part_1()}')

# Commenting out for now - not complete
# def part_2():
#     # TIL forward-looking rolling windows aren't straightforward in Pandas
#     indexer = pd.api.indexers.FixedForwardWindowIndexer(window_size=3)
#
#     return pd.Series(input_data).rolling(window=indexer, min_periods=1).sum()
#
#
# print(f'Part 2 Answer: {part_2()}')
