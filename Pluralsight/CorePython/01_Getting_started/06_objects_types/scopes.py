count = 0


def show_count():
    print(count)


def set_count(c):
    count = c


# print(show_count())  # 0 /n None
# print(set_count(5))  # None
# print(show_count())  # 0 /n None
#===============================

fount = 0


def show_fount():
    return fount


def set_fount(c):
    global fount
    fount = c
    return fount


print(show_fount())  # 0
print(set_fount(5))  # 5
print(show_fount())  # 5
