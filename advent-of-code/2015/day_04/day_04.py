import hashlib


def get_input(filepath):
    with open(filepath, 'r') as f:
        return [x.strip() for x in f.readlines()][0]


def get_hash_hex(secret, number):
    combined = secret + str(number)
    combined_bytes = combined.encode('utf-8')
    return hashlib.md5(combined_bytes).hexdigest()


def check_zeros(s, num_zeros):
    return s[0:num_zeros] == '0' * num_zeros


def find_num(filepath, max_num, num_zeros):
    input_secret = get_input(filepath)

    for i in range(max_num):
        test = check_zeros(get_hash_hex(input_secret, i), num_zeros)
        if test:
            return i

    print(f'i: {i}, no match found')


print(f"part 1 answer: {find_num('input_data.txt', 1000000, 5)}")
print(f"part 2 answer: {find_num('input_data.txt', 5000000, 6)}")
