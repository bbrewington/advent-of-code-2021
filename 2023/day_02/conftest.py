import pytest

@pytest.fixture()
def cube_info_expected_pairs():
    return_val = [(
        [ {'blue': 3, 'green': 0, 'red': 4},
          {'blue': 6, 'green': 2, 'red': 1},
          {'blue': 0, 'green': 2, 'red': 0}],
    48),
    (
        [{'blue': 1, 'green': 2, 'red': 0},
          {'blue': 4, 'green': 3, 'red': 1},
          {'blue': 1, 'green': 1, 'red': 0}],
    12),
    (   [{'blue': 6, 'green': 8,  'red': 20},
          {'blue': 5, 'green': 13, 'red': 4},
          {'blue': 0, 'green': 5,  'red': 1}],
    1560),
    (
        [{'blue': 6,  'green': 1, 'red': 3},
          {'blue': 0,  'green': 3, 'red': 6},
          {'blue': 15, 'green': 3, 'red': 14}],
    630),
    (   [{'blue': 1, 'green': 3, 'red': 6},
          {'blue': 2, 'green': 2, 'red': 1}],
    36)
    ]
    
    return return_val

@pytest.fixture()
def cube_info_input(cube_info_expected_pairs):
    return [x[0] for x in cube_info_expected_pairs]

@pytest.fixture()
def expected(cube_info_expected_pairs):
    return [x[1] for x in cube_info_expected_pairs]
