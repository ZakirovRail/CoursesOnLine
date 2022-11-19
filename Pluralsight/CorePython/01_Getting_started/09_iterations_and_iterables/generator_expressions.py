"""
(expr(item) for item in iterable)
"""
from filtering_comprehensions import is_prime

# million_squares = (x*x for x in range(1, 1000001))
# print(million_squares)
# print(list(million_squares)[-10:])
# print(million_squares, million_squares)
#
# sum = sum(x*x for x in range(1, 1000001))
# print(sum)  # 333333833333500000


sum_prime = sum(x for x in range(1001) if is_prime(x))
print(sum_prime)

print(sum(x for x in range(1001) if is_prime(x)))

