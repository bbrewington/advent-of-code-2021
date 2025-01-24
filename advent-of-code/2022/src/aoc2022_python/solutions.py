from utility import read_input_file, directory_operations, runners

git_root = directory_operations.get_git_root()
docs_path = git_root / '2022/docs'

def day_01(input_filename):
    day_01_docs_path = docs_path / 'day_01'
    example_input = read_input_file.read_newline_delim_file(day_01_docs_path / input_filename)
    
    # This feels kind of hacky, but found string strip/split/join method the most elegant
    list_of_chunks = []
    list_of_pipe_delim_string_chunks = [x.strip('|') for x in '|'.join(example_input).split('\n')]
    for string_chunk in list_of_pipe_delim_string_chunks:
        list_of_chunks.append([int(y) for y in string_chunk.split('|')])
    
    return max([sum(x) for x in list_of_chunks])

if runners.solution_runner(day_01, 'example_input.txt', 24000) == 'pass':
    print(f"Day 1 test(s) passed! Answer: {day_01('input.txt')}")
else:
    print('Day 1 test(s) failed, need to fix')
