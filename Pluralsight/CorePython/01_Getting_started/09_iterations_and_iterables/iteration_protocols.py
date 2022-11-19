iterable_list = ["Spring", "Summer", "Autumn", "Winter"]
# iterator = iter(iterable)
# print(iterator)  # <list_iterator object at 0x7f9e05c2ab20>
# print(*iterator)  # Spring Summer Autumn Winter


def first(iterable):
    iterator  = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("Iterable is empty")


first_1 = first(iterable_list)
second_2 = first(iterable_list)
print(first_1)
print(second_2)
