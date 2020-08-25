message = 'global'


# def enclosing():
#     message = 'enclosing'
#
#     def local():
#         message = 'local'
#
#     print('enclosing message:', message)
#     local()
#     print('enclosing message:', message)
#
# print('global message', message)
# enclosing()
# print('global message', message)
"""
global message global
enclosing message: enclosing
enclosing message: enclosing
global message global
"""


#================================================================
message = 'global'

# def enclosing():
#     message = 'enclosing'
#     def local():
#         global message
#         message = 'local'
#     print('enclosing message:', message)
#     local()
#     print('enclosing message:', message)

# print('global message', message)
# enclosing()
# print('global message', message)
"""
global message global
enclosing message: enclosing
enclosing message: enclosing
global message local
"""

#================================================================
# message = 'global'
# def enclosing():
#     message = 'enclosing'
#     def local():
#         nonlocal message
#         message = 'local'
#     print('enclosing message:', message)
#     local()
#     print('enclosing message:', message)
# print('global message', message)
# enclosing()
# print('global message', message)
"""
global message global
enclosing message: enclosing
enclosing message: local
global message global
"""
#================================================================
import time
def make_timer():
    last_called = None # Never
    def elapsed():
        nonlocal last_called
        now = time.time()
        if last_called is None:
            last_called  = now
            return None
        result = now - last_called
        last_called = now
        return result
    return elapsed
t = make_timer()
print(make_timer())
print(make_timer())

print(t())
print(t())
print(t())
print(t())
print(t())







#================================================================


