# s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
# S = [i for i in range(1, 10)]
# print(s)
# print(S)

# print(s.remove(4))  # None
# print(s)  # {1, 2, 3, 5, 6, 7, 8, 9}
# print(s.remove(0))  # KeyError: 0
# print(s.discard(0))  # None
# print(s.pop())  # 1
# print(s)  # {2, 3, 5, 6, 7, 8, 9}
# ===================================================
n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range(N):
    command = input().split()
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove':
        s.remove(int(command[1]))
    elif command[0] == 'discard':
        s.discard(int(command[1]))
    else:
        print('Some error happens')
print(sum(s))



