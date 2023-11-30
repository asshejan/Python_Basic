def sumup(x, n):
    sum = 0
    n, x = int(n), int (x)
    for i in range(0, n+1, 2):
        sum += pow(x, i)
    return sum-1

x, n = input().split()

res = sumup(x, n)
print(res)