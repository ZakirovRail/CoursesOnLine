# N, M = (input().split(' '))

# L = []
# for i in range(size):
#     s = "-".join(alpha[i:size])
#     L.append((s[::-1] + s[1:]).center(4 * size - 3, "-"))
# print('\n'.join(L[:0:-1] + L))

N, M = map(int, input().split())
for i in range(1, N, 2):
    print((i * ".|.").center(M, "-"))
print("WELCOME".center(M, "-"))
for i in range(N-2, -1, -2):
    print((i * ".|.").center(M, "-"))