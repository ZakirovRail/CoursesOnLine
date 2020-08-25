# def escape_unicode(f):
#     def wrap(*args, **kwargs):
#         x = f(*args, **kwargs)
#         return x.encode('unicode-escape').decode('ascii')
#     return wrap

# class Trace:
#     def __init__(self):
#         self.enabled = True
#     def __call__(self, f):
#         def wrap(*args, **kwargs):
#             if self.enabled:
#                 print('Calling {}'.format(f))
#             return f(*args, **kwargs)
#         return wrap

# tracer = Trace()
# @tracer
# @escape_unicode
# def norwagian_island_maker(name):
#     return name + 'øy'


# print(norwagian_island_maker('Llama'))
# print(norwagian_island_maker('Python'))
# print(norwagian_island_maker('Troll'))
"""
Calling <function escape_unicode.<locals>.wrap at 0x0000018BBFFD58C8>
Llama\xf8y
Calling <function escape_unicode.<locals>.wrap at 0x0000018BBFFD58C8>
Python\xf8y
Calling <function escape_unicode.<locals>.wrap at 0x0000018BBFFD58C8>
Troll\xf8y
"""

#==========================================================================
#Decorating Methods
def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return x.encode('unicode-escape').decode('ascii')
    return wrap

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

class IslandMaker:
    def __init__(self, suffix):
        self.suffix = suffix
    @tracer
    def make_island(self, name):
        return name + self.suffix
im = IslandMaker(' Island')
im.make_island('Python')
print(im.make_island('Python'))
