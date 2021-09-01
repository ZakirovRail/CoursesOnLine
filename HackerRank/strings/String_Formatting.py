def print_formatted(number):
    width = len("{0:b}".format(number))
    for i in range(1, number + 1):
        i_decimal = (str(i)).rjust(width, ' ')
        i_oct = oct(i).replace('0o', '', 1).rjust(width, ' ')
        i_hex = (hex(i)).replace('0x', ''). upper().rjust(width, ' ')
        i_bin = (bin(i)).replace('0b', '').rjust(width, ' ')
        print (i_decimal, i_oct, i_hex, i_bin)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
