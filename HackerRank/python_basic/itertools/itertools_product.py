from itertools import product

list_a = input().split(' ')
list_a = [int(i) for i in list_a]
list_b = input().split(' ')
list_b = [int(i) for i in list_b]

print(*(product(list_a, list_b)))



