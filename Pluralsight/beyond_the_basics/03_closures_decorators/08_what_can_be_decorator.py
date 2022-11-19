class CountCall:
    def __init__(self, f):
        self.f = f
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.f(*args, **kwargs)


@CountCall
def hello(name):
    print("Hello, {}".format(name))


hello("Jhon")
hello("Mike")
hello("Sara")
hello("Olga")
print(hello.count)


