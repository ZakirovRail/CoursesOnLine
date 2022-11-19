import sys


def sqrt(x):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
    except ValueError as e:
        print(e, file=sys.stderr)




# main()


if __name__ == "main":
    print('start main')
    main()
    # print(sqrt(9))
    # print(sqrt(2))






