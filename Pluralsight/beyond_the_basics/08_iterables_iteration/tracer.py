class Tracer:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap


instance = Tracer()
result = map(instance(ord), 'The quick brown fox')
print(*result)





