#
# print(isinstance(3, int))  # True
# print(isinstance('hello', str))  # True
# print(isinstance(3.456, bytes))  # False
#
# x = []
# print(isinstance(x, (float, dict, list)))   # True

# ==============================================================================================================================

class SimpleList:
    def __init__(self, items):
        self._items = list(items)

    def add(self, item):
        self._items.append(item)

    def __getitem__(self, index):
        return self._items[index]

    def sort(self):
        self._items.sort()

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return "SimpleList({!r})".format(self._items)


class SortedList(SimpleList):
    def __init__(self, items=()):
        super().__init__(items)
        self.sort()

    def add(self, item):
        super().add(item)
        self.sort()

    def __repr__(self):
        return "SortedList({!r})".format(list(self))


class IntList(SimpleList):
    def __init__(self, items=()):
        for x in items:
            self._validate(x)
        super().__init__(items)

    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError('IntList only supports integers values.')

    def add(self, item):
        self._validate(item)
        super().add(item)

    def __repr__(self):
        return "IntList({!r})".format(list(self))


il = IntList([1,2,3,4])
il.add(19)
print(il)  # IntList([1, 2, 3, 4, 19])
il.add('5')
print(il)

# ==============================================================================================================================







# ==============================================================================================================================




