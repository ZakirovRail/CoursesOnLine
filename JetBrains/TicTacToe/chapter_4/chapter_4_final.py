def create_field():
    print('---------')
    for i in range(len(matrix)):
        row = ''.join(matrix[i]).replace('_', ' ')
        print('|', *row, '|')
    print('---------')


def check_input(x):
    if not x.isnumeric():
        print('You should enter numbers!')
        return False
    i = int(x)
    if i < 1 or i > 3:
        print('Coordinates should be from 1 to 3!')
        return False
    return True


if __name__ == '__main__':
    origin_list = list(input('Enter cells: '))
    matrix = [origin_list[0:3], origin_list[3:6], origin_list[6:9]]
    create_field()
    while True:
        x, y = (input('Enter the coordinates: ').split())
        if check_input(x) and check_input(y):
            x = int(x)
            y = -(int(y))
            if matrix[y][x - 1] == '_':
                matrix[y][x - 1] = 'X'
                create_field()
                break
            else:
                print('This cell is occupied! Choose another one!')

#  =====================================================================================================================
# Other variants pieces of code

# def check_input(x, y):
#     list_letters = list(
#         string.ascii_letters)  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
#     # 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
#     # 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     list_symbols = list(
#         string.punctuation)  # ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':',
#     # ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
#     list_whitespace = list(string.whitespace)  # [' ', '\t', '\n', '\r', '\x0b', '\x0c']
#
#     if (int(x) not in (1, 2, 3)) and (int(y) not in (1, 2, 3)) is True:
#         print('Coordinates should be from 1 to 3!')
#     if (x in list_letters or x in list_symbols or x in list_whitespace) or (
#             y in list_letters or y in list_symbols or y in list_whitespace):
#         print('You should enter numbers!')
