def count_substring(string, sub_string):
    # faster
    counter = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            counter += 1
    return counter


    # slower
    # counter = 0
    # while sub_string in string:
    #     i = string.find(sub_string)
    #     string = string[:1] + string[i + 1:]
    #     counter += 1
    # return counter


if __name__ == '__main__':
    string = 'aabraacaadbraa'
    sub_string = 'aa'

    count = count_substring(string, sub_string)
    print(count)
