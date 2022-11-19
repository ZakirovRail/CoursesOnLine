from itertools import groupby

string_input = input()
# string_input = '1222311'
test_tuple = []

for k, g in groupby(string_input):
    test_tuple.append((len(list(g)), int(k)))
print(*test_tuple)
