# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return '{}, {}'.format(self.x, self.y)
#
#     def __repr__(self):
#         return 'Point2D(x={}, y={})'.format(self.x, self.y)

# from str_repr import Point2D
# p = Point2D(x=42, y=69)
# print(str(p))
# print(repr(p))


# l = [Point2D(i, i * 2) for i in range(3)]
# print(str(l))  # [Point2D(x=0, y=0), Point2D(x=1, y=2), Point2D(x=2, y=4)]
# print(repr(l))  # [Point2D(x=0, y=0), Point2D(x=1, y=2), Point2D(x=2, y=4)]

# d = {i: Point2D(i, i *2) for i in range(3)}
# print(str(d))  # {0: Point2D(x=0, y=0), 1: Point2D(x=1, y=2), 2: Point2D(x=2, y=4)}
# print(repr(d))  # {0: Point2D(x=0, y=0), 1: Point2D(x=1, y=2), 2: Point2D(x=2, y=4)}

# print(f'this is a point: {Point2D(1, 2)}')  #   # {0: Point2D(x=0, y=0), 1: Point2D(x=1, y=2), 2: Point2D(x=2, y=4)}

# ==============================================================================================================


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '{}, {}'.format(self.x, self.y)

    def __repr__(self):
        return 'Point2D(x={}, y={})'.format(self.x, self.y)

    def __format__(self, f):
        return '[Formatted point: {}, {}, {}]'.format(self.x, self.y, f)

print(f'this is a point: {Point2D(1, 2)}')  # this is a point: [Formatted point: 1, 2, ]

 