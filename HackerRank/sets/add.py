num_count = int(input())
list_of_countries = set()

for i in range(num_count):
    country = input()
    # print(country)
    # print(type(country))
    list_of_countries.add(country)
print(len(list_of_countries))
