
def students_subscription():
    n, list_n = int(input()), set((input()).split())
    b, list_b = int(input()), set((input()).split())

    return len(list_n.intersection(list_b))


if __name__ == '__main__':
    print(students_subscription())
