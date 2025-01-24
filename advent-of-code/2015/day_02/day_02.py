from typing import List

with open('input_data.txt', 'r') as f:
    # leaving next line as a terse list comprehension of list comprehension.  deal with it :)
    # converts each LxWxH entry into a list of integers --> making list of lists of 3 integers
    input_data = [[int(b) for b in a.strip().split('x')] for a in f.readlines()]


def part_1():
    def box_surface_area(input_dims: List[int]) -> int:
        L, W, H = input_dims
        side_areas = [(2 * L * W), (2 * L * H), (2 * W * H)]

        return sum(side_areas) + (min(side_areas) / 2)

    total_paper = 0

    for x in input_data:
        total_paper += box_surface_area(x)

    return int(total_paper)


print(f'part 1 answer: {part_1()}')


def part_2():
    def ribbon_length(input_dims: List[int]) -> int:
        L, W, H = input_dims
        side_perimeters = [2 * (L + W), 2 * (L + H), 2 * (W + H)]
        volume = L * W * H

        return min(side_perimeters) + volume

    total_ribbon = 0

    for x in input_data:
        total_ribbon += ribbon_length(x)

    return total_ribbon


print(f'part 2 answer: {part_2()}')