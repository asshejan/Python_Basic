def maximum(N, A):

    even = all(x % 2 == 0 for x in A)

    if even:
        min_pow2 = min(bin(x)[::-1].index('1') for x in A)
        return min_pow2
    else:
        return 0

N = int(input())
A = list(map(int, input().split()))

result = maximum(N, A)
print(result)
