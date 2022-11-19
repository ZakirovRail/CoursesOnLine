# class ExampleIterator:
#     def __init__(self):
#         self.index = 0
#         self.data = [1, 2, 3]
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.data):
#             raise StopIteration()
#
#         rslt = self.data[self.index]
#         self.index += 1
#         return rslt
#
# i = ExampleIterator()
# print(next(i)) # 1
# print(next(i)) # 2
# print(next(i)) # 3

# ==============================================================================================================================
# class ExampleIterator:
#     def __init__(self, data):
#         self.index = 0
#         self.data = data
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= len(self.data):
#             raise StopIteration()
#
#         rslt = self.data[self.index]
#         self.index += 1
#         return rslt
#
#
# class ExampleIterable:
#     def __init__(self):
#         self.data = [1, 2, 3]
#
#     def __iter__(self):
#         return ExampleIterator(self.data)
#
#
# for i in ExampleIterable():
#     print(i)
#
# lis_iter = [i for i in ExampleIterable()]
# print(lis_iter)
# ==============================================================================================================================
# Alternative Iterable protocol

class AlternateIterable:
    def __init__(self):
        self.data = [1, 2, 3]

    def __getitem__(self, idx):
        return self.data[idx]


lis_iter = [i for i in AlternateIterable()]
print(lis_iter)  # [1, 2, 3]


