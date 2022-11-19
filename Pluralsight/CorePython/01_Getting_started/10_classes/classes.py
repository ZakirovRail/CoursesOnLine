# class Flight:
#     def number(self):
#         return "SN060"

# print(Flight.number())

"""
Traceback (most recent call last):
  File "/Users/Rail.zakirov/PycharmProjects/PluralSight/01_Getting_started/10_classes/classes.py", line 8, in <module>
    print(Flight.number(faker))
NameError: name 'faker' is not defined
"""

# f = Flight
# print(Flight.number(f))  # SN060
# =============


class Flight:
    def __init__(self, number):
        if not number[:2].isalpha():
            raise ValueError(f'No airline code in "{number}"')

        if not number[:2].isupper():
            raise ValueError(f'Invalid airline code "{number}"')

        if not number[2:].isdigit() and int(number[2:]) <= 9999:
            raise ValueError(f'Invalid route number "{number}"')

        self._number = number

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]


f = Flight("SN060")
print(f.number())  # SN060
