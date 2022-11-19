from itertools import islice, count
from filtering_comprehensions import is_prime

# islice(all_primes, 1000)

thousands_primes = islice((x for x in count() if is_prime(x)), 1000)
print(thousands_primes)  # <itertools.islice object at 0x7febfb3ab130>
print(list(thousands_primes)[-10:])  # [7841, 7853, 7867, 7873, 7877, 7879, 7883, 7901, 7907, 7919]

print(any([False, False, True]))  # True
print(all([False, False, True]))  # False

print(all(name == name.title() for name in ['London', 'Paris', 'Tokyo', 'New York']))  # True
print('*' * 60)

sunday = [12, 13, 14, 15, 16, 17, 18]
monday = [22, 23, 24, 25, 26, 27, 28]

for item in zip(sunday, monday):
    print(item)
"""
(12, 22)
(13, 23)
(14, 24)
(15, 25)
(16, 26)
(17, 27)
(18, 28)
"""

for sun, mon in zip(sunday, monday):
    print('average = ', (sun + mon) / 2)
"""
average =  17.0
average =  18.0
average =  19.0
average =  20.0
average =  21.0
average =  22.0
average =  23.0
"""