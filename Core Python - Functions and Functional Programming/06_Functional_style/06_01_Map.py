# print(map(ord, 'The quick brown')) # <map object at 0x000002C89B7A6470>
# print(list(map(ord, 'The quick brown'))) # [84, 104, 101, 32, 113, 117, 105, 99, 107, 32, 98, 114, 111, 119, 110]
# print(set(map(ord, 'The quick brown'))) # {32, 98, 99, 101, 104, 105, 107, 110, 111, 113, 114, 84, 117, 119}
# print(tuple(map(ord, 'The quick brown'))) # (84, 104, 101, 32, 113, 117, 105, 99, 107, 32, 98, 114, 111, 119, 110)


#==========================================================================
# class Trace:
#     def __init__(self):
#         self.enabled = True
#     def __call__(self, f):
#         def wrap(*args, **kwargs):
#             if self.enabled:
#                 print('Calling {}'.format(f))
#             return f(*args, **kwargs)
#         return wrap
# result = map(Trace()(ord), 'The quick brown fox')
# print(result)
# print(next(result))
# print(next(result))
# print(next(result))
"""
<map object at 0x00000287AA58F6A0>
Calling <built-in function ord>
84
Calling <built-in function ord>
104
Calling <built-in function ord>
101
"""



#==========================================================================
# sizes = ['small', 'medium', 'large']
# colors = ['lavander', 'teal', 'burnt orange']
# animals = ['koala', 'platypus', 'salamander']
# def combine(size, color, animal):
#     return '{} {} {}'.format(size, color, animal)
# print(list(map(combine, sizes, colors, animals))) # ['small lavander koala', 'medium teal platypus', 'large burnt orange salamander']

#==========================================================================
# import itertools
#
# sizes = ['small', 'medium', 'large']
# colors = ['lavander', 'teal', 'burnt orange']
# animals = ['koala', 'platypus', 'salamander']
# def combine(quantity,size, color, animal):
#     return '{} x {} {} {}'.format(quantity, size, color, animal)
#
# print(list(map(combine, itertools.count(), sizes, colors, animals))) # ['0 x small lavander koala', '1 x medium teal platypus', '2 x large burnt orange salamander']

#==========================================================================
print([str(i) for i in range(5)]) # ['0', '1', '2', '3', '4']
print(list(map(str, range(5)))) # ['0', '1', '2', '3', '4']
