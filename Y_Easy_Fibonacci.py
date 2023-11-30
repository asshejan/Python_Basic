def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input())

for d in range(1, num + 1):
    res = fibonacci(d)
    if d == num+1 : print(res)
    else : print(res, end=" ")
