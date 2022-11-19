# Touples

# def minmax(items):
#     return min(items), max(items)
#
#
# print(minmax([83, 16, 5, 1, -6, 100]))  # (-6, 100)
# lower, upper = minmax([83, 16, 5, 1, -6, 100])
# print(lower)  # -6
# print(upper)  # 100
#
# (a, (b, (c, d))) = (4, (3, (2, 1)))
# print('a ==', a, '\n', 'b ==', b, '\n', 'c ==', c, '\n', 'd ==', d)
# =====================================================================
# a = 'jelly'
# b = 'bean'
# a, b = b, a
# print(a)  # bean
# print(b)  # jelly
# =====================================================================

# String

# c = 'unforgetable'
# l = c.partition('forget')
# print(l)  # ('un', 'forget', 'able')
#
# departure, separator, arrival =  "London:Edinburg".partition(':')
# print(departure, arrival)  # London Edinburg
#
#
# origin, _, destination = "Seattle-Boston".partition('-')
# print(origin, destination)  # Seattle Boston
#
#
# import datetime
# print(f'The current time is {datetime.datetime.now().isoformat()}')  # example The current time is 2021-05-29T15:43:20.513388
#
# import math
# print(f'Math constants: pi = {math.pi:.3f}, e = {math.e:.6f}')  # Math constants: pi = 3.142, e = 2.718282

# =====================================================================

# Ranges
# li = list(range(5, 9))
# print(li)  # [5, 6, 7, 8]
#
# pi = list(range(2, 9, 2))
# print(pi)  # [2, 4, 6, 8]
#
# t = [6, 372, 8862, 148800, 2096886]
# for i, v in enumerate(t):
#     print(f"i = {i}, v = {v}")
"""
i = 0, v = 6
i = 1, v = 372
i = 2, v = 8862
i = 3, v = 148800
i = 4, v = 2096886
"""
# =====================================================================

# Lists



# =====================================================================

# Dictionaries

# name_and_ages = [('Alice', 32), ('Bob', 48), ('Charlie', 28), ('Daniel', 33)]
# d = dict(name_and_ages)
# print(d)  # {'Alice': 32, 'Bob': 48, 'Charlie': 28, 'Daniel': 33}
#
# phonetic = dict(a='alfa', b='bravo', c='charlie')
# print(phonetic)  # {'a': 'alfa', 'b': 'bravo', 'c': 'charlie'}
#
# for key in phonetic:
#     print(f'{key} - {phonetic[key]}')
# """
# a - alfa
# b - bravo
# c - charlie
# """
#
# for value in phonetic.values():
#     print(value)
# """
# alfa
# bravo
# charlie
# """
#
# for key in phonetic.keys():
#     print(key)
# """
# a
# b
# c
# """
#
#
# for key, value in phonetic.items():
#     print(f'{key} - {value}')
# """
# a - alfa
# b - bravo
# c - charlie
# """

# =====================================================================

# Set








