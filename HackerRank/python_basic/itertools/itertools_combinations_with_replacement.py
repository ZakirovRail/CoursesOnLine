from itertools import combinations_with_replacement

string, size = input().split(' ')

string = [char.upper() for char in string]
string.sort()
size = int(size)
combinations_list = []


new_iter_list = list(combinations_with_replacement(string,size))

for j in new_iter_list:
    joined_chars = ''.join(j)
    combinations_list.append(joined_chars)

for joined_chars in combinations_list:
    print(joined_chars)