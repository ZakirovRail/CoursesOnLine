def fibo(fib_n):
    if fib_n <= 1:
        return fib_n
    else:
        return (fibo(fib_n - 1) + fibo(fib_n - 2))

result = fibo(10)
print('fibo(10) = ' + str(result))