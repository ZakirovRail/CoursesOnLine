def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)


N = int(input(''))
if N in range(1, 100):
    print(factorial(N))


#  ====================================================================================================================
n_number = 1
inp_number = int(input())

while inp_number > 0:
    n_number = n_number * inp_number
    inp_number -= 1
print(n_number)