string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'

vowel_counter = 0

for i in list(string):
    if i in list(vowels):
        vowel_counter += 1
print(vowel_counter)
# print(list(string))


