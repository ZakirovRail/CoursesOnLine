# s = set('Hacker')
# print(s)  # {'a', 'H', 'e', 'r', 'k', 'c'}
# # ==============
# print(s.union('Rank'))  # {'c', 'n', 'R', 'k', 'a', 'r', 'H', 'e'}
# print(s.union(enumerate('Rank')))  # {'H', (2, 'n'), 'c', 'a', (0, 'R'), 'e', 'k', (3, 'k'), (1, 'a'), 'r'}


def students_subscription():
    n, list_n = int(input()), set((input()).split())
    b, list_b = int(input()), set((input()).split())

    return len(list_n.union(list_b))


if __name__ == '__main__':
    print(students_subscription())
