def swap_case(s):
    new_string = s.swapcase()
    return str(new_string)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
