string = 'First ladies rule the State and state the rule: ladies first'



list_words = string.split()
# print(list_words)
new_list = []
suffix = 's'

for word in list_words:
    if word.endswith(suffix):
        new_list.append(word)
print('_'.join(new_list))