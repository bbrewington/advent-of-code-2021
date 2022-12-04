def read_newline_delim_file(filepath):
    test_input = []

    with open(filepath, 'r') as f:
        for line in f.readlines():
            line_val = line if line == '\n' else line.strip()
            test_input.append(line_val)

    return test_input
