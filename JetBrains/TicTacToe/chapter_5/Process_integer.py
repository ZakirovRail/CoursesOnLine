list_numbers = []
# N = int(input())

while True:
    N = int(input())
    if (N >= 10) and (N <= 100):
        list_numbers.append(N)
        # print(list_numbers)
    if N >= 100:
        break
print(*list_numbers, sep='\n')

# =====================================================================================================================
# lists = []
# while True:
#     x = int(input())
#     if x < 10:
#         continue
#     elif x > 100:
#         break
#     else:
#         lists.append(x)
# for x in lists:
#     print(x)