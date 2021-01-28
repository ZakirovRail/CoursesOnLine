line = 'The quick brown fox jumped over the lazy dog.'


def reverse_other_words(line):
    list_words = line.split()
    second_words = list_words[1::2]
    first_words = list_words[::2]
    reversed_list = []  # ['ehT', 'nworb', 'depmuj', 'eht', '.god']
    final_list = []

    for i in first_words:
        reversed_list.append(i[::-1])
    print(reversed_list)

    len_first = len(reversed_list)
    len_second = len(second_words)
    counter_first = 0
    counter_second = 0

    # while (len_first != counter_first and len_second != counter_second) or (len_second != counter_second and len_first != counter_first):
    #     final_list.append(reversed_list[counter_first])
    #     final_list.append(second_words[counter_second])
    #     counter_first += 1
    #     counter_second += 1



    # print(len_first) # 5
    # print(len_second) # 4
    # print(final_list)



reverse_other_words(line)




