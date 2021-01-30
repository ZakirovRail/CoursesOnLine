# In this stage, you should write a program that:
#
# Reads 9 symbols from the input and writes an appropriate 3x3 field. Elements of the field can contain
# only 'X', 'O' and '_' symbols.
# Sets the field to a specific format, i.e. field should start and end with ---------, all lines in between
# should start and end with '|' symbol and everything in the middle should be separated with a single space.

origin_list = list(input())

line_1 = origin_list[0:3]
line_2 = origin_list[3:6]
line_3 = origin_list[6:]
print('---------')
print('|', ' '.join(line_1), '|')
print('|', ' '.join(line_2), '|')
print('|', ' '.join(line_3), '|')
print('---------')
