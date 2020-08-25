# def hello():
#     "Print a well-known message."
#     print('Hello, world !')
#
# print(hello.__name__)
# print(hello.__doc__)
# help(hello)
"""
hello
Print a well-known message.
Help on function hello in module __main__:

hello()
    Print a well-known message.
"""
#==========================================================================
# def noop(f):
#     def noop_wrapper():
#         "Will replace doc information for the function"
#         return f()
#     return noop_wrapper
#
# @noop
# def hello():
#     "Print a well-known message"
#     print('hello world!')
# help(hello)
"""
Help on function noop_wrapper in module __main__:
noop_wrapper()
    Will replace doc information for the function
"""


#==========================================================================
import functools

def noop(f):
    @functools.wraps(f)
    def noop_wrapper():
        return f()
    return noop_wrapper()

@noop
def hello():
    "Print a well-known message"
    print('hello world!')

help(hello)



