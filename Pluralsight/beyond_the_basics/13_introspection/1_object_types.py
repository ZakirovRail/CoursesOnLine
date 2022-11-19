i = 7
print(type(i))  # <class 'int'>
print(repr(i))  # 7
print(type(type(i)))  # <class 'type'>
print(i.__class__)  # <class 'int'>
print(isinstance(i, int))  # True
