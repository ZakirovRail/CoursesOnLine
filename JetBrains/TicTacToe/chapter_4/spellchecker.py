dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']

list_words = input().split()
# print(list_words)
counter = 0

for word in list_words:
    if word not in dictionary:
        print(word, end='\n')
        counter += 1
if counter == 0:
    print('OK')