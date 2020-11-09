
a = int(input())
if a > 1:
    for i in range(2, a):
        if a % i == 0:
            print('This number is not prime')
            break
    else:
        print('This number is prime')
else:
    print('This number is not prime')
