from day_01 import read_input, get_list_sum_diff

list1, list2 = read_input('input_example.txt')
assert get_list_sum_diff(list1, list2) == 11

list1_final, list2_final = read_input('input_final.txt')
print(get_list_sum_diff(list1_final, list2_final))
