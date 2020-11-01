origin_list = input()
print("---------")
print("|", origin_list[0], origin_list[1], origin_list[2], "|")
print("|", origin_list[3], origin_list[4], origin_list[5], "|")
print("|", origin_list[6], origin_list[7], origin_list[8], "|")
print("---------")

result = ""
x_signs = [x for x in origin_list if x == "X"]  # a list of x
o_signs = [o for o in origin_list if o == "O"]  # a list of o
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
