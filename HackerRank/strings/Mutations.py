def mutate_string(string, position, character):
    parsed_string = list(string)
    parsed_string[position] = character
    new_string = ''.join(parsed_string)
    return new_string


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
