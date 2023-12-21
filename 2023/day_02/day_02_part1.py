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
                            cube_dict[color] = int(re.search('\d+', cube).group(0))
                # HACK: This for loop is garbage (re-iterating through same thing) - candidate for refactor
                for color in ['red', 'green', 'blue']:
                    if color not in cube_dict.keys():
                        cube_dict[color] = 0
                cube_set_list.append(cube_dict)
            game_info.append({'game_id': game_id, 'cube_info': cube_set_list})
    return game_info

game_info = get_input_data('input_data.txt')

cube_capacity = {'red': 12, 'green': 13, 'blue': 14}

for i, game in enumerate(game_info):
    print(f"game: {game['game_id']}")
    game_info[i]['cube_set_capacity_tests'] = []
    for cube_set in game['cube_info']:
        # True means test fails
        test = any([cube_set[color] > cube_capacity[color] for color in ['red', 'green', 'blue']])
        game_info[i]['cube_set_capacity_tests'].append(test)
    game_info[i]['game_is_possible'] = not(any(game_info[i]['cube_set_capacity_tests']))

possible_game_ids = [game['game_id'] for game in game_info if game['game_is_possible'] == True]

print(sum(possible_game_ids))
