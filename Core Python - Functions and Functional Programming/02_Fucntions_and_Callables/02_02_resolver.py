import socket


class Resolver:
    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

# resolve = Resolver()
# print(resolve('sixty-north.com')) # 93.93.131.30
# print(resolve.__call__('sixty-north.com')) # 93.93.131.30


"""
$python
>>> import resolver

>>> resolve=Resolver()
>>> resolve('sixrt-north.com')
'93.93.131.30'
>>> resolve.__call__('sixty-north.com')
'93.93.131.30'
>>> resolve._cache
{'sixty-north.com': '93.93.131.30'}
>>> resolve('pluralsight.com')
'54.148.56.39'
>>> resolve._cache
{'sixty-north.com': '93.93.131.30', 'pluralsight.com': '54.148.56.39'}



>>> from timeit import timeit
>>> timeit(setup="from __main__ import resolve", stmt ="resolve('google.com')", number = 1)
0.02722977000001947
>>> timeit(setup="from __main__ import resolve", stmt ="resolve('google.com')", number = 1)
7.505999974455335e-06
>>> print("{:f}".format(_))
0.000008


"""