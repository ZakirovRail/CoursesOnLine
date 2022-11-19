# list_comp = [i * 2 for i in range(10)]
# print(list_comp)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
#
# dict_compr = {i: i * 2 for i in range(10)}
# print(dict_compr)  # {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18}
#
# set_compr = {i * 2  for i in range(10)}
# print(set_compr)  # {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}
#
# generator_compr = (i for i in range(10))
# print(*generator_compr)  # 0 1 2 3 4 5 6 7 8 9
#
# compl_compr = [(x, y) for x in range(5) for y in range(3)]
# print(compl_compr)  # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2)]

# ==============================================================================================================================
# difficult to read
# values = [x / (x - y) for x in range(100) if x > 50 for y in range(100) if x - y != 0]
# print(values)

# better to read
# values = [x / (x - y)
#           for x in range(100)
#           if x > 50
#           for y in range(100)
#           if x - y != 0]
# print(values)

# # another way
# values = []
# for x in range(100):
#     if x > 50:
#         for y in range(100):
#             if x - y != 0:
#                 values.append(x / (x - y))


# another example
example_2 = [(x, y) for x in range(10) for y in range(x)]
result = []
for x in range(10):
    for y in range(x):
        result.append((x, y))

print(result)














