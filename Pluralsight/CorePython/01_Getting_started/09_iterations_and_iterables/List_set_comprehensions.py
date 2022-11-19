from math import factorial

words = 'Why sometimes I have believed as many as six impossible things before breakfast'.split()
print(words)

comp_list = [len(word) for word in words]
print(comp_list)

f = [len(str(factorial(x))) for x in range(20)]
print(f)

set_fact = {len(str(factorial(x))) for x in range(20)}
print(set_fact)


