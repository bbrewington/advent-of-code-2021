import string

CHAR_TYPES =  {'blank': '.', 'digit': '#', 'symbol': '$'}

def read_input_data(filepath):
    with open(filepath, 'r') as f:
        lines = [x.strip() for x in f.readlines()]
    return lines

class Schematic:
    def __repr__(self) -> str:
        return_val = ''
        for i in range(len(self.lines)):
            return_val += self.lines[i] + '  '
            return_val += self.symbol_mask[i] + '  ' + self.partnumber_mask[i] + '\n'
            
        return return_val
    
    def __init__(self, filepath):
        with open(filepath, 'r') as f:
            lines = [x.strip() for x in f.readlines()]
        self.lines = lines
        self.symbol_mask = self._make_symbol_mask()
        self.partnumber_mask = self._make_partnumber_mask()
    
    def get_symbols(self):
        chars = set(''.join(self.lines))
        symbols = chars.difference(set(string.digits))
        symbols.remove('.')
        
        return symbols
    
    def classify_char(self, x):
        if x == CHAR_TYPES['blank']:
            return CHAR_TYPES['blank']
        elif x in string.digits:
            return CHAR_TYPES['digit']
        else:
            return CHAR_TYPES['symbol']
    
    def _make_symbol_mask(self):
        symbol_mask = []
        for row in self.lines:
            mask = ''.join([self.classify_char(x) for x in row])
            symbol_mask.append(mask)
        return symbol_mask
    
    def _subset_symbol_mask(self, i, j):
        num_rows = len(self.symbol_mask)
        num_cols = len(self.symbol_mask[0])
        a = 0 if j == 0 else j-1
        b = num_cols-1 if j == num_cols-1 else j+1
        c = 0 if i == 0 else i-1
        d = num_rows-1 if i == num_rows-1 else i+1
        
        result_subset = [row[a:b+1] for row in self.symbol_mask[c:d+1]]
        
        return result_subset

    def _make_partnumber_mask(self):
        partnumber_mask = []
        num_cols = len(self.symbol_mask[0])
        for i, row in enumerate(self.symbol_mask):
            partnumber_mask.append([False for _ in range(num_cols)])
            for j in range(len(row)):
                subset = self._subset_symbol_mask(i, j)
                partnumber_mask[i][j] = CHAR_TYPES['symbol'] in subset
        return partnumber_mask

sample = Schematic('schematic_sample.txt')
