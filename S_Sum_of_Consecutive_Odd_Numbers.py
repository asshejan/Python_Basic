def oddsum(n1, n2):
    if n1 > n2 : 
        n1, n2 = n2, n1
    sum = 0
    for d in range(n1 + 1, n2):
        if d % 2 == 1:
            sum += d
    return sum

t = int(input())

for _ in range(t):
    n1, n2 = map(int, input().split())
    res = oddsum(n1, n2)
    print(res)
