# origin_list = list(input())
#
# line_1 = origin_list[0:3]
# line_2 = origin_list[3:6]
# line_3 = origin_list[6:]
# hor_1 = origin_list[0:3]
# hor_2 = origin_list[3:6]
# hor_3 = origin_list[6:]
# ver_1 = [origin_list[0], origin_list[3], origin_list[6]]
# ver_2 = [origin_list[1], origin_list[4], origin_list[7]]
# ver_3 = [origin_list[2], origin_list[5], origin_list[8]]
# cros_1 = [origin_list[0], origin_list[4], origin_list[8]]
# cros_2 = [origin_list[2], origin_list[4], origin_list[6]]
# x_signs = origin_list.count('X')
# o_signs = origin_list.count('O')
#
#
# def print_frame(line_1, line_2, line_3):
#     print('---------')
#     print('|', ' '.join(line_1), '|')
#     print('|', ' '.join(line_2), '|')
#     print('|', ' '.join(line_3), '|')
#     print('---------')
#
#
# if len(origin_list) < 9:
#     print_frame(line_1, line_2, line_3)
#     print('Game not finished')
# else:
#     if (x_signs - o_signs in (-1, 0, 1)) or (o_signs - x_signs in (-1, 0, 1)):
#         print(x_signs)  # TBD
#         print(o_signs)  # TBD
#         print(x_signs - o_signs)  # TBD
#         print(o_signs - x_signs)  # TBD
#
#         print_frame(line_1, line_2, line_3)
#         print('Success')
#     elif x_signs == o_signs:
#         print_frame(line_1, line_2, line_3)
#         print('Impossible')
#         print('Impossible because of equality') # TBD
#     elif abs(x_signs - o_signs) > 1:
#         print(x_signs)  # TBD
#         print(o_signs)  # TBD
#         print(x_signs - o_signs)  # TBD
#         print(o_signs - x_signs)  # TBD
#         print_frame(line_1, line_2, line_3)
#         print('Impossible')
#         print('Impossible because of to much different')  # TBD


#  --------------------------------------------------------------------------------------------------------------------
var_1 = 'XXXOO__O_'
var_2 = 'XOXOXOXXO'
var_3 = 'XOOOXOXXO'
var_4 = 'XOXOOXXXO'
var_5 = 'XO_OOX_X_'
var_6 = 'XO_XO_XOX'
var_7 = '_O_X__X_X'
var_8 = '_OOOO_X_X'

origin_list = input()
print("---------")
print("|", origin_list[0], origin_list[1], origin_list[2], "|")
print("|", origin_list[3], origin_list[4], origin_list[5], "|")
print("|", origin_list[6], origin_list[7], origin_list[8], "|")
print("---------")

result = ""
x_signs = [x for x in origin_list if x == "X"]
o_signs = [o for o in origin_list if o == "O"]
empty_lines = 9 - (len(x_signs) + len(o_signs))


def score(table, player):
    if (table[0] == table[1] == table[2] == player or table[3] == table[4] == table[5] == player
            or table[6] == table[7] == table[8] == player or table[0] == table[3] == table[6] == player
            or table[1] == table[4] == table[7] == player or table[2] == table[5] == table[8] == player
            or table[0] == table[4] == table[8] == player or table[2] == table[4] == table[6] == player):
        return True
    else:
        return False


if (len(x_signs) - len(o_signs) >= 2) or (len(o_signs) - len(x_signs) >= 2) or score(origin_list, "X") and score(
        origin_list, "O"):
    print("Impossible")
elif score(origin_list, "X"):
    print("X wins")
elif score(origin_list, "O"):
    print("O wins")
elif empty_lines > 0:
    print("Game not finished")
elif empty_lines == 0:
    print("Draw")
#  --------------------------------------------------------------------------------------------------------------------
