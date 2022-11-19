# def hypervolume(*args):
#     print(args)
#     print(*args)
#     print(type(args))
#
#
# print(hypervolume(3, 4, 5))

# ====================================================================================================
# def hypervolume_2(*lengths):
#     i = iter(lengths)
#     v = next(i)
#     for length in i:
#         v *= length
#     return v
#
#
# print(hypervolume_2(2, 4))
# print(hypervolume_2(2, 4, 6))
# print(hypervolume_2(2, 4, 6, 8))
# ====================================================================================================
# def hypervolume_3(length, *lengths):
#     v = length
#     for item in lengths:
#         v *= item
#     return v
#
#
# print(hypervolume_3(2, 4))
# print(hypervolume_3(2, 4, 6))
# print(hypervolume_3(2, 4, 6, 8))
# ====================================================================================================
# def tag(name, **kwargs):
#     print(name)
#     print(kwargs)
#     print(type(kwargs))
#
# tag('img', src='monet.jpg', alt='Sunrise by Claude Monet', border = 1)
# ====================================================================================================

# def tag(name, **attributes):
#     result = '<' + name
#     for key, value in attributes.items():
#         result += ' {k}="{v}"'.format(k=key, v=value)
#     result += '>'
#     return result
#
# print(tag('img', src='monet.jpg', alt='Sunrise by Claude Monet', border = 1))
# ====================================================================================================

# def trace(f, *args, **kwargs):
#     print("args =", args)
#     print("kwargs =", kwargs)
#     result = f(*args, **kwargs)
#     print("result =", result)
#     return result
#
# print(int("ff", base=16))
#
# print(trace(int, "ff", base=16))
# ====================================================================================================
sunday = [12, 14, 15, 15, 17, 21, 22, 23, 22, 20, 18]
monday = [13, 14, 14, 14, 16, 20, 21, 20, 21, 19, 17]

# for item in zip(sunday, monday):
#     print(item)

tuesday = [7,8,9,7,8,9,8,9,11,12]

daily = [sunday, monday, tuesday]
from pprint import pprint as pp

print(daily)
pp(daily)

for item in zip(daily[0], daily[1], daily[2]):
    print(item)
print("-"*50)
for item in zip(*daily):
    print(item)
print("-"*50)
transposed = list(zip(*daily))
pp(transposed)

