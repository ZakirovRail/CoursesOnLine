# string = 'Nobody expects the Spanish inquisition! And you?!'

string = input()
new_string = string.replace('!', '')
new_string_2 = new_string.replace('?', '')
new_string_3 = new_string_2.replace('.', '')
new_string_4 = new_string_3.replace(',', '')
print(new_string_4.lower())
