p = '/path/to/datafile.dat'


def process_file(f):
    pass


try:
    process_file(p)
except OSError as e:
    print(f'Error: {e}')
