def fromltor(num):
    num_str = str(num)
    for d in reversed(num_str):
        print(d, end=" ")

t = int(input())

for _ in range(t):
    n = int(input())

    fromltor(n)
    print()