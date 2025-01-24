import urllib.request
import ssl

def read_newline_delim_file(filepath, access_type):
    """Read newline-delimited file from a path

    Args:
        filepath (str): Either local file path or url
        access_type (str): 'local' or 'web'

    Returns:
        test_input: List[str]
    """

    test_input = []
    
    if access_type == 'local':
        with open(filepath, 'r') as f:
            for line in f.readlines():
                line_val = line if line == '\n' else line.strip()
                test_input.append(line_val)

    elif access_type == 'web':
        # Had to do this b/c certificate not found error
        ssl._create_default_https_context = ssl._create_unverified_context
        
        for line in urllib.request.urlopen(filepath):
            line_val = line if line == '\n' else line.strip()
            if line_val == '':
                # test_input.append('\n')
                print('blank')
            else:
                print('not blank')
                # test_input.append(line_val.decode('utf-8'))

    # return test_input


url_base = "https://raw.githubusercontent.com/bbrewington/advent-of-code/main/2022/docs"
subfolder = "day_01"
filename = "example_input.txt"

url = '/'.join([url_base, subfolder, filename])

read_newline_delim_file(url, 'web')
read_newline_delim_file('/Users/brentbrewington/github/advent-of-code/2022/docs/day_01/example_input.txt', 'local')
