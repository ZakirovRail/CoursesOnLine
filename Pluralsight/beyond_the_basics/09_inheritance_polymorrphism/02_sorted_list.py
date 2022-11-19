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


sl = SortedList([4, 3, 78, 11])
print(sl)  # SortedList([3, 4, 11, 78])
sl.add(-43)
print(sl)   # SortedList([-43, 3, 4, 11, 78])


# ==============================================================================================================================





# ==============================================================================================================================







# ==============================================================================================================================




