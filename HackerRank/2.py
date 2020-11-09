line = 'The quick brown fox jumped over the lazy dog.'


def reverse_other_words(line):
    line = line.split() # ['The', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog.']
    print(line)
    for i in line[::2]:
        print(i[::-1])
        # print(i)
        # print(i[::-1])
        # i == i[::-1]
    print(line)






reverse_other_words(line)




