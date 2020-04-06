# def sequence_class(immutable):
#     if immutable:
#         cls=tuple
#     else:
#         cls = list
#     return cls
#
#
# seq = sequence_class(immutable=True)
# t = seq("Timbuktu")
# print(t)
# print(type(t))
# print("=" * len(t))
#==========================================================
# Conditional Expression


def sequence_class(immutable):
    return tuple if immutable else list


seq = sequence_class(immutable=False)
s = seq('Nairobi')
print(s)
print(type(s))