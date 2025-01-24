def solution_runner(func_name, input_file, expect_value):
    try:
        assert func_name(input_file) == expect_value, 'fail'
    except AssertionError as error:
        return error
    else:
        return 'pass'
