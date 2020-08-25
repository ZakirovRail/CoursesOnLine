# def count_words(doc):
#     normalised_doc = ''.join(c.lower() if c.isalpha() else ' ' for c in doc)
#     frequencies = {}
#     for word in normalised_doc.split():
#         frequencies[word] = frequencies.get(word, 0) + 1
#     return frequencies
# print(count_words('It was the best of times, it was the worst of times.')) # {'it': 2, 'was': 2, 'the': 2, 'best': 1, 'of': 2, 'times': 2, 'worst': 1}




#==========================================================================
from functools import reduce

def count_words(doc):
    normalised_doc = ''.join(c.lower() if c.isalpha() else ' ' for c in doc)
    frequencies = {}
    for word in normalised_doc.split():
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


documents = ['It was the best of times, it was the worst of times.', 'I went to the woods because I wished to live...',
             'Friends, Romas, contrymen, lend me your ears...']


counts = map(count_words, documents)
def combine_counts(d1, d2):
    d = d1.copy()
    for word, count in d2.items():
        d[word] = d.get(word, 0) + 1
    return d


total_counts = reduce(combine_counts, counts)
print(total_counts)

"""
{'it': 2, 'was': 2, 'the': 3, 'best': 1, 'of': 2, 'times': 2, 'worst': 1, 'i': 1, 'went': 1, 'to': 1, 'woods': 1, 
'because': 1, 'wished': 1, 'live': 1, 'friends': 1, 'romas': 1, 'contrymen': 1, 'lend': 1, 'me': 1, 
'your': 1, 'ears': 1}
"""
