from day_03_part1 import Schematic
import pytest

# 'd': digit, 'b': blank (includes '.'), 's': symbol (i.e. not ".")
@pytest.fixture()
def symbol_mask_input():
  return [
  '###..###..',
  '...$......',
  '..##..###.',
  '......$...',
  '###$......',
  '.....$.##.',
  '..###.....',
  '......###.',
  '...$.$....',
  '.###.###..'
]

@pytest.fixture()
def schematic_sample():
    return Schematic('schematic_sample.txt')

def test_get_adjacent_mask(schematic_sample):
    sample = schematic_sample
    
@pytest.fixture()
def symbols():
    return {'=', '@', '&', '$', '%', '+', '/', '-', '#', '*'}

def test_get_symbols(schematic_sample, symbols):
    schematic_sample_symbols = schematic_sample.get_symbols()
    print(schematic_sample_symbols)
    assert schematic_sample.get_symbols().issubset(symbols)

@pytest.mark.parametrize("row_id,col_id,expected", [
    (0, 0, ['##', '..']),
    (1, 1, ['###', '...', '..#']),
    (2, 2, ['..$', '.##', '...']),
    (1, 0, ['##', '..', '..']),
    (9, 9, ['..', '..']),
    (8, 8, ['##.', '...', '#..'])
])
def test__subset_symbol_mask(schematic_sample, row_id, col_id, expected):
    assert schematic_sample._subset_symbol_mask(i=row_id, j=col_id) == expected

@pytest.mark.parametrize("symbol_mask,partnumber_mask", [
    
])
def test__make_adjacent_mask():
    assert True