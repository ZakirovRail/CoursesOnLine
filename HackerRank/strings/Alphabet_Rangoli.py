def print_rangoli(size):
    myStr = 'abcdefghijklmnopqrstuvwxyz'[0:size]
    for i in range(size - 1, -size, -1):
        x = abs(i)
        # print('this x is equal to:', x)
        line = myStr[size:x:-1] + myStr[x:size]
        # print('this is line:',line)
        # print("--" * x + '-'.join(line) + "--" * x)
        print('-'.join(line))
        # print('-'.join(line).center(4 * (size - 1) + 1, '-'))
    # print('------------------------')
    #
    # for i in range(size - 1, -size, -1):
    #     x = abs(i)
    #     line = myStr[size:x:-1] + myStr[x:size]
    #     print('-'.join(line).center((size - 1) + 1, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
