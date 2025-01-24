import numpy as np


def get_input_data(filepath):
    with open(filepath, 'r') as f:
        all_data = [x.strip() for x in f.readlines()]

    draws = [int(x) for x in all_data[0].split(',')]

    boards_raw = all_data[2:]
    n_boards = int((len(boards_raw) + 1) / 6)

    boards = []
    for i in range(n_boards):
        row_start = 6 * i
        boards.append(boards_raw[row_start:(row_start+5)])

    boards2 = []
    for b in boards:
        y = [[int(q) for q in z.replace('  ', ' ').split(' ')] for z in b]
        boards2.append(y)

    return {'draws': draws,
            'boards': np.array(boards2)}


def get_match_state(board_array, cuml_draws):
    board_matrix = np.matrix(board_array)

    row_match = np.isin(board_matrix, cuml_draws).all(axis=1).any()
    col_match = np.isin(board_matrix, cuml_draws).all(axis=0).any()

    return any([row_match, col_match])

def get_sum_of_unmatched(board, cuml_draws):
    return board[np.logical_not(np.isin(board, cuml_draws))].sum()

def part_1(filepath):
    input_data = get_input_data(filepath)
    boards = input_data['boards']
    draws = input_data['draws']
    score_winning_board = None

    for d_i, d in enumerate(draws):
        cuml_draws = draws[0:d_i+1]
        for b_i, b in enumerate(boards):
            if get_match_state(b, cuml_draws):
                score_winning_board = get_sum_of_unmatched(b, cuml_draws)
                break

        if score_winning_board is not None:
            break

    assert score_winning_board is not None, 'Error: No winning boards found'

    return score_winning_board * d


def part_2(filepath):
    input_data = get_input_data(filepath)
    boards = input_data['boards']
    draws = input_data['draws']

    # Array, one element per board recording position in draws where it wins
    win_index = [None] * len(boards)

    for d_i, d in enumerate(draws):
        cuml_draws = draws[0:d_i+1]
        for b_i, b in enumerate(boards):
            is_match = get_match_state(b, cuml_draws)
            if is_match and win_index[b_i] is None:
                win_index[b_i] = d_i
        if win_index.count(None) == 0:
            break

    last_board_index = win_index.index(max(win_index))
    return get_sum_of_unmatched(boards[last_board_index], cuml_draws) * d

# print(part_1('input_data.txt'))
print(part_2('input_data.txt'))