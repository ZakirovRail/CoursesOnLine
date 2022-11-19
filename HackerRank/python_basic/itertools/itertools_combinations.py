from itertools import combinations

string, size = input().split(' ')

string = [char.upper() for char in string]
string.sort()
size = int(size)
combinations_list = []

for i in range(1, int(size+1)):
    new_iter_list = list(combinations(string, i))
    for j in new_iter_list:
        joined_chars = ''.join(j)
        combinations_list.append(joined_chars)

for joined_chars in combinations_list:
    print(joined_chars)