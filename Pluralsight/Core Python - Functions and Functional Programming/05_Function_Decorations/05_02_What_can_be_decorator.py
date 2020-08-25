#classes as decorators
# class CallCount:
#     def __init__(self, f):
#         self.f = f
#         self.count = 0
#     def __call__(self, *args, **kwargs):
#         self.count += 1
#         return self.f(*args, **kwargs)

# @CallCount
# def hello(name):
#     print('Hello, {}!'.format(name))

# hello('Fred')
# hello('Greg')
# hello('Bet')
# print(hello.count)
# hello('Greg')
# hello('Bet')
# print(hello.count)
"""
Hello, Fred!
Hello, Greg!
Hello, Bet!
3
Hello, Greg!
Hello, Bet!
5
"""
#==========================================================================
# Instances as Decorators
class Trace:
    def __init__(self):
        self.enabled = True
    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap
tracer = Trace()

@tracer
def rotate_list(l):
    return l[1:] + [l[0]]

l = [1,2,3]
print(l)  # [1, 2, 3]
# print(rotate_list(l))
# print(rotate_list(l))
# l = rotate_list(l)
tracer.enabled = False
print(rotate_list(l))


#==========================================================================







#==========================================================================







#==========================================================================
