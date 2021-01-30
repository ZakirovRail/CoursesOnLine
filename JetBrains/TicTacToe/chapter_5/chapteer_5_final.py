# lines = [[" "] * 3 for i in range(3)]


def create_field(lines):
    """
    create a game board for Tic Tac Toe
    :param lines
    :return:
    """

    print('-' * 9)
    for i in range(3):
        print('|', *lines[i], '|')
    print('-' * 9)


def check_board_win(lines):
    """
    the methode which verify if there are any win lines for "O" or for "X"
    :param lines
    :return "X", "O" or False:
    """

    win_variants = (
        (lines[0][0], lines[1][1], lines[2][2]),
        (lines[0][2], lines[1][1], lines[2][0]),
        (lines[0][1], lines[1][1], lines[2][1]),
        (lines[0][0], lines[0][1], lines[0][2]),
        (lines[1][0], lines[1][1], lines[1][2]),
        (lines[2][0], lines[2][1], lines[2][2]),
        (lines[0][0], lines[1][0], lines[2][0]),
        (lines[0][1], lines[1][1], lines[2][1]),
        (lines[0][2], lines[1][2], lines[2][2]),
    )

    if any(winner == ("X", "X", "X") for winner in win_variants):
        return "X"
    elif any(winner == ("O", "O", "O") for winner in win_variants):
        return "O"

    return False


def check_board(lines):
    finished = not any(x == "_" for y in lines for x in y)
    win = check_board_win(lines)

    if win:
        print(f"{win} wins")
    elif finished:
        print("Draw")
    else:
        return True


def main():
    lines = [["_"] * 3 for i in range(3)]

    create_field(lines)

    player = "X"

    while check_board(lines):
        while True:
            coordinates = input("Enter coordinates: > ")

            if coordinates.replace(" ", "").isnumeric():
                x, y = [int(c) for c in coordinates.split()]

                if 0 < x < 4 and 0 < y < 4:
                    real_x, real_y = x - 1, 3 - y

                    if lines[real_y][real_x] == "_":
                        lines[real_y][real_x] = player

                        player = "O" if player == "X" else "X"
                        break
                    else:
                        print("This cell is occupied! Choose another one!")
                else:
                    print("Coordinates should be from 1 to 3!")
            else:
                print("You should enter numbers!")

        create_field(lines)


if __name__ == "__main__":
    lines = [[" "] * 3 for i in range(3)]
    main()
