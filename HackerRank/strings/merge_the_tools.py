def merge_the_tools(string, k):
    list_lines = [string[i:i + k] for i in range(0, len(string), k)]
    print(list_lines)
    final_list = []
    for substring in list_lines:
        print(substring)
        unique = []
        for letter in substring:
            if letter not in unique:
                unique += letter
        final_list.append(''.join(unique))
    print(final_list)
    for sub in final_list:
        print(sub)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
