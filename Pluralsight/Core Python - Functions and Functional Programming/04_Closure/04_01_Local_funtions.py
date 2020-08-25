#Local functions - functions defined within other function

# def sort_by_lst_letter(strings):
#     def last_letter(s):
#         return s[-1]
#     return sorted(strings, key=last_letter)

# print(sort_by_lst_letter(['hello', 'from', 'a', 'local', 'function']))  # ['a', 'local', 'from', 'function', 'hello']


#================================================================
# def sort_by_lst_letter(strings):
#     def last_letter(s):
#         return s[-1]
#     print(last_letter)
#     return sorted(strings, key=last_letter)

# print(sort_by_lst_letter(['hello', 'from', 'a', 'local', 'function']))
"""
<function sort_by_lst_letter.<locals>.last_letter at 0x000002BD342A5A60>
['a', 'local', 'from', 'function', 'hello']
"""

#================================================================
# Scoping rules for names
# LEGB - Local, Enclosing, Global, BuiltIn

# g = 'global'
# def outer(p='param'):
#     l = 'local'
#     def inner():
#         print(g,p,l)
#     inner()

# outer()  # global param local

#================================================================
#Returning Local Functions
def enclosing():
    def local_func():
        print('local func')
    return local_func()

enclosing()  # local func





#================================================================





#================================================================