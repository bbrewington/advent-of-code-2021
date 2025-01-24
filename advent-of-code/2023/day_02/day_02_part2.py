import pytest
import re

def get_input_data(filepath):
    with open(filepath, 'r') as f:
        game_info = []
        for line in f.readlines():
            line_cleaned = line.strip()
            game_part, roll_part = line_cleaned.split(': ')
            game_id = int(game_part[5:])
            cube_sets = roll_part.split('; ')
            cube_set_list = []
            for cube_set in cube_sets:
                cube_set_split = cube_set.split(', ')
                cube_dict = {}
                for cube in cube_set_split:
                    for color in ['red', 'green', 'blue']:
                        if cube.endswith(color):
                            cube_dict[color] = int(re.search(r'\d+', cube).group(0))
                # HACK: This for loop is garbage (re-iterating through same thing) - candidate for refactor
                for color in ['red', 'green', 'blue']:
                    if color not in cube_dict.keys():
                        cube_dict[color] = 0
                cube_set_list.append(cube_dict)
            game_info.append({'game_id': game_id, 'cube_info': cube_set_list})
    return game_info


def find_cubes_needed_by_color(cube_info):
    return_list = []
    for color in ['blue', 'green', 'red']:
        vals = []
        for cube_dict in cube_info:
          vals.append(cube_dict[color])
        return_list.append(max([x for x in vals if x != 0]))
    return return_list

def calc_power_of_list(fewest_cubes_list):
    return_val = 1
    for x in fewest_cubes_list:
        return_val *= x
    return return_val

def part2():
    input_data = get_input_data('input_data.txt')
    power_total = 0
    for input_entry in input_data:
        assert isinstance(input_entry, dict)
        assert isinstance(input_entry['cube_info'], list)
        cube_info = input_entry['cube_info']
        
        fewest_cubes = find_cubes_needed_by_color(cube_info)
        power_total += calc_power_of_list(fewest_cubes)
    
    return power_total

if __name__ == '__main__':
    print(part2())