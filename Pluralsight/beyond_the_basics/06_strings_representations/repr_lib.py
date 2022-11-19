import reprlib


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '{}, {}'.format(self.x, self.y)

    def __repr__(self):
        return 'Point2D(x={}, y={})'.format(self.x, self.y)

    def __format__(self, f):
        if f == 'i':
            return '{}, {}'.format(self.y, self.x)
        else:
            return '{}, {}'.format(self.x, self.y)


points = [Point2D(x, y) for x in range(1000) for y in range(1000)]
len(points)
# print(reprlib.repr(points))  # [Point2D(x=0, y=0), Point2D(x=0, y=1), Point2D(x=0, y=2), Point2D(x=0, y=3), Point2D(x=0, y=4), Point2D(x=0, y=5), ...]
# print((points))  # [Point2D(x=0, y=0), Point2D(x=0, y=1), Point2D(x=0, y=2), Point2D(x=0, y=3), Point2D(x=0, y=4), Point2D(x=0, y=5), ...]





