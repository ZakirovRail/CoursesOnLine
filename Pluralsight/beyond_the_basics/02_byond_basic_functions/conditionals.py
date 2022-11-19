# Conditional statement
# if condition:
#     result = true_value
# else:
#     result = false_value
#
#
# # Conditional expression:
# result = true_value if condition else false_value


def sequence_class(immutable):
    return tuple if immutable else list


seq = sequence_class(immutable=False)
s = seq("Nairobi")
print(s)
print(type(s))

seq_2 = sequence_class(immutable=True)
q = seq_2("Bahrein")
print(q)
print(type(q))
