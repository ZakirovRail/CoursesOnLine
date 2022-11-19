import sys
from itertools import count, islice


def sequence():
    seen = set()
    a = 0
    for n in count(1):
        yield a
        seen.add(a)
        c = a - n
        if c < 0 or c in seen:
            c = a + n
        a = c


def write_sequence(filename, num):
    f = open(filename, mode='wt', encoding='utf-8')
    f.writelines(f"{r}\n"
                 for r in islice(sequence(), num+1))
    f.close()


if __name__ == '__main':
    write_sequence(filename=sys.argv[1],
                   num=int(sys.argv[2]))
