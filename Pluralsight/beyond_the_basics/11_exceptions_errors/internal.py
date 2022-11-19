
def modulus_tree(n):
    r = n % 3
    if r == 0:
        print("Multiple of 3")
    elif r == 1:
        print("Reminder 1")
    else:
        assert r == 2, "reminder is not 2"
        print("Reminder 2")


def modulus_four(n):
    r = n % 4
    if r == 0:
        print("Multiple of 4")
    elif r == 1:
        print("Reminder 1")
    elif r == 2:
        print("Reminder 2")
    elif r == 3:
        print("Reminder 3")
    else:
        assert False, "This should never happen"
