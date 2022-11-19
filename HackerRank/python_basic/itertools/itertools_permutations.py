from itertools import permutations


string, size = input().split(' ')

string = [char for char in string]
size = int(size)

permutations_list = list(permutations(string, size))

joined_chars_list = ["".join(sub_list) for sub_list in permutations_list]
joined_chars_list.sort()
for joined_chars in joined_chars_list:
    print(joined_chars)