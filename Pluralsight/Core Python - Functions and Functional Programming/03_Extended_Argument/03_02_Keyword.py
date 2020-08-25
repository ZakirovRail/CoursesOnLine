# def tag(name, **kwargs):
#     print(name)
#     print(kwargs)
#     print(type(kwargs))


# tag('img', src="Monet.jpg", alt="Sunrise by Claude Monet", border=1)

"""
img
{'src': 'Monet.jpg', 'alt': 'Sunrise by Claude Monet', 'border': 1}
<class 'dict'>
"""


#================================================================
# def tag(name, **attributes):
#     result = '<' + name
#     for key, value in attributes.items():
#         result += ' {k}="{v}"'.format(k=key, v=str(value))
#     result += '>'
#     return result


# print(tag('img', src="Monet.jpg", alt="Sunrise by Claude Monet", border=1))
"""
<img src="Monet.jpg" alt="Sunrise by Claude Monet" border="1">
"""
#================================================================
# def print_args(arg1, arg2, *args):
#     print(arg1)
#     print(arg2)
#     print(args)


# print_args(1,2,3,4,5,6,7)
"""
1
2
(3, 4, 5, 6, 7)
"""
#================================================================

# def print_args(arg1, arg2, *args, kwarg1, kwarg2):
#     print(arg1)
#     print(arg2)
#     print(args)
#     print(kwarg1)
#     print(kwarg2)


# print_args(1,2,3,4,5,10,15,20,kwarg1=6, kwarg2=7)
"""
1
2
(3, 4, 5, 10, 15, 20)
6
7
"""

#================================================================
#Positional-only Arguments
# def number_lenght(x, /):
#     return len(str(x))

# print(number_lenght(2112))  # 4

# print(number_lenght(x=31557600))
"""
TypeErro:number_lenght() got some positional-only arguments passed as keyword arguments: 'x'
"""

#================================================================






#================================================================


#================================================================