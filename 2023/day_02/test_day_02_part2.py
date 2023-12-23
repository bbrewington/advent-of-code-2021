from day_02_part2 import find_cubes_needed_by_color, calc_power_of_list, part2

def test_calc_power(cube_info_expected_pairs):
    for input_expected in cube_info_expected_pairs:
        cube_info, expected_val = input_expected
        fewest_cubes = find_cubes_needed_by_color(cube_info)
        power = calc_power_of_list(fewest_cubes)
        assert power == expected_val

def test_part2():
    power_total = part2()
    
    assert power_total > 0
