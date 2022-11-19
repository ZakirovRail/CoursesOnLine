# class Base:
#     def __init__(self):
#         print('Base initializer')
#
#     def f(self):
#         print('Base.f()')
#
#
# b = Base()
# print(b)  # Base initializer
#
# print(b.f())  # Base.f()




# class Base:
#     def __init__(self):
#         print('Base initializer')
#
#     def f(self):
#         print('Base.f()')
#
#
# class Sub(Base):
#     def f(self):
#         print('Sub.f()')
#
#
# s = Sub()
# print(s)  # Base initializer
#
# print(s.f())  # Sub.f()



# ==============================================================================================================================

class Base:
    def __init__(self):
        print('Base initializer')

    def f(self):
        print('Base.f()')


class Sub(Base):

    def __init__(self):
        super().__init__()
        print('Sub initializer')

    def f(self):
        print('Sub.f()')


s = Sub()
print(s)
"""
Base initializer
Sub initializer
"""


print(s.f())  # Sub.f()

# ==============================================================================================================================







# ==============================================================================================================================




